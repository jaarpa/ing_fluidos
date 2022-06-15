import math
import fluids as fluids_pkg
from CoolProp import CoolProp as CP

from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from numpy import angle

# Create your models here.
KNOWN_VISCOSITY_FLUIDS = [
    'Air',
    'Ammonia',
    'Argon',
    'Benzene',
    'CarbonDioxide',
    'CycloHexane',
    'Cyclopentane',
    'DimethylEther',
    'Ethane',
    'Ethanol',
    'EthylBenzene',
    'HeavyWater',
    'Helium',
    'Hydrogen',
    'HydrogenSulfide',
    'IsoButane',
    'Isopentane',
    'Methane',
    'Methanol',
    'Nitrogen',
    'Oxygen',
    'Propylene',
    'R11',
    'R116',
    'R12',
    'R123',
    'R1233zd(E)',
    'R1234yf',
    'R1234ze(E)',
    'R124',
    'R125',
    'R13',
    'R134a',
    'R14',
    'R141b',
    'R143a',
    'R152A',
    'R218',
    'R22',
    'R227EA',
    'R23',
    'R236EA',
    'R236FA',
    'R245fa',
    'R32',
    'R404A',
    'R407C',
    'R410A',
    'R507A',
    'SulfurHexafluoride',
    'Toluene',
    'Water',
    'm-Xylene',
    'n-Butane',
    'n-Decane',
    'n-Dodecane',
    'n-Heptane',
    'n-Hexane',
    'n-Nonane',
    'n-Octane',
    'n-Pentane',
    'n-Propane',
    'o-Xylene',
    'p-Xylene'
]


class Project(models.Model):
    name = models.CharField(_("Project name"), max_length=100)
    fluid = models.CharField(
        _("Fluid"), max_length=20,
        choices=zip(KNOWN_VISCOSITY_FLUIDS, KNOWN_VISCOSITY_FLUIDS)
    )
    # [m^3/s]
    flux = models.FloatField(_("Mean flux [m^3/s]"))
    # [K]
    T_av = models.FloatField(_("Mean temperature [°C]"))
    # [Pa]
    P_av = models.FloatField(_("Mean Presssure [Pa]"), default=101325)

    class Meta:
        verbose_name = _("Project")
        verbose_name_plural = _("Projects")
        ordering = ["-id"]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("piping:project_detail", kwargs={"pk": self.pk})

    def get_rho(self):
        return CP.PropsSI(
            "D", "P", self.P_av, "T", self.get_K_temp(), self.fluid
        )

    def get_mu(self):
        return CP.PropsSI(
            "V", "P", self.P_av, "T", self.get_K_temp(), self.fluid
        )

    def get_K_temp(self):
        return self.T_av + 273.15

    def get_dPa(self):
        k = 0
        accesories = self.projectaccessory_set.all()
        for accessory in accesories:
            k += accessory.get_K()
        k += fluids_pkg.entrance_sharp()
        k += fluids_pkg.exit_normal()
        if not accesories.exists():
            return 0
        V1 = accesories.first().get_V()
        return fluids_pkg.dP_from_K(k, rho=self.get_rho(), V=V1)

    def get_sigma_f(self):
        return self.get_dPa()/self.get_rho()


def get_available_accessories():
    accessories = [
        "straight_pipe", "bend_rounded", "diffuser_sharp", "contraction_sharp"
    ]
    valves = [
        "K_gate_valve_Crane", "K_angle_valve_Crane", "K_globe_valve_Crane",
        "K_swing_check_valve_Crane", "K_lift_check_valve_Crane",
        "K_tilting_disk_check_valve_Crane", "K_globe_stop_check_valve_Crane",
        "K_angle_stop_check_valve_Crane", "K_ball_valve_Crane",
        "K_diaphragm_valve_Crane", "K_foot_valve_Crane",
        "K_butterfly_valve_Crane", "K_plug_valve_Crane"
    ]
    valves.sort()
    accessory_names = [
        _(name.replace("_", " ").capitalize())
        for name in accessories
    ]
    accessories += valves
    accessory_names += [
        _(" ".join(a.split("_")[1:-1]).capitalize())
        for a in accessories[4:]
    ]

    return zip(accessories, accessory_names)


class ProjectAccessory(models.Model):

    project = models.ForeignKey(
        "piping.Project", verbose_name=_("Project"), on_delete=models.CASCADE
    )
    accessory = models.CharField(
        _("Accessory"), max_length=50, choices=get_available_accessories()
    )
    quantity = models.FloatField(_("Quantity [m] or units"))
    material = models.CharField(
        _("Material"), max_length=50,
        choices=zip(
            fluids_pkg.friction.roughness_clean_names,
            fluids_pkg.friction.roughness_clean_names
        )
    )
    inner_diameter = models.FloatField(_("Inner diameter [m]"))
    inner_diameter2 = models.FloatField(
        _("Inner diameter 2 [m]"), blank=True, null=True
    )
    angle = models.FloatField(
        _("Angle [°]"), blank=True, null=True
    )

    class Meta:
        verbose_name = _("Pipe Accessory")
        verbose_name_plural = _("Pipe Accesories")
        ordering = ["-id"]

    def __str__(self):
        return self.accessory

    def get_V(self):
        D1 = self.inner_diameter
        flux = self.project.flux
        V = flux / ((math.pi * D1**2) / 4)
        return V

    def get_K(self):
        rho = self.project.get_rho()
        mu = self.project.get_mu()
        D1 = self.inner_diameter
        D2 = self.inner_diameter2
        V = self.get_V()
        Re = fluids_pkg.Reynolds(V=V, D=D1, rho=rho, mu=mu)
        epsilon = fluids_pkg.material_roughness(self.material)
        fd = fluids_pkg.friction_factor(Re, eD=epsilon/D1)
        if self.accessory == "straight_pipe":
            k = fluids_pkg.K_from_f(fd=fd, L=self.quantity, D=D1)
        elif self.accessory == "bend_rounded":
            k = fluids_pkg.bend_rounded(Di=D1, angle=self.angle, fd=fd)
        elif self.accessory == "diffuser_sharp":
            k = fluids_pkg.diffuser_sharp(D1, D2, fd=fd)
        elif self.accessory == "contraction_sharp":
            k = fluids_pkg.contraction_sharp(D1, D2, fd=fd)
        elif self.accessory == "K_angle_stop_check_valve_Crane":
            k = fluids_pkg.K_angle_stop_check_valve_Crane(
                D1, D2, fd=fd
            )
        elif self.accessory == "K_angle_valve_Crane":
            k = fluids_pkg.K_angle_valve_Crane(
                D1, D2, fd=fd
            )
        elif self.accessory == "K_ball_valve_Crane":
            k = fluids_pkg.K_ball_valve_Crane(
                D1, D2, angle=angle, fd=fd
            )
        elif self.accessory == "K_butterfly_valve_Crane":
            k = fluids_pkg.K_butterfly_valve_Crane(
                D=D1, fd=fd
            )
        elif self.accessory == "K_diaphragm_valve_Crane":
            k = fluids_pkg.K_diaphragm_valve_Crane(
                D=D1, fd=fd
            )
        elif self.accessory == "K_foot_valve_Crane":
            k = fluids_pkg.K_foot_valve_Crane(
                D=D1, fd=fd
            )
        elif self.accessory == "K_gate_valve_Crane":
            k = fluids_pkg.K_gate_valve_Crane(
                D1=D1, D2=D2, angle=angle, fd=fd
            )
        elif self.accessory == "K_globe_valve_Crane":
            k = fluids_pkg.K_globe_valve_Crane(
                D1=D1, D2=D2, fd=fd
            )
        elif self.accessory == "K_lift_check_valve_Crane":
            k = fluids_pkg.K_lift_check_valve_Crane(
                D1=D1, D2=D2, fd=fd
            )
        elif self.accessory == "K_plug_valve_Crane":
            k = fluids_pkg.K_plug_valve_Crane(
                D1=D1, D2=D2, angle=angle, fd=fd
            )
        elif self.accessory == "K_swing_check_valve_Crane":
            k = fluids_pkg.K_swing_check_valve_Crane(
                D=D1, fd=fd
            )
        elif self.accessory == "K_tilting_disk_check_valve_Crane":
            k = fluids_pkg.K_tilting_disk_check_valve_Crane(
                D=D1, angle=angle, fd=fd
            )
        return k

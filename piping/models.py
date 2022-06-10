from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

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
    # [K]
    T_av = models.FloatField(_("Mean temperature [°C]"))
    # [Pa]
    P_av = models.FloatField(_("Mean Presssure [Pa]"), default=101325)

    class Meta:
        verbose_name = _("Project")
        verbose_name_plural = _("Projects")
        ordering = ["id"]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("piping:project_detail", kwargs={"pk": self.pk})

    def get_T_C(self):
        return self.T_av-273.15

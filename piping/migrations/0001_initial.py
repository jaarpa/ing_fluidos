# Generated by Django 3.2.5 on 2022-06-09 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Project name')),
                ('fluid', models.CharField(choices=[('R1233zd(E)', 'R1233zd(E)'), ('R1234yf', 'R1234yf'), ('Nitrogen', 'Nitrogen'), ('R114', 'R114'), ('OrthoDeuterium', 'OrthoDeuterium'), ('SulfurHexafluoride', 'SulfurHexafluoride'), ('R115', 'R115'), ('n-Nonane', 'n-Nonane'), ('Acetone', 'Acetone'), ('R12', 'R12'), ('R245fa', 'R245fa'), ('R23', 'R23'), ('R124', 'R124'), ('MD3M', 'MD3M'), ('Isopentane', 'Isopentane'), ('Krypton', 'Krypton'), ('R1243zf', 'R1243zf'), ('n-Decane', 'n-Decane'), ('n-Undecane', 'n-Undecane'), ('Ethylene', 'Ethylene'), ('m-Xylene', 'm-Xylene'), ('R245ca', 'R245ca'), ('R507A', 'R507A'), ('R152A', 'R152A'), ('MM', 'MM'), ('R236EA', 'R236EA'), ('R125', 'R125'), ('R40', 'R40'), ('R11', 'R11'), ('Helium', 'Helium'), ('MethylPalmitate', 'MethylPalmitate'), ('CycloPropane', 'CycloPropane'), ('Water', 'Water'), ('Methanol', 'Methanol'), ('Isohexane', 'Isohexane'), ('OrthoHydrogen', 'OrthoHydrogen'), ('Ethanol', 'Ethanol'), ('HydrogenChloride', 'HydrogenChloride'), ('Deuterium', 'Deuterium'), ('n-Dodecane', 'n-Dodecane'), ('R143a', 'R143a'), ('D4', 'D4'), ('RC318', 'RC318'), ('cis-2-Butene', 'cis-2-Butene'), ('R41', 'R41'), ('NitrousOxide', 'NitrousOxide'), ('n-Propane', 'n-Propane'), ('R14', 'R14'), ('R21', 'R21'), ('Fluorine', 'Fluorine'), ('D5', 'D5'), ('R1234ze(E)', 'R1234ze(E)'), ('CycloHexane', 'CycloHexane'), ('R113', 'R113'), ('DimethylCarbonate', 'DimethylCarbonate'), ('DimethylEther', 'DimethylEther'), ('Hydrogen', 'Hydrogen'), ('n-Butane', 'n-Butane'), ('HFE143m', 'HFE143m'), ('D6', 'D6'), ('n-Hexane', 'n-Hexane'), ('Novec649', 'Novec649'), ('MethylLinoleate', 'MethylLinoleate'), ('Propyne', 'Propyne'), ('R134a', 'R134a'), ('Argon', 'Argon'), ('Dichloroethane', 'Dichloroethane'), ('Ethane', 'Ethane'), ('MDM', 'MDM'), ('MethylOleate', 'MethylOleate'), ('Xenon', 'Xenon'), ('Ammonia', 'Ammonia'), ('R410A', 'R410A'), ('MethylLinolenate', 'MethylLinolenate'), ('R161', 'R161'), ('Methane', 'Methane'), ('SES36', 'SES36'), ('R407C', 'R407C'), ('R123', 'R123'), ('Propylene', 'Propylene'), ('CarbonMonoxide', 'CarbonMonoxide'), ('Cyclopentane', 'Cyclopentane'), ('trans-2-Butene', 'trans-2-Butene'), ('Benzene', 'Benzene'), ('Neopentane', 'Neopentane'), ('MD4M', 'MD4M'), ('R141b', 'R141b'), ('DiethylEther', 'DiethylEther'), ('CarbonylSulfide', 'CarbonylSulfide'), ('IsoButane', 'IsoButane'), ('R13I1', 'R13I1'), ('R142b', 'R142b'), ('Air', 'Air'), ('R236FA', 'R236FA'), ('R227EA', 'R227EA'), ('ParaDeuterium', 'ParaDeuterium'), ('Neon', 'Neon'), ('R13', 'R13'), ('R404A', 'R404A'), ('R365MFC', 'R365MFC'), ('n-Octane', 'n-Octane'), ('R116', 'R116'), ('MD2M', 'MD2M'), ('n-Pentane', 'n-Pentane'), ('n-Heptane', 'n-Heptane'), ('Oxygen', 'Oxygen'), ('o-Xylene', 'o-Xylene'), ('R1234ze(Z)', 'R1234ze(Z)'), ('CarbonDioxide', 'CarbonDioxide'), ('p-Xylene', 'p-Xylene'), ('IsoButene', 'IsoButene'), ('1-Butene', '1-Butene'), ('R218', 'R218'), ('R32', 'R32'), ('R22', 'R22'), ('EthyleneOxide', 'EthyleneOxide'), ('ParaHydrogen', 'ParaHydrogen'), ('EthylBenzene', 'EthylBenzene'), ('HeavyWater', 'HeavyWater'), ('MethylStearate', 'MethylStearate'), ('Toluene', 'Toluene'), ('HydrogenSulfide', 'HydrogenSulfide'), ('SulfurDioxide', 'SulfurDioxide')], max_length=20, verbose_name='Fluid')),
                ('T_av', models.FloatField(verbose_name='Mean temperature')),
            ],
            options={
                'verbose_name': 'project',
                'verbose_name_plural': 'projects',
            },
        ),
    ]

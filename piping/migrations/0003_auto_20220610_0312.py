# Generated by Django 3.2.5 on 2022-06-10 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('piping', '0002_auto_20220610_0004'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['id'], 'verbose_name': 'Project', 'verbose_name_plural': 'Projects'},
        ),
        migrations.AddField(
            model_name='project',
            name='P_av',
            field=models.FloatField(default=101325, verbose_name='Mean Presssure [Pa]'),
        ),
        migrations.AlterField(
            model_name='project',
            name='T_av',
            field=models.FloatField(verbose_name='Mean temperature [°C]'),
        ),
        migrations.AlterField(
            model_name='project',
            name='fluid',
            field=models.CharField(choices=[('Air', 'Air'), ('Ammonia', 'Ammonia'), ('Argon', 'Argon'), ('Benzene', 'Benzene'), ('CarbonDioxide', 'CarbonDioxide'), ('CycloHexane', 'CycloHexane'), ('Cyclopentane', 'Cyclopentane'), ('DimethylEther', 'DimethylEther'), ('Ethane', 'Ethane'), ('Ethanol', 'Ethanol'), ('EthylBenzene', 'EthylBenzene'), ('HeavyWater', 'HeavyWater'), ('Helium', 'Helium'), ('Hydrogen', 'Hydrogen'), ('HydrogenSulfide', 'HydrogenSulfide'), ('IsoButane', 'IsoButane'), ('Isopentane', 'Isopentane'), ('Methane', 'Methane'), ('Methanol', 'Methanol'), ('Nitrogen', 'Nitrogen'), ('Oxygen', 'Oxygen'), ('Propylene', 'Propylene'), ('R11', 'R11'), ('R116', 'R116'), ('R12', 'R12'), ('R123', 'R123'), ('R1233zd(E)', 'R1233zd(E)'), ('R1234yf', 'R1234yf'), ('R1234ze(E)', 'R1234ze(E)'), ('R124', 'R124'), ('R125', 'R125'), ('R13', 'R13'), ('R134a', 'R134a'), ('R14', 'R14'), ('R141b', 'R141b'), ('R143a', 'R143a'), ('R152A', 'R152A'), ('R218', 'R218'), ('R22', 'R22'), ('R227EA', 'R227EA'), ('R23', 'R23'), ('R236EA', 'R236EA'), ('R236FA', 'R236FA'), ('R245fa', 'R245fa'), ('R32', 'R32'), ('R404A', 'R404A'), ('R407C', 'R407C'), ('R410A', 'R410A'), ('R507A', 'R507A'), ('SulfurHexafluoride', 'SulfurHexafluoride'), ('Toluene', 'Toluene'), ('Water', 'Water'), ('m-Xylene', 'm-Xylene'), ('n-Butane', 'n-Butane'), ('n-Decane', 'n-Decane'), ('n-Dodecane', 'n-Dodecane'), ('n-Heptane', 'n-Heptane'), ('n-Hexane', 'n-Hexane'), ('n-Nonane', 'n-Nonane'), ('n-Octane', 'n-Octane'), ('n-Pentane', 'n-Pentane'), ('n-Propane', 'n-Propane'), ('o-Xylene', 'o-Xylene'), ('p-Xylene', 'p-Xylene')], max_length=20, verbose_name='Fluid'),
        ),
    ]

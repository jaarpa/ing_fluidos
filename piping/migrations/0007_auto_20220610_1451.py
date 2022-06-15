# Generated by Django 3.2.5 on 2022-06-10 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('piping', '0006_auto_20220610_1448'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='flux',
            field=models.FloatField(default=0.01, verbose_name='Mean temperature [m^3/s]'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='projectaccessory',
            name='material',
            field=models.CharField(choices=[('Cr13, electropolished bare', 'Cr13, electropolished bare'), ('Cement lining', 'Cement lining'), ('Rough riveted steel', 'Rough riveted steel'), ('Rough wood stave', 'Rough wood stave'), ('Rough concrete', 'Rough concrete'), ('Galvanized iron', 'Galvanized iron'), ('Wood stave', 'Wood stave'), ('Carbon steel, bare', 'Carbon steel, bare'), ('Plastic coated', 'Plastic coated'), ('Concrete', 'Concrete'), ('Lead', 'Lead'), ('Cast iron', 'Cast iron'), ('Asphalted cast iron', 'Asphalted cast iron'), ('Fiberglass lining', 'Fiberglass lining'), ('Riveted steel', 'Riveted steel'), ('Steel', 'Steel'), ('Glass', 'Glass'), ('Brass', 'Brass'), ('Cr13, bare', 'Cr13, bare'), ('Carbon steel, honed bare', 'Carbon steel, honed bare')], max_length=50, verbose_name='Material'),
        ),
    ]
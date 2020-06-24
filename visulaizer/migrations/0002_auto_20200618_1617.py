# Generated by Django 3.0.7 on 2020-06-18 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visulaizer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formdetails',
            name='Category',
            field=models.CharField(choices=[('BR', 'Blowroom'), ('WC', 'Waste Collection '), ('CRD', 'Carding'), ('CD', 'Comber and Drawing'), ('SF', 'Speed Frame'), ('PRT', 'Pre Total'), ('SPG1', 'Spg DB1'), ('SPG2', 'Spg DB2'), ('SPG3', 'Spg DB3'), ('SPG4', 'Spg DB4'), ('SPGTOTAL', 'Spg Total'), ('AC', 'Autoconner'), ('PST', 'Post spinning total'), ('PREHMD', 'Pre HMD'), ('SPG1HMD', 'Spg1 HMD'), ('SPG2HMD', 'Spg2 HMD'), ('PSPGHMD', 'Post Spg HMD'), ('TO', 'Total'), ('CP', 'Compressor'), ('LT', 'Lighting'), ('TU', 'Total Units'), ('PRD', 'Production'), ('U. K. G.', 'U. K. G.'), ('40s Con Pro', '40s Con Pro'), ('40s Con Ukg', '40s Con Ukg'), ('40s compac Con Pro', '40s compac Con Pro'), ('40s compac Con ukg', '40s compac Con ukg')], max_length=200, null=True),
        ),
    ]
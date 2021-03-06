# Generated by Django 2.2.10 on 2020-11-07 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medical', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='gentotype',
            field=models.CharField(choices=[('AA', 'AA'), ('AS', 'AS'), ('AC', 'AC'), ('SS', 'SS'), ('SC', 'SC'), ('CC', 'CC')], default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='patient',
            name='blood_group',
            field=models.CharField(choices=[('A RhD positive', 'A+'), ('A RhD negative', 'A-'), ('B RhD positive', 'B+'), ('B RhD negative', 'B-'), ('O RhD positive', 'O+'), ('O RhD negative', 'O-')], default='', max_length=100),
        ),
    ]

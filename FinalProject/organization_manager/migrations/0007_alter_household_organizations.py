# Generated by Django 5.0.4 on 2024-04-22 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization_manager', '0006_remove_household_household_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='household',
            name='organizations',
            field=models.ManyToManyField(blank=True, to='organization_manager.organization'),
        ),
    ]

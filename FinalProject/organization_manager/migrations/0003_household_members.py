# Generated by Django 5.0.4 on 2024-04-22 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization_manager', '0002_alter_household_organizations'),
    ]

    operations = [
        migrations.AddField(
            model_name='household',
            name='members',
            field=models.ManyToManyField(blank=True, null=True, related_name='members_of_household', to='organization_manager.person'),
        ),
    ]

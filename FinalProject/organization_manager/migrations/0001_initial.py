# Generated by Django 5.0.4 on 2024-04-22 01:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('org_ID', models.AutoField(primary_key=True, serialize=False)),
                ('organization_name', models.CharField(max_length=80)),
                ('organization_description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Household',
            fields=[
                ('household_ID', models.AutoField(primary_key=True, serialize=False)),
                ('address', models.TextField(blank=True, null=True)),
                ('organizations', models.ManyToManyField(to='organization_manager.organization')),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('person_ID', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=20)),
                ('middle_name', models.CharField(blank=True, max_length=20, null=True)),
                ('last_name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('household', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='organization_manager.household')),
                ('spouse', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='organization_manager.person')),
            ],
        ),
        migrations.AddField(
            model_name='household',
            name='household_contact',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='contact_person', to='organization_manager.person'),
        ),
    ]
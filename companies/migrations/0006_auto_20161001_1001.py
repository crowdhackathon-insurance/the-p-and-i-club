# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-10-01 10:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0005_proposalformbooleanfield_proposalformfilefield_proposalformnumberfield_proposalformtextfield'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProposalFormField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('required', models.BooleanField(default=True)),
                ('field_type', models.CharField(choices=[('boolean', 'Boolean'), ('text', 'Text'), ('float', 'Float'), ('file', 'File')], max_length=255)),
                ('value', models.CharField(max_length=255)),
                ('proposal_form', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='companies.ProposalForm')),
            ],
        ),
        migrations.RemoveField(
            model_name='proposalformbooleanfield',
            name='proposal_form',
        ),
        migrations.RemoveField(
            model_name='proposalformfilefield',
            name='proposal_form',
        ),
        migrations.RemoveField(
            model_name='proposalformnumberfield',
            name='proposal_form',
        ),
        migrations.RemoveField(
            model_name='proposalformtextfield',
            name='proposal_form',
        ),
        migrations.DeleteModel(
            name='ProposalFormBooleanField',
        ),
        migrations.DeleteModel(
            name='ProposalFormFileField',
        ),
        migrations.DeleteModel(
            name='ProposalFormNumberField',
        ),
        migrations.DeleteModel(
            name='ProposalFormTextField',
        ),
    ]

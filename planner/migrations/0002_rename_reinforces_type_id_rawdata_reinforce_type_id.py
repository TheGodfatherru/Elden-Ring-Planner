# Generated by Django 4.1.3 on 2022-11-28 19:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rawdata',
            old_name='Reinforces_Type_ID',
            new_name='Reinforce_Type_ID',
        ),
    ]

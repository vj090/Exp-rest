# Generated by Django 3.2.7 on 2021-09-21 08:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('expense', '0009_alter_expensemonth_income'),
    ]

    operations = [
        migrations.RenameField(
            model_name='expense',
            old_name='spent_date',
            new_name='date',
        ),
    ]

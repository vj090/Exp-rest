# Generated by Django 3.2.7 on 2021-09-20 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expense', '0005_alter_expense_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expensemonth',
            name='income',
            field=models.DecimalField(decimal_places=5, max_digits=15),
        ),
        migrations.AlterField(
            model_name='expensemonth',
            name='limit',
            field=models.DecimalField(decimal_places=5, max_digits=15),
        ),
    ]

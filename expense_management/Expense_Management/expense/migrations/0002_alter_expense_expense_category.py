# Generated by Django 3.2.7 on 2021-09-17 12:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('expense', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='expense_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_categories', to='expense.category'),
        ),
    ]

# Generated by Django 4.1.13 on 2024-05-28 11:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('food_app', '0002_timerange'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timerange',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food_app.customer'),
        ),
    ]

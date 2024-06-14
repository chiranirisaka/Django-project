# Generated by Django 5.0.6 on 2024-06-12 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('vehicle_type', models.CharField(max_length=50)),
                ('max_persons', models.IntegerField()),
                ('fuel_efficiency', models.FloatField()),
                ('price_per_km', models.DecimalField(decimal_places=2, max_digits=10)),
                ('availability', models.BooleanField(default=True)),
                ('image', models.ImageField(upload_to='vehicles/')),
            ],
        ),
    ]

# Generated by Django 5.1.2 on 2024-11-12 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebApp', '0002_signup'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PQuantity', models.IntegerField(blank=True, null=True)),
                ('PPrice', models.IntegerField(blank=True, null=True)),
                ('PName', models.CharField(blank=True, max_length=200, null=True)),
                ('Total', models.IntegerField(blank=True, null=True)),
                ('UName', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]

# Generated by Django 5.1.2 on 2024-10-14 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CategoryName', models.CharField(blank=True, max_length=100, null=True)),
                ('CategoryImage', models.ImageField(blank=True, null=True, upload_to='Categories')),
                ('CategoryDesc', models.TextField(blank=True, max_length=600, null=True)),
            ],
        ),
    ]

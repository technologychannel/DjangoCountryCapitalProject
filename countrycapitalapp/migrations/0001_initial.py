# Generated by Django 5.1.4 on 2025-02-05 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('capital', models.CharField(max_length=150)),
                ('population', models.IntegerField()),
                ('official_language', models.CharField(max_length=50)),
                ('currency', models.CharField(max_length=50)),
            ],
        ),
    ]

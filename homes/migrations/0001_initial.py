# Generated by Django 4.1.7 on 2023-04-07 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SignupUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=35, unique=True)),
                ('email', models.CharField(max_length=60)),
                ('phonenumber', models.CharField(max_length=10)),
                ('Address', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('reenterpassword', models.CharField(max_length=20)),
            ],
        ),
    ]

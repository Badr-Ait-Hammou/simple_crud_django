# Generated by Django 4.1.7 on 2023-04-03 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=70)),
                ('prenom', models.CharField(max_length=80)),
                ('type', models.CharField(max_length=80)),
                ('date', models.DateTimeField(max_length=100)),
            ],
        ),
    ]
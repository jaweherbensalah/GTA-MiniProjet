# Generated by Django 3.2.5 on 2021-07-19 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Formation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=200)),
                ('logo', models.CharField(max_length=300)),
                ('etat', models.BooleanField()),
                ('categorie', models.CharField(max_length=200)),
                ('prix', models.FloatField()),
                ('description', models.TextField()),
            ],
        ),
    ]
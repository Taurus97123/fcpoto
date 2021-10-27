# Generated by Django 3.2.5 on 2021-10-05 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Partenaire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entreprise', models.CharField(max_length=30)),
                ('description', models.TextField(max_length=200)),
                ('logo_entreprise', models.ImageField(blank=True, upload_to='club/images/')),
            ],
        ),
    ]

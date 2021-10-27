# Generated by Django 3.2.5 on 2021-09-28 09:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0006_auto_20210928_1000'),
    ]

    operations = [
        migrations.CreateModel(
            name='Saisons',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('saison', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='adversaire',
            name='saison',
            field=models.ForeignKey(default='0', on_delete=django.db.models.deletion.CASCADE, to='club.saisons'),
        ),
        migrations.AddField(
            model_name='match',
            name='saison',
            field=models.ForeignKey(default='0', on_delete=django.db.models.deletion.CASCADE, to='club.saisons'),
        ),
    ]

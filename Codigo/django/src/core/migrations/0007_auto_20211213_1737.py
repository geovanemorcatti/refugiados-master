# Generated by Django 3.2.9 on 2021-12-13 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_refugiado_ficha_social'),
    ]

    operations = [
        migrations.AddField(
            model_name='refugiado',
            name='celular',
            field=models.CharField(blank=True, default='', max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='refugiado',
            name='email',
            field=models.CharField(blank=True, default='', max_length=120, null=True),
        ),
    ]
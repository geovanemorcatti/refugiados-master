# Generated by Django 3.2 on 2021-11-10 21:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20211110_1738'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solicitacao',
            name='area',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.areaatendimento'),
            preserve_default=False,
        ),
    ]

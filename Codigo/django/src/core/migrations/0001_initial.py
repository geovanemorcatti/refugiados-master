# Generated by Django 3.2 on 2021-09-20 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Refugiado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=120)),
                ('sexo', models.CharField(choices=[('masc', 'Masculino'), ('fem', 'Feminino'), ('nb', 'Não-binário'), ('outro', 'Outro')], max_length=20)),
                ('idade', models.IntegerField()),
                ('nacionalidade', models.CharField(max_length=120)),
                ('formacao', models.CharField(blank=True, default='', max_length=120, null=True)),
                ('profissao', models.CharField(blank=True, default='', max_length=120, null=True)),
                ('lingua', models.CharField(blank=True, default='', max_length=120, null=True)),
                ('pais', models.CharField(blank=True, default='', max_length=120, null=True)),
                ('cidade', models.CharField(blank=True, default='', max_length=120, null=True)),
                ('primeiro_destino', models.CharField(blank=True, default='', max_length=120, null=True)),
                ('motivo_ida_brasil', models.TextField()),
                ('como_conheceu_projeto', models.TextField()),
                ('servicos_que_procura', models.TextField()),
            ],
        ),
    ]
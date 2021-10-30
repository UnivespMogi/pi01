# Generated by Django 3.2.8 on 2021-10-30 00:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nm_categoria', models.CharField(max_length=150, verbose_name='Nome da Categoria')),
                ('tp_categoria', models.CharField(choices=[('P', 'Produto'), ('S', 'Serviço')], max_length=1, verbose_name='Tipo de Categoria')),
            ],
        ),
    ]

# Generated by Django 3.2.8 on 2021-10-31 19:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('anuncios', '0010_merge_0008_auto_20211031_1114_0009_auto_20211031_1225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='nm_icone',
            field=models.CharField(help_text='Opções no site https://fontawesome.com.', max_length=30, verbose_name='Nome do Ícone'),
        ),
        migrations.AlterField(
            model_name='produto',
            name='categoria',
            field=models.ForeignKey(limit_choices_to={'tp_categoria': 'P'}, on_delete=django.db.models.deletion.CASCADE, related_name='fk_produto_categoria1', to='anuncios.categoria'),
        ),
        migrations.AlterField(
            model_name='servico',
            name='categoria',
            field=models.ForeignKey(limit_choices_to={'tp_categoria': 'S'}, on_delete=django.db.models.deletion.CASCADE, related_name='fk_servico_categoria1', to='anuncios.categoria'),
        ),
    ]

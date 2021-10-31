# Generated by Django 3.2.8 on 2021-10-31 00:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('anuncios', '0005_condominio_contato'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contato',
            name='condominios',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fk_contato_condominio1', to='anuncios.condominio'),
        ),
        migrations.CreateModel(
            name='Residencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nm_bloco', models.CharField(help_text='Nome do prédio. Ex.: Torre 1, Bloco B, Bloco Camélia.', max_length=45, verbose_name='Nome do Bloco')),
                ('nr_residencia', models.IntegerField(choices=[('Telefone', 'Telefone'), ('WhatsApp', 'WhatsApp'), ('Telegram', 'Telegram'), ('E-Mail', 'E-Mail')], verbose_name='Número')),
                ('condominios', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fk_residencia_condominio1', to='anuncios.condominio')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fk_residencia_user1', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

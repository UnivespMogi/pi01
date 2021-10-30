# Generated by Django 3.2.8 on 2021-10-30 01:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('anuncios', '0002_produto'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='usuario',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='fk_produto_user1', to='auth.user'),
            preserve_default=False,
        ),
    ]

# Generated by Django 4.1.1 on 2022-09-14 23:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('contatos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contato',
            name='data_cadastro',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='contato',
            name='telefone',
            field=models.CharField(max_length=30),
        ),
    ]
# Generated by Django 5.0.6 on 2024-05-17 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='registro_movimentacao',
            name='closed',
            field=models.BooleanField(default=True, null=True),
        ),
    ]
# Generated by Django 4.2.5 on 2023-11-05 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadcli', '0005_alter_cliente_email_cliente_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='tel_cliente',
            field=models.CharField(max_length=2),
        ),
    ]
# Generated by Django 2.2 on 2019-06-03 22:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderitem',
            old_name='regular',
            new_name='regularPizza',
        ),
    ]

# Generated by Django 3.0 on 2020-03-14 18:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testpro', '0036_auto_20200314_1709'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='users',
            new_name='user',
        ),
    ]

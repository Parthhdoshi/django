# Generated by Django 3.0 on 2020-03-19 13:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testpro', '0046_remove_places_date_create'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='place',
        ),
        migrations.AddField(
            model_name='order',
            name='place',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='testpro.Places'),
        ),
    ]

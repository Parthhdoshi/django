# Generated by Django 3.0 on 2020-05-04 19:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('testpro', '0052_auto_20200502_1615'),
    ]

    operations = [
        migrations.AddField(
            model_name='advertise',
            name='users',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

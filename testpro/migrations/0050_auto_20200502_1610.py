# Generated by Django 3.0 on 2020-05-02 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testpro', '0049_auto_20200321_0209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='profile_pic',
            field=models.ImageField(blank=True, default='default.jpg', upload_to=''),
        ),
    ]

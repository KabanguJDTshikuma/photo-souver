# Generated by Django 2.2.1 on 2019-05-24 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0004_auto_20190524_1735'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portrait',
            name='portrait',
            field=models.ImageField(upload_to='portrait/'),
        ),
        migrations.AlterField(
            model_name='portrait_detail',
            name='details',
            field=models.ImageField(upload_to='portrait/'),
        ),
    ]

# Generated by Django 2.2.3 on 2019-07-10 07:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0010_portrait_portrait_detail'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wedding',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weddding', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.AlterField(
            model_name='lifestyle',
            name='lifestyle',
            field=models.ImageField(upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='lifestyle_detail',
            name='lifestyle_detail',
            field=models.ImageField(upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='portrait',
            name='portrait',
            field=models.ImageField(upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='portrait_detail',
            name='portrait_detail',
            field=models.ImageField(upload_to='images/'),
        ),
        migrations.CreateModel(
            name='Wedding_detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wedding_detail', models.ImageField(upload_to='images/')),
                ('wedding_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='photo.Wedding')),
            ],
        ),
    ]
# Generated by Django 5.0.7 on 2024-07-30 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'verbose_name_plural': 'Новости'},
        ),
        migrations.AddField(
            model_name='news',
            name='image',
            field=models.ImageField(default=11, upload_to='news', verbose_name='Фото'),
            preserve_default=False,
        ),
    ]

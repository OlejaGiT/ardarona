# Generated by Django 3.2.6 on 2021-11-06 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Изображения', max_length=255)),
                ('img_one', models.ImageField(upload_to='', verbose_name='Первое изображение')),
                ('img_two', models.ImageField(upload_to='', verbose_name='Второе изображение')),
                ('img_thre', models.ImageField(upload_to='', verbose_name='Третье изображение')),
                ('img_four', models.ImageField(upload_to='', verbose_name='Четвертое изображение')),
                ('img_five', models.ImageField(upload_to='', verbose_name='Пятое изображение')),
                ('img_six', models.ImageField(upload_to='', verbose_name='Шестое изображение')),
                ('img_seven', models.ImageField(upload_to='', verbose_name='Седьмое изображение')),
            ],
            options={
                'verbose_name': 'Изображения',
                'verbose_name_plural': 'Изображения',
            },
        ),
    ]

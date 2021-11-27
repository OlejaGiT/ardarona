from django.db import models


class About(models.Model):
    title = models.CharField(max_length=255, default='Изображения')
    img_one = models.ImageField(verbose_name='Первое изображение')
    img_two = models.ImageField(verbose_name='Второе изображение')
    img_thre = models.ImageField(verbose_name='Третье изображение')
    img_four = models.ImageField(verbose_name='Четвертое изображение')
    img_five = models.ImageField(verbose_name='Пятое изображение')
    img_six = models.ImageField(verbose_name='Шестое изображение')
    img_seven = models.ImageField(verbose_name='Седьмое изображение')

    def __str__(self):
        return self.title



    class Meta:
        verbose_name = 'Изображения'
        verbose_name_plural = 'Изображения'



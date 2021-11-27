from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
import datetime



class DogInfo(models.Model):
    name = models.CharField('Имя', max_length=250)
    color = models.ForeignKey('DogColor', on_delete=models.PROTECT, null=True, blank=True, related_name="color", verbose_name='Цвет')
    weight = models.PositiveSmallIntegerField('Вес', default=0)
    height = models.PositiveSmallIntegerField('Рост', default=0)
    number_of_awards = models.PositiveSmallIntegerField('Число наград', default=0)
    age = models.DateField(verbose_name="age", default=0, blank=True)
    info = models.TextField('Информация', blank=True)
    img = models.ImageField(blank=True) 
    position = models.ForeignKey('DogPosition', on_delete=models.PROTECT, null=True, blank=True, related_name="position", verbose_name='Позиция')
    gender = models.ForeignKey('DogGender', on_delete=models.PROTECT, null=True, blank=True, related_name="gender", verbose_name='Пол')
    status = models.ForeignKey('DogStatus', on_delete=models.PROTECT, null=True, blank=True, related_name="status", verbose_name='Статус')
    pos = models.BooleanField(default=False, verbose_name='Показывать?')
    mother = models.ForeignKey('self', on_delete=models.PROTECT, null=True, blank=True, related_name='mother_info', verbose_name='Мама',
    related_query_name="mot"
    )
    father = models.ForeignKey('self', on_delete=models.PROTECT, null=True, blank=True, related_name='father_info', verbose_name='Папа',
    related_query_name="fat"
    ) 
    display_puppy = models.ForeignKey('DogDisplayPuppy',on_delete=models.PROTECT, null=True, blank=True, related_name="display", verbose_name='Отображать в щенках?')
    display_galery = models.ForeignKey('DogDisplayGalery',on_delete=models.PROTECT, null=True, blank=True, related_name="display", verbose_name='Отображать в галерее?')
   

    def __str__(self):
        return self.name


    

    class Meta:
        verbose_name = 'Собака'
        verbose_name_plural = 'Собаки'
        ordering = ['-id']



class PostImage(models.Model):
    post = models.ForeignKey(DogInfo, default=None, on_delete=models.CASCADE)
    imgs = models.ImageField(upload_to = 'images/')


    def __str__(self):
            return self.post.name


    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'


class DogColor(models.Model):
    dog_color = models.CharField('Цвет', max_length=55)

    def __str__(self):
        return self.dog_color

    class Meta:
        verbose_name = 'Цвет'
        verbose_name_plural = 'Цвета'


class DogGender(models.Model):
    dog_gender = models.CharField('Пол', max_length=55)

    def __str__(self):
        return self.dog_gender

    class Meta:
        verbose_name = 'Пол'
        verbose_name_plural = 'Пол'


class DogPosition(models.Model):
    dog_position = models.CharField('Позиция', max_length=55)

    def __str__(self):
        return self.dog_position

    class Meta:
        verbose_name = 'Позиция'
        verbose_name_plural = 'Позиции'


class DogStatus(models.Model):
    dog_status = models.CharField('Статус', max_length=55)

    def __str__(self):
        return self.dog_status

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'


class DogDisplayPuppy(models.Model):
    dog_display_puppy = models.CharField('Отображать в щенках?', max_length=55)

    def __str__(self):
        return self.dog_display_puppy

    class Meta:
        verbose_name = 'Отображать в щенках?'
        verbose_name_plural = 'Отображать в щенках?'


class DogDisplayGalery(models.Model):
    dog_display_galery = models.CharField('Отображать в родителях?', max_length=55)

    def __str__(self):
        return self.dog_display_galery

    class Meta:
        verbose_name = 'Отображать в родителях?'
        verbose_name_plural = 'Отображать в родителях?'


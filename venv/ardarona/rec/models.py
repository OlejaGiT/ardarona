from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Title(models.Model):
    title = models.TextField(verbose_name='Заголовок страницы')
     
    class Meta:
        verbose_name = 'Заголовок'
        verbose_name_plural = 'Заголовки'


class RecomendInfo(models.Model):
    text = models.TextField('Рекомендации')

    class Meta:
        verbose_name = 'Рекомендации'
        verbose_name_plural = 'Рекомендации'


class Accordion(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название аккордиона')
    accordion_img = models.ImageField(verbose_name='Изображение аккордиона')


    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'Аккордион'
        verbose_name_plural = 'Аккордионы'


class AccordionText(models.Model):
    accordion_title = models.CharField(max_length=255, verbose_name='Название раздела аккордиона')
    accordion = models.ForeignKey(Accordion, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Название аккордиона')
    accordion_text = models.TextField(verbose_name='Информация аккордиона')
    

    def __str__(self):
        return self.accordion.title


    class Meta:
        verbose_name = 'Информацию аккордиона'
        verbose_name_plural = 'Информация аккордиона'


class RecomendLogo(models.Model):
    logo_title = models.TextField(verbose_name='Заголовок')
    logo_img = models.ImageField(verbose_name='Логотип')
    logo_text = models.TextField(verbose_name='Информация')


    class Meta:
        verbose_name = 'Логотип'
        verbose_name_plural = 'Логотипы'



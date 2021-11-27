from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя')
    prof = models.CharField(max_length=255)
    img = models.ImageField(verbose_name="фотография")


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Команда'
        verbose_name_plural = 'Команда'


class PrilTeam(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    link = models.CharField(max_length=255, verbose_name='Ссылка')
    icon = models.CharField(max_length=255, verbose_name='Иконка')


    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'Приложение'
        verbose_name_plural = 'Приложения'


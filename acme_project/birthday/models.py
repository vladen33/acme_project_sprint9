from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from .validators import real_age


class Birthday(models.Model):
    first_name = models.CharField(verbose_name='Имя', max_length=20)
    last_name = models.CharField(verbose_name='Фамилия', max_length=20, blank=True, help_text='Необязательное поле')
    birthday = models.DateField(verbose_name='Дата рождения', validators=[real_age,])
    image = models.ImageField(
        verbose_name='Фото',
        upload_to='birthdays_images',
        blank=True,
    )

    class Meta:
        constraints = (
            models.UniqueConstraint(
                fields=('first_name', 'last_name', 'birthday'),
                name='Unique person constraint',
            ),
        )

#
# class Contest(models.Model):
#     title = models.CharField(verbose_name='Название', max_length=20)
#     description = models.TextField(verbose_name='Описание')
#     price = models.IntegerField(
#         verbose_name='Цена',
#         validators=[MinValueValidator(10), MaxValueValidator(100)],
#         help_text='Рекомендованная розничная цена'
#     )
#
#     comment = models.TextField(verbose_name='Комментарий', blank=True)

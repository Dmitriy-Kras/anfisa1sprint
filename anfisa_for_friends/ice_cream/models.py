from core.models import PublishedModel
from django.db import models


class Wrapper(PublishedModel):
    title = models.CharField(
        max_length=256,
        verbose_name='название',
        help_text='Уникальное название обёртки, не более 256 символов'
    )

    class Meta:
        verbose_name = 'объект обёртка'
        verbose_name_plural = 'Обёртки'


class Topping(PublishedModel):
    slug = models.SlugField(
        max_length=64,
        unique=True,
        verbose_name='слаг'
    )

    class Meta:
        verbose_name = 'топпинг'
        verbose_name_plural = 'Топпинги'


class IceCream(PublishedModel):
    description = models.TextField(verbose_name='описание')
    is_on_main = models.BooleanField(
        default=False,
        verbose_name='на главной',
        help_text='на главную'
    )
    category = models.ForeignKey(
        'Category',
        on_delete=models.CASCADE,
        related_name='ice_creams',
        verbose_name='категория'
    )
    toppings = models.ManyToManyField(Topping, verbose_name='топпинги')
    wrapper = models.OneToOneField(
        Wrapper,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='ice_cream',
        verbose_name='обертка'
    )
    output_order = models.PositiveSmallIntegerField(
        default=100,
        verbose_name='Порядок отображения',
        help_text='Чем меньше цифра тем выше отображение на сайте '
    )
    price = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        verbose_name='цена'
    )

    class Meta:
        ordering = ('output_order', 'title')
        verbose_name = 'мороженое'
        verbose_name_plural = 'Мороженое'


class Category(PublishedModel):
    slug = models.SlugField(
        max_length=64,
        unique=True,
        verbose_name='слаг'
    )
    output_order = models.PositiveSmallIntegerField(
        default=100,
        verbose_name='Порядок отображения',
        help_text='Чем меньше цифра тем выше отображение на сайте '
    )

    class Meta:
        verbose_name = 'категорию'
        verbose_name_plural = 'Категории'

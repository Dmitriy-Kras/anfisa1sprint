from core.models import PublishedModel
from django.db import models


class Wrapper(PublishedModel):
    title = models.CharField(max_length=256)


class Topping(PublishedModel):
    title = models.CharField(max_length=256)
    slug = models.SlugField(max_length=64, unique=True)


class IceCream(PublishedModel):
    title = models.CharField(max_length=256)
    description = models.TextField()
    is_on_main = models.BooleanField(default=False)
    category = models.ForeignKey(
        'Category',
        on_delete=models.CASCADE,
        related_name='ice_creams'
    )
    toppings = models.ManyToManyField(Topping)
    wrapper = models.OneToOneField(
        Wrapper,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='ice_cream'
    )


class Category(PublishedModel):
    title = models.CharField(max_length=256)
    slug = models.SlugField(max_length=64, unique=True)
    output_order = models.PositiveSmallIntegerField(default=100)

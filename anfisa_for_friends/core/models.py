from django.db import models


class PublishedModel(models.Model):
    """Абстрактная модель. Добвляет название и флаг is_published."""
    title = models.CharField(
        max_length=256,
        verbose_name='название',
        help_text='Обязательное поле'
    )
    is_published = models.BooleanField(
        default=True,
        verbose_name='опубликовано',
        help_text='Снимите галочку, чтобы скрыть публикацию'
    )

    class Meta:
        abstract = True

    def __str__(self):
        return self.title

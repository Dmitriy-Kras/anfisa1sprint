from django.contrib import admin
from django.contrib.auth.models import Group
from django.urls import reverse
from django.utils.html import format_html

from .models import Category, IceCream, Topping, Wrapper

admin.site.empty_value_display = 'Не задано'
admin.site.site_header = 'Сайт администратора "Анфиса для друзей"'
admin.site.site_title = 'Анфиса для друзей - админка'
admin.site.index_title = 'Сайт администратора "Анфиса для друзей"'
admin.site.unregister(Group)


class IceCreamInline(admin.StackedInline):
    model = IceCream
    extra = 0


@admin.register(IceCream)
class IceCreamAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'is_published',
        'is_on_main',
        'category',
        'wrapper',
        'toppings_display'
    )
    list_editable = (
        'is_published',
        'is_on_main',
        'category'
    )
    list_per_page = 5
    fields = (
        'title',
        ('is_published', 'is_on_main',),
        'description',
        ('category', 'wrapper'),
        'toppings'
    )
    search_fields = ('title',)
    list_filter = ('category',)
    list_display_links = ('title',)
    filter_horizontal = ('toppings',)

    def toppings_display(self, obj):
        display_text = ", ".join([
            "<a href={}>{}</a>".format(
                    reverse('admin:{}_{}_change'.format(
                                tp._meta.app_label,
                                tp._meta.model_name),
                            args=(tp.pk,)),
                    ' '.join(str(tp).split()[:2]))
            for tp in obj.toppings.all()
        ])
        return format_html(display_text)

    toppings_display.short_description = 'Топпинги'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    inlines = (
        IceCreamInline,
    )
    list_display = (
        'title',
        'count_ice_cream'
    )

    def count_ice_cream(self, obj):
        count = obj.ice_creams.count()
        return f'{count} наименов. мороженого'

    count_ice_cream.short_description = 'Кол-во в категории'


admin.site.register(Topping)
admin.site.register(Wrapper)

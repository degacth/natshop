# coding: utf-8

import init
import fake
from section.models import Section, Article
from catalog.models import Category

Section.objects.all().exclude(id__in=Category.objs.all()).delete()


# Main menu
menu = (
    ('Контакты', 'phone'),
    ('Новости', 'newspaper-o'),
    ('Как купить', 'question'),
    ('Корзина', 'shopping-cart'),
)

for section in menu:
    section = Section.objects.create(**{
        'title': section[0],
        'name': section[1],
        'grouping': 'main_menu',
    })

Section.objects.create(**{
    'title': 'Каталог',
    'name': 'catalog',
})

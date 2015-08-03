# coding: utf-8

import init
import fake
from section.models import Section, Article

Section.objects.all().delete()

# Main menu
menu = (
    ('Контакты', 'contacts'),
    ('Новости', 'news'),
    ('Как купить', 'howbay'),
)

for section in menu:
    section = Section.objects.create(**{
        'title': section[0],
        'name': section[1],
        'grouping': 'main_menu',
    })

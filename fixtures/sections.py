# coding: utf-8

import init
import fake
from section.models import Section, Article
from catalog.models import Category

Section.objects.all().exclude(id__in=Category.objs.all()).delete()


# Main menu
menu = (
    ('Контакты', 'phone'),
    ('Новости', 'newspaper-o', 'blog'),
    ('Как купить', 'question'),
    ('Корзина', 'shopping-cart'),
)

for section in menu:
    section = Section.objects.create(**{
        'title': section[0],
        'name': section[1],
        'grouping': 'main_menu',
        'action': section[2] if len(section) > 2 else ""
    })

phone = Section.objects.get(name="phone")

for point in range(-1, 2):
    Article.objects.create(**{
        'title': 'Статься контактов',
        'parent': phone,
        'other_info': "%s" % [coord + point * 0.1 for coord in [57.813788, 28.348867]],
        'short': fake.lorem,
        'description': fake.lorem * 2
    })

Section.objects.create(**{
    'title': 'Каталог',
    'name': 'catalog',
})

news_sec = Section.objects.get(name='newspaper-o')
news = []

for i in range(0, 40):
    article = Article.objects.create(**{
        'title': 'Великая новость #%s' % i,
        'parent': news_sec,
        'short': fake.lorem * 2,
        'description': fake.lorem * 4,
    })

    fake.add_attachment(article)

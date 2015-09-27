# coding: utf-8

import init
from config.models import Config

Config.objects.create(**{
    'title': 'Имя сайта',
    'name': 'site_name',
    'value': 'NatShop',
})

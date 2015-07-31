# coding: utf-8

import init
from config.models import Config

Config.objects.all().delete()

for name in ['title', 'description', 'keywords']:
    tp = "seo_%s" % name
    conf = Config(title=tp, name=tp, value="Hello, World")
    conf.save()

getback_address = Config(title="Адрес возврата", name='getback_address',
                         value="Адрес для возврата: 180004, г. Псков, ул. Железнодорожная, 60, для ООО «Псков Полимер»")
getback_address.save()

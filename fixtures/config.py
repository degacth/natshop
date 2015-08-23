# coding: utf-8

import init
from config.models import Config

Config.objects.all().delete()

for name in ['title', 'description', 'keywords']:
    tp = "seo_%s" % name
    conf = Config(title=tp, name=tp, value="Hello, World")
    conf.save()

Config(title="Tелефоны", name="phones", value="+7 911 921 83 88,+7 911 834 83 71", type="array").save()
Config(title="Email адреса", name="emails", value="degacth@yandex.ru,hello@world.ru", type="array").save()
Config(title="Email адреса admins", name="admin_emails", value="degacth@yandex.ru", type="array").save()

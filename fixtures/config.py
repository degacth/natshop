# coding: utf-8

import init
from config.models import Config

Config.objects.all().delete()

for name in ['title', 'description', 'keywords']:
    tp = "seo_%s" % name
    conf = Config(title=tp, name=tp, value="Hello, World")
    conf.save()

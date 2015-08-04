from . import globals
from config.models import init_config
from section.models import Section

class Global(object):
    def process_request(self, request):
        globals.request = request
        globals.user = getattr(request, 'user', None)
        globals.config = init_config()
        globals.catalog = Section.objs.get(name='catalog')

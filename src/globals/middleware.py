from . import globals
from config.models import init_config

class Global(object):
    def process_request(self, request):
        globals.request = request
        globals.user = getattr(request, 'user', None)
        globals.config = init_config()

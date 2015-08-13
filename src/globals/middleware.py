from . import globals
from config.models import init_config
from section.models import Section
from customer.models import Customer


class Global(object):
    def process_request(self, request):
        globals.request = request
        customet_id = request.session.get(Customer.SESSION_KEY)
        setattr(request, 'customer', Customer.objects.get(id=customet_id) if customet_id else None)
        globals.config = init_config()
        globals.catalog = Section.objs.get(name='catalog')

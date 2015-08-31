from . import globals
from config.models import init_config
from section.models import Section
from customer.models import Customer


class Global(object):
    def process_request(self, request):
        globals.request = request
        customet_id = request.session.get(Customer.SESSION_KEY, False)
        if customet_id:
            try:
                customer = Customer.objects.get(id=customet_id)
            except Customer.DoesNotExist:
                customer = None
                del request.session[Customer.SESSION_KEY]

        else: customer = None

        setattr(request, 'customer', customer)
        globals.config = init_config()
        try:
            globals.catalog = Section.objs.get(name='catalog')
        except Section.DoesNotExist:
            globals.catalog = None

# coding: utf-8
from django.views import generic
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string


def send(subject, message, to):
    html = render_to_string('emails/base_mail.html', {
        'subject': subject,
        'message': message,
    })

    send_mail(subject, None, settings.EMAIL_HOST_USER, to, fail_silently=settings.DEBUG, html_message=html)


class ShowEmail(generic.TemplateView):
    template_name = 'emails/base_mail.html'

    def get_context_data(self, **kwargs):
        return {
            'subject': 'Проверка представления письма',
            'message': '''
                Lorem ipsum dolor sit amet, consectetur adipisicing elit. Alias animi architecto autem,
                cum dicta et fuga, ipsam mollitia numquam quidem suscipit,
                ullam vitae voluptates.
                Corporis explicabo inventore perferendis quibusdam recusandae?
            '''
        }

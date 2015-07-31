# coding: utf-8
from django.db import models
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.template.loader import render_to_string
from django.utils.translation import ugettext as _
from django.utils import timezone
from mailer.views import send
from globals import globals


class Feedback(models.Model):
    class Meta:
        verbose_name = _('Feedback')
        verbose_name_plural = _('Feedbacks')

    username = models.CharField(_('username'), max_length=255)
    email = models.EmailField(_('email'), max_length=255)
    message = models.TextField(_('message_text'))
    phone = models.CharField(_('phone_number'), max_length=255)
    created = models.DateTimeField(_('created'), default=timezone.now)

    adminname = models.CharField(_('adminname'), max_length=255, blank=True)
    admin_message = models.TextField(_('admin_message'), blank=True)
    answer_date = models.DateTimeField(_('answer_date'), blank=True, null=True)

    is_new = models.BooleanField(_('is_new'), default=True)
    is_notified = models.BooleanField(_('is_notified'), default=False)
    status = models.BooleanField(_('status'), default=False)

    def __unicode__(self):
        return self.username


@receiver(post_save, sender=Feedback)
def check_post_feedback(instance, sender, created, **kwargs):
    html = render_to_string('feedback/feedback_fields.html', {
        'feedback': instance,
    })

    if created:
        send(_('Thanks for question'), html, [instance.email])
        send(_('Received a complaint from') + ' %s' % instance.username, html, globals.config['admin_emails'])


@receiver(pre_save, sender=Feedback)
def check_pre_feedback(instance, **kwargs):
    if instance.id and instance.admin_message and not instance.is_notified:
        instance.is_notified = True
        instance.answer_date = timezone.now()
        send(_('Answer on your question from site ') + globals.request.get_host(),
             render_to_string('feedback/feedback_fields.html', {
                 'feedback': instance,
                 'answer': True,
             }), [instance.email])

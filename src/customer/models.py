from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.utils import six, timezone
from django.utils.translation import ugettext as _


class Customer(AbstractBaseUser):
    name = models.CharField(_('name'), max_length=30, blank=True)
    email = models.EmailField(_('email'), blank=True)
    is_active = models.BooleanField(_('active'), default=True,
                                    help_text=_('Designates whether this user should be treated as '
                                                'active. Unselect this instead of deleting accounts.'))
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name = _('customer')
        verbose_name_plural = _('customer')

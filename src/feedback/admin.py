from django.contrib import admin
from django.utils.translation import ugettext as _
import models

@admin.register(models.Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    search_fields = ('message', 'username')
    list_filter = ['created', 'is_new']

    fieldsets = (
        (None, {
            'fields': ('username', 'email', 'phone', 'message', 'created', 'status', 'is_new', 'is_notified'),
        }),

        (_('Answer_form'), {
            'fields': ('adminname', 'admin_message'),
            'classes': ('collapse',)
        })
    )

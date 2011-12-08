"""Signal handler if someone fails to login."""
from django.conf import settings
from django.contrib.sites.models import Site
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.template.loader import render_to_string

from BruteBuster.models import FailedAttempt


def send_notification(sender, instance, signal, *args, **kwargs):
    ctx_dict = {
        'object': instance,
        'site': Site.objects.get_current()
    }
    subject = render_to_string(
            'brutebustersignals/notification_subject.txt',
            ctx_dict)
    # Email subject *must not* contain newlines
    subject = ''.join(subject.splitlines())

    message = render_to_string('brutebustersignals/notification.txt', ctx_dict)
    to = [item[1] for item in settings.MANAGERS]
    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, to)

post_save.connect(send_notification, sender=FailedAttempt)

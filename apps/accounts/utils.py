from django.core.mail import send_mail
from django.template.loader import render_to_string


def send_activation_email(request, activation):

    subject = render_to_string('accounts/mail/activation_subject.txt', {
        'activation': activation, 'site': request.site
    })
    subject = ''.join(subject.splitlines())
    body = render_to_string('accounts/mail/activation_body.txt', {
        'activation': activation, 'site': request.site,
    })
    send_mail(subject, message, settings.DEFAULT_EMAIL_FROM, [activation.user.email])

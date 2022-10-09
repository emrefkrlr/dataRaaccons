import smtplib as smtp, ssl
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import EmailMultiAlternatives

templates = {
    'verify_email': "email/verify_email.html",
}
def send_mail(subject, from_address, to_address, template, confirm_code):

    subject, from_email, to = subject, from_address, to_address
    text_content = 'This is an important message.'
    html_content = render_to_string(template, {'confirme_code': confirm_code})
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()
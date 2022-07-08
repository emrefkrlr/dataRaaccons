import smtplib as smtp
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import EmailMultiAlternatives

templates = {
    'verify_email': "email/verify_email.html",
}
def send_mail(mail_address, template, confirm_code):

    html_content = render_to_string(template, {'confirme_code': confirm_code})
    content = strip_tags(html_content)
    connection = smtp.SMTP_SSL(settings.EMAIL_HOST, settings.EMAIL_PORT)
    conn = connection.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)


    email = EmailMultiAlternatives(
        subject="Verify Email to Account | Raccoon Analytic", 
        body=content, 
        from_email=settings.EMAIL_HOST_USER, 
        to=mail_address, 
        connection=conn)

    email.attach_alternative(content, "text/html")
    result = email.send()

    if result:
        return True
    else:
        return False




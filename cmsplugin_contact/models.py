from django.db import models
from django.utils.translation import ugettext_lazy as _
from cms.models import CMSPlugin

# Feel free to extend this class instead of Contact.
class BaseContact(CMSPlugin):
    SPAM_PROTECTION_CHOICES = (
        (0, 'Honeypot'),
        (1, 'Akismet'),
        (2, 'ReCAPTCHA'),
    )
    
    THEME_CHOICES = (
        ('clean', 'Clean'),
        ('red', 'Red'),
        ('white', 'White'),
        ('blackglass', 'Black Glass'),
        ('custom', 'Custom'),
    )
    
    site_email = models.EmailField(_('Email recipient'))
    thanks = models.TextField(
        verbose_name=_("Thanks message"),
        help_text=_('Message displayed on successful submit'),
        default=_('Thank you for your message.'), max_length=200)

    spam_protection_method = models.SmallIntegerField(
        verbose_name=_('Spam protection method'),
        choices=SPAM_PROTECTION_CHOICES, default=0)
    
    akismet_api_key = models.CharField(max_length=255, blank=True)
    
    recaptcha_public_key = models.CharField(max_length=255, blank=True)
    recaptcha_private_key = models.CharField(max_length=255, blank=True)
    recaptcha_theme = models.CharField(max_length=20,
                                       choices=THEME_CHOICES,
                                       default='clean',
                                       verbose_name=_('ReCAPTCHA theme'))

    class Meta:
        abstract = True
    
    def __unicode__(self):
        return self.site_email

class Contact(BaseContact):
    pass

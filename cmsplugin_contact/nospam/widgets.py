from django import forms
from django.utils.translation import ugettext_lazy as _, get_language
from django.utils.safestring import mark_safe


# RECAPTCHA widgets
class RecaptchaResponse(forms.Widget):

    def render(self, *args, **kwargs):
        from recaptcha.client import captcha as recaptcha
        recaptcha_options = ("""<script type="text/javascript"> """
                             """var RecaptchaOptions = { theme: '%(theme)s', """
                                """lang: '%(language)s', """
                                """custom_theme_widget: '%(widget)s'}; """
                             """</script>\n"""%{
                    'theme': self.theme,
                    'language': get_language()[0:2],
                    'widget': ('recaptcha_widget' if self.theme == 'custom'
                               else '')})
        return mark_safe(recaptcha_options + 
                         recaptcha.displayhtml(self.public_key))


class RecaptchaChallenge(forms.Widget):
    is_hidden = True
    def render(self, *args, **kwargs):
        return ""
#        return mark_safe('')
    
    
    
# Honeypot widget -- most automated spam posters will check any checkbox
# assuming it's an "I accept terms and conditions" box
class HoneypotWidget(forms.CheckboxInput):
    is_hidden = True
    def render(self, *args, **kwargs):
        #here the first %s gets replaced by the translation of "Are you a robot?
        # the second one stays as %s
        wrapper_html = ('<div style="display: none;">'
                        '<label for="id_accept_terms">%s</label>%%s</div>' % 
                        (_('Are you a robot?')))
        return mark_safe(wrapper_html % 
                         (super(HoneypotWidget, self).render(*args, **kwargs)))

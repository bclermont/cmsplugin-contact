
from django.utils.deprecation import MiddlewareMixin


class ForceResponseMiddleware(MiddlewareMixin):
    def process_response(self, request, response):
        if getattr(request, 'django_cms_contact_redirect_to', None):
            return request.django_cms_contact_redirect_to
        return response

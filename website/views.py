from typing import Any, Dict
from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self):
        ctxt = super().get_context_data()
        ctxt['username'] = "Satoshi"
        return ctxt

class ContactView(TemplateView):
    template_name = 'contact.html'

class AboutView(TemplateView):
    template_name = 'about.html'

    def get_context_data(self):
        ctxt = super().get_context_data()
        ctxt['numServices'] = 123456789
        ctxt['skills'] = [
                'Python',
                'C++',
                'JavaScript',
                'Rust',
                ]
        return ctxt

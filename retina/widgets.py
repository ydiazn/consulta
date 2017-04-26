from django import forms
from django.conf import settings


class DateInput(forms.TextInput):
    class Media:
        css = {
            'all': ('%scss/datepicker.min.css' % settings.STATIC_URL,)
        }
        js = ('%sjs/bootstrap-datepicker.min.js' % settings.STATIC_URL,)


class ChosenInput(forms.Select):
    class Media:
        css = {
            'all': ('%scss/chosen.min.css' % settings.STATIC_URL,)
        }
        js = ('%sjs/chosen.jquery.min.js' % settings.STATIC_URL,)

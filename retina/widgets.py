from django import forms
from django.conf import settings


class DatePicker(forms.DateInput):
    class Media:
        css = {
            'all': ('%scss/bootstrap-datepicker.min.css' % settings.STATIC_URL,)
        }
        js = ('%sjs/bootstrap-datepicker.min.js' % settings.STATIC_URL,
              '%sjs/bootstrap-datepicker.es.min.js' % settings.STATIC_URL,)


class DateTimePicker(forms.DateTimeInput):
    class Media:
        css = {
            'all': ('%scss/jquery.datetimepicker.min.css' % settings.STATIC_URL,)
        }
        js = ('%sjs/jquery.datetimepicker.full.min.js' % settings.STATIC_URL,)


class ChosenInput(forms.Select):
    class Media:
        css = {
            'all': ('%scss/chosen.min.css' % settings.STATIC_URL,)
        }
        js = ('%sjs/chosen.jquery.min.js' % settings.STATIC_URL,)


class ChosenInputMultiple(forms.SelectMultiple):
    class Media:
        css = {
            'all': ('%scss/chosen.min.css' % settings.STATIC_URL,)
        }
        js = ('%sjs/chosen.jquery.min.js' % settings.STATIC_URL,)

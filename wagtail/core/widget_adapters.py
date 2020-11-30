"""
Register Telepath adapters for core Django form widgets, so that they can
have corresponding Javascript objects with the ability to render new instances
and extract field values.
"""

from django import forms
from wagtail.core.telepath import register, Adapter


class WidgetAdapter(Adapter):
    js_constructor = 'wagtail.widgets.Widget'

    def js_args(self, widget, context):
        return [
            widget.render('__NAME__', None, attrs={'id': '__ID__'}),
            widget.id_for_label('__ID__'),
        ]

    class Media:
        js = ['wagtailadmin/js/telepath/widgets.js']

register(WidgetAdapter(), forms.widgets.Input)
register(WidgetAdapter(), forms.Textarea)
register(WidgetAdapter(), forms.Select)


class RadioSelectAdapter(WidgetAdapter):
    js_constructor = 'wagtail.widgets.RadioSelect'

register(RadioSelectAdapter(), forms.RadioSelect)

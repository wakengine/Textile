from django import forms
from django.template.loader_tags import register


class FormReader:
    request = None

    def __init__(self, request):
        self.request = request

    def get_post_data(self, name):
        if name in self.request.POST:
            return self.request.POST[name]
        else:
            return None


@register.filter(name='is_textarea')
def is_textarea(field):
    return field.field.widget.__class__.__name__ == forms.Textarea().__class__.__name__


@register.filter(name='is_checkbox')
def is_textarea(field):
    return field.field.widget.__class__.__name__ == forms.CheckboxInput().__class__.__name__


class DataListWidget(forms.TextInput):
    def __init__(self, data_list, name, *args, **kwargs):
        super(DataListWidget, self).__init__(*args, **kwargs)
        self._name = name
        self._list = data_list
        self.attrs.update({'list': 'list_{}'.format(self._name)})

    def render(self, name, value, attrs=None):
        text_html = super(DataListWidget, self).render(name, value, attrs=attrs)
        data_list = '<datalist id="list_{}">'.format(self._name)
        for item in self._list:
            data_list += '<option value="{}">'.format(item)
        data_list += '</datalist>'

        return text_html + data_list

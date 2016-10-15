class FormData:
    label = ''
    input_type = ''
    name = ''
    required = True
    max_length = 0
    place_holder = ''
    help_text = ''
    options = []

    def __init__(self, label, name, required, input_type, max_length, place_holder, options):
        self.label = label
        self.name = name
        self.required = required
        self.input_type = input_type
        self.max_length = max_length
        self.place_holder = place_holder
        self.options = options

    def __str__(self):
        return self.name

    def get_label(self):
        if self.required:
            return '<span class="text-primary bg-info">{}</span>'.format(self.label)
        return '<span class="text-muted">{}</span>'.format(self.label)

    def get_required(self):
        if self.required:
            return 'required'
        return ''

    def get_placeholder(self):
        if self.place_holder:
            return 'placeholder={}'.format(self.place_holder)
        return ''

    def get_placeholder_content(self):
        return self.place_holder

    def get_max_length(self):
        if self.max_length > 0:
            if self.input_type == 'number':
                return 'max={} step=any'.format(self.max_length)
            else:
                return 'maxlength={}'.format(self.max_length)
        return ''


class FormReader:
    request = None

    def __init__(self, request):
        self.request = request

    def get_post_data(self, name):
        if name in self.request.POST:
            return self.request.POST[name]
        else:
            return None

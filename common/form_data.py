class FormData:
    label = ''
    name = ''
    required = ''
    input_type = ''
    max_length = ''
    place_holder = ''
    help_text = ''
    options = {}

    def __init__(self, label, name, required, input_type, max_length, place_holder, options):
        self.label = label
        self.name = name
        self.required = required
        self.input_type = input_type
        self.max_length = max_length
        self.place_holder = place_holder
        self.options = options

class Text:
    def __init__(self, text, section):
        self.text = text
        self.section = section

    def add_ref(self, ref):
        self.text.format('\\ref{' + self.section[ref].label + '}')

    def compile(self):
        return self.text

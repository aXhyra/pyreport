class Text:
    def __init__(self, text, section):
        self.text = text
        self.section = section

    def add_ref(self, ref):
        refs = ('\\ref"{"{}"}"'*len(ref)).format(*ref)
        self.text.format(*refs)

    def add_itemize(self, items):
        self.text.append('\n\\begin{itemize}')
        for item in items:
            self.text.append('\n\\item ' + item)
        self.text.append('\n\\end{itemize}')

    def add_enumerate(self, items):
        self.text.append('\n\\begin{enumerate}')
        for item in items:
            self.text.append('\n\\item ' + item)
        self.text.append('\n\\end{enumerate}')

    def compile(self):
        return self.text

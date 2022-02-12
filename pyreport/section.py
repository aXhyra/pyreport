from pyreport import PyReport, Image, Table, Text


class Section:

    def __init__(self, title, index=True, level=0):
        self.title = title
        self.label = '\\label{' + 'sub' * level + 'sec:' + title + '}'
        self.level = level
        self.images = {}
        self.index = index
        self.text_counter = 0
        self.static_content = [
            '\\' + 'sub' * self.level + 'section{' + self.title + '}' if self.index else '\\' + 'sub' * self.level + 'section*{' + self.title + '}',
            self.label,
        ]

        self.content = {}
        self.subsections = {
        }

    def add_subsection(self, title):
        self.subsections[title] = Section(title, level=self.level + 1)
        self.content[title] = self.subsections[title].content

    def add_image(self, image, caption, label):
        self.content[label] = Image(image, caption, label)

    def add_table(self, table, caption, label):
        self.content[label] = Table(table, caption, label)

    def add_text(self, text):
        self.content[f'text_{self.text_counter}'] = Text(text, self)

    def compile(self):
        compiled = ''
        for item in self.static_content:
            compiled += item + '\n'
        for item in self.content:
            compiled += item.compile() + '\n'


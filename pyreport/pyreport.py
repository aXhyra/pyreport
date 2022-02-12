from pyreport import Section


class PyReport:

    def __init__(self, author, date, title, doc_class):
        self.author = author
        self.date = date
        self.title = title
        self.doc_class = doc_class
        self.preamble = [
            f'%! Author: {self.author}',
            f'%! Date: {self.date}',
            '',
            '% Preamble',
            '\\documentclass{' + self.doc_class + '}',
            '',
            '% Packages',
            '\\usepackage[utf8]{inputenc}',
            '\\usepackage{import}',
            '\\usepackage{graphicx}',
            '\\usepackage{subfig}',
            '\\usepackage{algorithm}',
            '\\usepackage{algpseudocode}',
            '\\usepackage{float}',
            '\\usepackage{mathtools}',
            '\\usepackage{multirow}',
            '\\usepackage[parfill]{parskip}',
            '\\usepackage[shortlabels]{enumitem}',
            '',
            '',
            '% Title',
            '\\title{' + self.title + '}',
            '\\author{' + self.author + '}',
            '\\date{' + self.date + '}',
            '',
            '% Document',
            '\\begin{document}',
            '\\maketitle'
        ]

        self.document = {
            'preamble': self.preamble,
        }

    def add_section(self, title):
        section = Section(title)
        self.document[title] = section

    def compile(self):
        compiled = ''
        for section in self.document:
            compiled += self.document[section].compile()
        return compiled

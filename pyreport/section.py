class Section:

    def __init__(self, title, index=True, level=0):
        self.title = title
        self.label = '\\label{' + 'sub' * level + 'sec:' + title + '}'
        self.level = level
        self.images = {}
        self.index = index
        self.static_content = [
            '\\' + 'sub' * self.level + 'section{' + self.title + '}' if self.index else '\\' + 'sub' * self.level + 'section*{' + self.title + '}',
            self.label,
        ]
        self.content = []
        self.subsections = {
        }

    def add_subsection(self, title):
        self.subsections[title] = PyReport.Section(title, level=self.level + 1)
        self.content.append(self.subsections[title])

    def add_image(self, image, caption, label):
        self.images[label] = [
            '\\begin{figure}[H]',
            '\\centering',
            '\\includegraphics[width=\\textwidth]{' + image + '}',
            '\\caption{' + caption + '}',
            '\\label{' + label + '}',
            '\\end{figure}',
        ]
        self.content.append(self.images[label])
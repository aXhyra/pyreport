class Image:
    def __init__(self, path, caption, label):
        self.path = path
        self.caption = caption
        self.label = label
        self.content = [
            '\\begin{figure}[H]',
            '\\centering',
            '\\includegraphics[width=\\textwidth]{' + self.path + '}',
            '\\caption{' + caption + '}',
            '\\label{' + label + '}',
            '\\end{figure}',
        ]

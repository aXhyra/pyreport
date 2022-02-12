class Table:
    def __init__(self, label, caption, table):
        self.label = label
        self.caption = caption
        self.table = table
        self.content = table.to_latex(caption=self.caption, label=self.label)

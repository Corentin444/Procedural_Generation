from config import COLOR


class Case:

    def __init__(self, x, y, type):
        self.x = x
        self.y = y
        self.type = type
        self.color = COLOR[type]

    def draw(self, canvas):
        canvas.create_rectangle(self.x, self.y, self.x + 1, self.y + 1, fill=self.color, outline=self.color)

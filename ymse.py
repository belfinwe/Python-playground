class Ymse():
    Y = "Den einaste klassevariabelen! (Enda.)"

    def __init__(self, y : str):
        self.y = y

    def set_y(self, y : str):
        self.y = y

    def get_y(self) -> str:
        return self.y

    def get_Y(self) -> str:
        return self.Y


x = Ymse("ost")
print(x.get_y())
print(x.get_Y())

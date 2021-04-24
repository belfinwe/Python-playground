class Ymse:
    Y = "The only class variable (yet)"

    def __init__(self, y: str):
        self.y = y

    def set_y(self, y: str):
        self.y = y

    def get_y(self) -> str:
        return self.y

    def get_Y(self) -> str:
        return self.Y


if __name__ == "__main__":
    x = Ymse("cheese")
    print(x.get_y())
    print(x.get_Y())

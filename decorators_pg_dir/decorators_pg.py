def add_things(func):
    def wrapper():
        title = func()
        new_title = title + ' !!!'
        return new_title
    return wrapper

@add_things
def get_title():
    return '7 Levels of Using Decorators in Python'

print(get_title())
# 7 Levels of Using Decorators in Python !!!


class Fjas:
    fjas_atr = "Fjas class"

    def __init__(self, fjas):
        self.fjas = fjas


fjas_object = Fjas("self fjas")


# @Fjas("self fjas")
def ost():
    return "ost func"

print(ost())

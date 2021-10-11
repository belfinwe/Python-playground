# https://medium.com/techtofreedom/7-levels-of-using-decorators-in-python-370473fcbe76


def add_author(func):
    def wrapper(*args, **kwargs):
        author = "Some name"
        return author + "\n" + func(*args, **kwargs)
    return wrapper


@add_author
def get_title(title: str):
    return title
    

@add_author
def get_several_titles(title1, title2):
    return title1 + "\n" + title2
    # return f"Title one: {title1}, title two: {title2}."


print(get_title("Some book"))
print()
print(get_several_titles("Bok1", "Bok2"))

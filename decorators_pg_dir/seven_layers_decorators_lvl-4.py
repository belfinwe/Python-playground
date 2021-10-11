# https://medium.com/techtofreedom/7-levels-of-using-decorators-in-python-370473fcbe76


def add_author_with_name(author):
    def add_author(func):
        def wrapper(*args, **kwargs):
            # print(f"args: {args}")
            # print(f"kwargs: {kwargs}")
            return author + "\n" + func(*args, **kwargs)
        return wrapper
    return add_author


@add_author_with_name("J. K. Rowling")
def get_title(title: str):
    return title
    

print(get_title("Harry Potter"))

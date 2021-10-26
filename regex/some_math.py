import re


def get_two_numbers(data: str, operator: int) -> tuple:
    if data[-1] == "=":
        data = data[:-1]
    
    num1 = data[:operator]
    num2 = data[operator + 1:]

    return (int(num1), int(num2))


def unpack_string(func):
    def wrapper(*args, **kwargs):
        data = kwargs["data"]

        operators = ("+", "-", "*", "/")
        for op in operators:
            if op in data:
                operator_sep = data.find(op)
                operator_str = op
        
        num1, num2 = get_two_numbers(data=data, operator=operator_sep)
        return func(num1, num2, operator_str)
    return wrapper


@unpack_string
def plain(num1: int, num2: int, operation: str):
    operations_dict = {
        "+": plain_add,
        "-": plain_sub,
        "*": plain_multi,
        "/": plain_div
    }
    return operations_dict[operation](num1=num1, num2=num2)


def plain_add(num1, num2):
    """Only used by plain()"""
    return num1 + num2
def plain_sub(num1, num2):
    """Only used by plain()"""
    return num1 - num2
def plain_multi(num1, num2):
    """Only used by plain()"""
    return num1 * num2
def plain_div(num1, num2):
    """Only used by plain()"""
    if num2 == 0:
        raise ZeroDivisionError
    return num1 / num2
def plain_expo(num1, num2):
    """Only used by plain()"""
    return num1 ** num2


def expo(data):
    pass


def main(data: str):
    pattern_list = {plain: re.compile(r"^\d+[\+\-\*\/]{1}\d+\=?$"), expo: re.compile(r"^\d+\*{2}\d+\=?$")}
    for item in pattern_list.items():
        if item[1] is not None and item[1].match(data):
            return item[0](data=data)



if __name__ == "__main__":
    print("Enter 'q' to quit...")
    math_expression = input("Enter a math expression: ")
    while math_expression.lower() != "q":
        print(main(math_expression))
        math_expression = input("Enter a math expression: ")

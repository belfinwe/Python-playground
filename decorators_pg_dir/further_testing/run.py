from my_decorator import check_for_zero, log_inputs
import logging

FORMAT = "%(asctime)s: %(filename)16s:%(lineno)3d -> %(message)s"
logging.basicConfig(level=logging.INFO, format=FORMAT)

logg = logging.getLogger()


@log_inputs
@check_for_zero
def custom_division_func(num1: int|float, num2: int|float) -> float:
    """For some reason: a custom function for dividing two numbers (int or float)"""
    return num1 / num2


@log_inputs
def custom_addition_func(num1: int|float, num2: int|float) -> float:
    """For some reason: a custom function for adding two numbers (int or float)"""
    return num1 + num2


if __name__ == "__main__":
    logg.info("Starting...")
    logg.info(custom_division_func(1, 2))
    logg.info(custom_division_func(1, 0.0))
    logg.info(custom_addition_func(1, 3))

    logg.info(custom_division_func(42, 0))
    logg.info(f"{custom_division_func.__doc__=}")

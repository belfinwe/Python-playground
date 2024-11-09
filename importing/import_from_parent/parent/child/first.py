from child import utils
# from pathlib import Path
import sys

# Solution number one
sys.path.append("../")
from parent import parent_utils


def fjas():
    print("Fjas called")
    utils.support()
    print("Calling parent utils")
    parent_utils.support()

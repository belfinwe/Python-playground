from first import main as first_main
from second import main as sec_main
from source import GLOB_VAR

if __name__ == "__main__":
    print("-"*50)
    print("Running first main")
    first_main()

    print("-"*50)
    print("Running second main")
    sec_main()

    print("-"*50)
    print(f"{GLOB_VAR=}")

    print("-"*50)
    print("Done")


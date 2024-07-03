from source import GLOB_VAR

def main():
    global GLOB_VAR
    print(f"first print#1: {GLOB_VAR=}")

    update = "first:1"
    GLOB_VAR.append(update)
    print(f"Added '{update}' to GLOB_VAR")
    print(f"first print#2: {GLOB_VAR=}")


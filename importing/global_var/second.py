from source import GLOB_VAR

def main():
    global GLOB_VAR
    print(f"second print#1: {GLOB_VAR=}")

    update = "second:2"
    GLOB_VAR.append(update)
    print(f"Added '{update}' to GLOB_VAR")
    print(f"second print#2: {GLOB_VAR=}")


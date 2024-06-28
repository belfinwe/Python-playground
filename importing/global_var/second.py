from source import GLOB_VAR

def main():
    global GLOB_VAR
    print(f"second print#1: {GLOB_VAR=}")

    GLOB_VAR.append("second:1")
    print(f"Added 'second:1' to GLOB_VAR")
    print(f"second print#2: {GLOB_VAR=}")


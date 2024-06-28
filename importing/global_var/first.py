from source import GLOB_VAR

def main():
    global GLOB_VAR
    print(f"first print#1: {GLOB_VAR=}")

    GLOB_VAR.append("first:1")
    print(f"Added 'first:1' to GLOB_VAR")
    print(f"first print#2: {GLOB_VAR=}")


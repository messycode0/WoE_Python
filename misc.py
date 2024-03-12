from os import system, name
from time import sleep


def clrscn():
    # for windows (ew)
    if name == 'nt':
        _ = system('cls')
    # for mac and linux
    else:
        _ = system('clear')


def slow_print(type, mil=50):
    for char in list(type):
        print(char, end='', flush=True)
        sleep(mil / 1000)
    print("")
    pass

def debug(str):
    print(f"Debug: {str}")
    pass
from os import system, name
def clrscn():
    # for windows (ew)
    if name == 'nt':
        _ = system('cls')
    # for mac and linux
    else:
        _ = system('clear')
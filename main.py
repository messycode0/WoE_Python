from os import system, name
from time import sleep

def clrscn():
    # for windows (ew)
    if name == 'nt':
        _ = system('cls')
    # for mac and linux
    else:
        _ = system('clear')
def main():
    clrscn()
    print("game start")

    print(r"""
                    _     _          __            _
                   | |   | |        / _|          | |
__      _____  _ __| | __| |   ___ | |_    ___  __| | __ _  ___ _ __ ___
\ \ /\ / / _ \| '__| |/ _` |  / _ \|  _|  / _ \/ _` |/ _` |/ _ \ '__/ __|
 \ V  V / (_) | |  | | (_| | | (_) | |   |  __/ (_| | (_| |  __/ |  \__ \
  \_/\_/ \___/|_|  |_|\__,_|  \___/|_|    \___|\__,_|\__, |\___|_|  |___/
     Under Development, Alpha                         __/ |
                       Miguel INC                    |___/
    """)
    pass

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
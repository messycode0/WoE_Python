from settings import clrscn
from time import sleep
from parser import parse

def main():
    clrscn()
    print("game start")
    parsed_lines = parse("start.GSF")
    print(parsed_lines)
    i = 0
    for foo in parsed_lines:
        print(f"{i}: {foo}")
        i += 1
        pass
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


if __name__ == '__main__':
    main()
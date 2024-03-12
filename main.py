from misc import clrscn, slow_print, debug
from time import sleep
from parser import parse
from rich.prompt import Prompt


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

    version = parsed_lines[1]
    print(version)

    sleep(.1)
    clrscn()

    slow_print(rf"""
                    _     _          __            _
                   | |   | |        / _|          | |
__      _____  _ __| | __| |   ___ | |_    ___  __| | __ _  ___ _ __ ___
\ \ /\ / / _ \| '__| |/ _` |  / _ \|  _|  / _ \/ _` |/ _` |/ _ \ '__/ __|
 \ V  V / (_) | |  | | (_| | | (_) | |   |  __/ (_| | (_| |  __/ |  \__ \
  \_/\_/ \___/|_|  |_|\__,_|  \___/|_|    \___|\__,_|\__, |\___|_|  |___/
     Under Development, Alpha {version}               __/ |
                       Miguel INC                    |___/
    """, 0)

    debug([*parsed_lines[5]])
    slow_print(parsed_lines[5], 800)

    pass


if __name__ == '__main__':
    main()

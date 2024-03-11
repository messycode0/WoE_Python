from settings import clrscn
def parse(file_gsf):
    gsf = open(file_gsf, "r")

    line_array = ["0_buff"]
    for line in gsf:
        print(line)
        line_array.append(line)
        print(line_array)
        pass

    gsf.close()
    clrscn()
    return line_array
    pass
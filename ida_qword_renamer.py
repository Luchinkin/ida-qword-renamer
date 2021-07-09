import pathlib
import idaapi
import idc

def linear_address(rva):
    return idaapi.get_imagebase() + rva

current_path = str(pathlib.Path(__file__).parent.resolve())
input_file = open(current_path + "\\input.txt", 'r')

lines = input_file.readlines()

for line in lines:
    parsed = line.partition("=")
    address = linear_address(int(parsed[0], 16))
    name = parsed[2].rstrip() + "_qword"
    if idc.set_name(address, name, SN_NOWARN) == 0:
        print("[ida_qword_renamer] Couldn't rename qword at", hex(address), "to", name);

print("[ida_qword_renamer] Renamed!")

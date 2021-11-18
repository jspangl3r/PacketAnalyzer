class Packet:
    def __init__(self):
        self.ip_hdr_len = 0

def parse(file_name) :
	f = open(file_name)
        lines = f.readlines()
        i = 0
        while i < len(lines):
            line = lines[i].strip()
            while line != "":
                split_hex = line.split()
                i += 1


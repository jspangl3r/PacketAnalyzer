class Packet:
    def __init__(self):
        self.type = -1
        self.ip_hdr_len = 0
        self.time = 0.0
        self.src_ip = ""
        self.dest_ip = ""
        self.frame_len = 0
        self.data_len = 0
        self.ttl = 0


def parse(file_name):
    f = open(file_name)
    lines = f.readlines()
    i = 0
    packet_list = []
    while i < len(lines):
        split_line = lines[i].strip().split()
        packet = Packet()
        if split_line[0] == "No.":
            i += 1
            split_line = lines[i].strip().split()
            packet.time = float(split_line[1])
            i += 2

        split_line = lines[i].strip().split()[:-1]
        hex_data = []
        while len(split_line[0]) == 4:
            hex_data.extend(split_line[1:])
            i += 1
            if i < len(lines):
                split_line = lines[i].strip().split()[:-1]
            else:
                break
        print(hex_data)
        

parse("text_filt.txt")

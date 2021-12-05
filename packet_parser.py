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
        self.seq_number = 0
    # Allows packet objects to be printed in a readable manner 
    def __str__(self):
        pack_str = ""
        pack_str += "Time: " + str(self.time) + "\n"
        pack_str += "Type: " + str(self.type) + "\n"
        pack_str += "Src: " + self.src_ip + ", Dest: " + self.dest_ip + "\n"
        pack_str += "TTL: " + str(self.ttl) + ", Seq Num: " + str(self.seq_num) + "\n"
        pack_str += "Data Len: " + str(self.data_len) + ", Total Len: " + str(self.frame_len) + "\n"
        return pack_str

def hex_to_ip(hex_data):
    nums = [str(int(x,16)) for x in hex_data]
    ip_addr = ".".join(nums)
    return ip_addr
        
# Takes in a file name containing the filtered ICMP packets and returns a list of 
# packet objects
def parse(file_name):
    f = open(file_name)
    lines = f.readlines()
    i = 0
    packet_list = []
    eth_hdr_len = 14
    icmp_hdr_len = 8
    while i < len(lines):
        split_line = lines[i].strip().split()
        if split_line[0] == "":
            i+=1
            continue
        packet = Packet()
        if split_line[0] == "No.":
            i += 1
            split_line = lines[i].strip().split()
            packet.time = float(split_line[1])
            i += 2

        split_line = lines[i].strip().split()
        hex_data = []
        while split_line != [] and len(split_line[0]) == 4:
            hex_data.extend(split_line[1:-1])
            i += 1
            if i < len(lines):
                split_line = lines[i].strip().split()
            else:
                break
        i+=1
        #### IP HEADER ####
        packet.ip_hdr_len = int(hex_data[eth_hdr_len][1])*4
        
        #Get ttl data, starts at the 8th byte of the ip header
        packet.ttl = int(hex_data[eth_hdr_len+8],16)
        
        #Get source and destination addresses
        src_start = eth_hdr_len + 12 # Addresses are 12 bytes into the ip header
        src_bytes = [hex_data[i] for i in range(src_start, src_start+4)]
        dest_bytes = [hex_data[i] for i in range(src_start+4, src_start+8)]
        packet.src_ip = hex_to_ip(src_bytes)
        packet.dest_ip = hex_to_ip(dest_bytes)

        #### ICMP HEADER ####
        #Get ICMP type
        packet.type = int(hex_data[eth_hdr_len+packet.ip_hdr_len],16)

        #Get sequence number
        seq_start = eth_hdr_len+packet.ip_hdr_len+6
        seq_bytes = [hex_data[x] for x in range(seq_start, seq_start+2)]
        packet.seq_num = int("".join(seq_bytes),16)
        
        #### GENERAL ####
        packet.frame_len = len(hex_data)
        data_start = eth_hdr_len+packet.ip_hdr_len+icmp_hdr_len
        packet.data_len = len(hex_data[data_start:])
        packet_list.append(packet)
    return packet_list

from filter_packets import filter 
from packet_parser import parse 
from compute_metrics import compute 

def main():
    # Loop through Nodes 1 - 4
    NUM_NODES = 4
    output_f = open("output.csv", "w")
    for i in range(1, NUM_NODES + 1):
        unfiltered = f"captures/Node{i}.txt"
        filter(unfiltered)
        filtered = f"captures/Node{i}_filtered.txt"
        packets = parse(filtered)
        compute(packets, i, output_f)
        if i != NUM_NODES:
            output_f.write("\n") 
  
    output_f.close()

if __name__ == "__main__":
    main()

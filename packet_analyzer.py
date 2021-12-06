from filter_packets import filter
from packet_parser import *
from compute_metrics import *

def main():
    # Loop through Nodes 1 - 4
    for i in range(1, 5):
        unfiltered = f"captures/Node{i}.txt"
        filter(unfiltered)
        filtered = f"captures/Node{i}_filtered.txt"
        packets = parse(filtered)
        compute(i, packets)

if __name__ == "__main__":
    main()

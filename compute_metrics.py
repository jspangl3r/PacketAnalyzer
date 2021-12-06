from packet_parser import Packet

# Global IP information of nodes
NODE_IPS = ["192.168.100.1", "192.168.100.2", "192.168.200.1", "192.168.200.2"]

def compute(packets, node_num, output_f):
    node_ip = NODE_IPS[node_num - 1]
    
    output_f.write(f"Node {node_num}\n\n")

    # Data size metrics
    echo_requests_sent = [p for p in packets if p.src_ip == node_ip and p.type == 8]
    echo_requests_received = [p for p in packets if p.dest_ip == node_ip and p.type == 8]
    echo_replies_sent = [p for p in packets if p.src_ip == node_ip and p.type == 0]
    echo_replies_received = [p for p in packets if p.dest_ip == node_ip and p.type == 0]
    # 1. Num Echo Requests sent
    num_echo_requests_sent = len(echo_requests_sent)
    # 2. Num Echo Requests received
    num_echo_requests_received = len(echo_requests_received)
    # 3. Num Echo Replies sent 
    num_echo_replies_sent = len(echo_replies_sent)
    # 4. Num Echo Replies received 
    num_echo_replies_received = len(echo_replies_received)
    # 5. Total Echo Request bytes sent
    total_echo_request_bytes_sent = sum([p.frame_len for p in echo_requests_sent])
    # 6. Total Echo Request bytes received
    total_echo_request_bytes_received = sum([p.frame_len for p in echo_requests_received])
    # 7. Total Echo Request data sent
    total_echo_request_data_sent = sum([p.data_len for p in echo_requests_sent])
    # 8. Total Echo Request data received
    total_echo_request_data_received = sum([p.data_len for p in echo_requests_received])
    
    output_f.write("Echo Requests Sent,Echo Requests Received,Echo Replies Sent,Echo Replies Received\n")
    output_f.write(f"{num_echo_requests_sent},{num_echo_requests_received},{num_echo_replies_sent},{num_echo_replies_received}\n\n")
    output_f.write("Echo Request Bytes Sent (bytes),Echo Request Data Sent (bytes)\n")
    output_f.write(f"{total_echo_request_bytes_sent},{total_echo_request_data_sent}\n")
    output_f.write("Echo Request Bytes Received (bytes),Echo Request Data Received (bytes)\n")
    output_f.write(f"{total_echo_request_bytes_received},{total_echo_request_data_received}\n\n")
     
    # Time Based Metrics
    # 1. Average Ping Round Trip Time (RTT)
    ping_rtts = []
    avg_rtt = 0
    for request in echo_requests_sent:
        # Find corresponding ping reply
        reply = [p for p in echo_replies_received if p.seq_num == request.seq_num][0]
        ping_rtts.append(reply.time - request.time) 
    avg_rtt = sum(ping_rtts) / len(packets)
    # 2. 
    
    output_f.write(f"Average RTT (milliseconds),{avg_rtt}\n")

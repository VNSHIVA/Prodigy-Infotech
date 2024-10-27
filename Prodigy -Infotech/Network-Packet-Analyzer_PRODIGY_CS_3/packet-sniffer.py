import os
import sys
from scapy.all import IP, TCP, sniff, conf

# Disclaimer and terms of use
print("------------------------ Packet Sniffer Tool Disclaimer ---------------------------")
print("This packet sniffer tool is intended for educational and ethical purposes only.")
print("Unauthorized use, distribution, or modification of this tool is strictly prohibited.")
print("By using this tool, you agree to the following terms and conditions:")
print("\n1. You will only use this tool on networks and systems for which you have explicit permission.")
print("2. You will not use this tool to violate any laws, regulations, or terms of service.")
print("3. You will not use this tool to harm, disrupt, or exploit any networks or systems.")
print("4. You will not use this tool to intercept, collect, or store any sensitive or confidential information.")
print("5. You will not redistribute or sell this tool without the express permission of the author.")
print("6. The author is not responsible for any damages or losses incurred as a result of using this tool.")
print("7. You will respect the privacy and security of all networks and systems you interact with using this tool.")

accept_terms = input("\nDo you accept these terms and conditions? (y/n): ")

if accept_terms.lower() != 'y':
    print("You must accept the terms and conditions before using this tool.")
    sys.exit()

print("\n--------------- Packet Sniffing Tool ---------------")

# Function to display and save captured packets
def packet_sniff(packet):
    if packet.haslayer(TCP) and packet.haslayer(IP):
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        src_port = packet[TCP].sport
        dst_port = packet[TCP].dport
        protocol = packet[IP].proto
        
        # Safely attempt to access the payload
        payload = str(packet[TCP].payload) if packet[TCP].payload else "No Payload"

        output_string = f"Source IP: {src_ip}\n"
        output_string += f"Destination IP: {dst_ip}\n"
        output_string += f"Source Port: {src_port}\n"
        output_string += f"Destination Port: {dst_port}\n"
        output_string += f"Protocol: {protocol}\n"
        output_string += f"Payload: {payload[:50]}...\n\n"  # Added newline for better readability

        print(output_string, end='')
        
        try:
            with open('packet_sniffer_results.txt', 'a') as f:
                f.write(output_string)
        except IOError as e:
            print(f"Error writing to file: {e}")

# Function to start sniffing packets
def sniffing(interface):
    conf.sniff_promisc = True  # Enable promiscuous mode to capture all packets
    # Using a filter to capture only IP packets
    try:
        sniff(iface=interface, filter="ip", prn=packet_sniff, store=0)
    except Exception as e:
        print(f"Error during sniffing: {e}")

# Ask user for the network interface to sniff on
interface = input("Enter the network interface to sniff on (e.g., 'Wi-Fi' or 'Ethernet'): ")

# Validate the interface input
if not interface:
    print("You must enter a valid network interface.")
    sys.exit()

# Calls the sniffing function to start capturing packets
sniffing(interface)

# Displays the output file's name and location after successful sniffing
print(f"\nResults saved to: packet_sniffer_results.txt")

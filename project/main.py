import os
import geoip2.database
from scapy.all import *

# def ip_to_as(ip_address):
#     # Load the MaxMind ASN database
#     reader = geoip2.database.Reader(r"c:\Users\vigne\OneDrive\Desktop\Downloads\GeoLite2-ASN.mmdb")

#     # Perform the IP to AS lookup
#     try:
#         response = reader.asn(ip_address)
#         return (response.autonomous_system_number,response.autonomous_system_organization)
#     except geoip2.errors.AddressNotFoundError:
#         return "IP Address not found in the database."
#     finally:
#         reader.close()

# # Function to read pcap files and perform ASN lookup
# def process_pcap_files(folder_path):
#     as_names = set()  # Container to store AS names without repetition

#     for file_name in os.listdir(folder_path):
#         if file_name.endswith('.pcap'):
#             file_path = os.path.join(folder_path, file_name)
#             print("Processing file:", file_path)

#             # Read pcap file
#             packets = rdpcap(file_path)

#             # Extract IP addresses from packets
#             ip_addresses = [pkt[IP].src for pkt in packets if IP in pkt]

#             # Perform ASN lookup for each IP address and add AS names to the container
#             for ip_address in ip_addresses:
#                 as_name = ip_to_as(ip_address)
#                 if as_name != "IP Address not found in the database.":
#                     as_names.add(as_name)
#                 else:
#                     print("ip address {} not known".format(ip_address))

#     for name in as_names:
#         print(name)


# folder_path = r"c:\Users\vigne\OneDrive - IIT Delhi\sem 8 2023-24\COL867\data\01012023\data"
# process_pcap_files(folder_path)


# Initialize an empty dictionary to store ISP names and ASN numbers
isp_asns = {}

with open('isp_to_asns_map.txt', 'r') as file:
    # Read each line in the file
    for line in file:
        # Split the line at the comma
        parts = line.strip().split(',')
        # Extract ISP name (first part)
        isp_name = parts[0].strip()
        # Extract list of ASN numbers (remaining parts)
        asns = [asn.strip() for asn in parts[1:]]
        isp_asns[isp_name] = asns

print(isp_asns.keys())

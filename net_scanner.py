import scapy.all as scapy

# ARP request
# broadcast
# response

arp_package = scapy.ARP(pdst="192.168.0.1/24")

#scapy.ls(scapy.ARP)

broadcast_package = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")

#scapy.ls(scapy.Ether)

combined_pack = broadcast_package/arp_package

(answered_list, unanswered_list) = scapy.srp(combined_pack, timeout=1)

print(list(answered_list))
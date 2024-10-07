import scapy.all as scapy
import optparse

# ARP request
# broadcast
# response

def get_user_input() :
    parse_obj = optparse.OptionParser()
    parse_obj.add_option('-i', '--ipadress', dest="ip_adress", help="Enter IP adress for changing!")
    (user_input, user_arg) = parse_obj.parse_args()
    if not user_input.ip_adress:
        print ("Enter IP adress")
    return user_input

def scan_my_network(ip):
    arp_package = scapy.ARP(pdst=ip)
    #scapy.ls(scapy.ARP)
    broadcast_package = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    #scapy.ls(scapy.Ether)
    combined_pack = broadcast_package/arp_package
    (answered_list, unanswered_list) = scapy.srp(combined_pack, timeout=1)
    answered_list.summary()

user_ip_adress = get_user_input()
scan_my_network(user_ip_adress)

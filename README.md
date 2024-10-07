# Net-Scanner-PY

## What is ARP?
ARP (Address Resolution Protocol) is used to map an IP address (logical address) to a MAC address (physical address). Devices in a network use ARP to communicate with each other by resolving their IP addresses into MAC addresses.

## ARP Table
Both your device (e.g., computer) and other devices connected to the same network maintain an ARP table. This table stores pairs of IP addresses and corresponding MAC addresses.

## How ARP Requests Work
When you want to communicate with a device in the network, your system sends out an ARP request asking, “Who has IP address X.X.X.X?”
The device with that IP address replies back with its MAC address in an ARP response.
Both devices update their ARP tables with this information, allowing them to communicate with each other without sending further ARP requests.
Network Scanning Using ARP
To scan devices on a Wi-Fi network, you can send ARP requests to every IP address within the range of your network’s subnet. When a device responds to the ARP request, it adds its IP-MAC pair to your ARP table, allowing you to map which devices are present on the network. Similarly, the device that responds will also add your IP-MAC pair to its own ARP table.

## ARP Network Scanner Code
This code helps you scan a network to find all the devices connected to it by sending ARP (Address Resolution Protocol) requests to different IP addresses in the network. It will then display which devices are responding, so you can see who else is on the network with you.

## Getting the IP Address from the User
The function **```get_user_input()```** is used to ask the user to enter an IP address (or a range of IPs) that they want to scan. For example, you might enter something like **```192.168.1.1/24```** to scan all devices in your local network.

It uses a Python library called optparse to get this information from the command line, where you can pass the IP address using **```-i```** or **```--ipadress```**. If the user forgets to enter an IP address, the program will remind them to do so.

```python
def get_user_input() :
    parse_obj = optparse.OptionParser()
    parse_obj.add_option('-i', '--ipadress', dest="ip_adress", help="Enter IP adress for scanning!")
    (user_input, user_arg) = parse_obj.parse_args()
    if not user_input.ip_adress:
        print ("Enter IP adress")
    return user_input
```

## ARP Request and Broadcast
The function **```scan_my_network(ip)```** does the actual network scanning.

First, it creates an ARP packet using **```scapy.ARP(pdst=ip)```**. This packet is like a message that says, “Hey, who has this IP address?” and it’s sent to every IP in the range you specified.
Then, it creates a broadcast packet using **```scapy.Ether(dst="ff:ff:ff:ff:ff:ff")```**. This broadcast is sent to all devices in the network (the **```ff:ff:ff:ff:ff:ff```** is a special MAC address for broadcasting).
The ARP packet and broadcast packet are combined into one, called **```combined_pack```**, which is then sent to the network.

```python
def scan_my_network(ip):
    arp_package = scapy.ARP(pdst=ip)
    broadcast_package = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    combined_pack = broadcast_package/arp_package
    (answered_list, unanswered_list) = scapy.srp(combined_pack, timeout=1)
    answered_list.summary()
```  

## Sending and Receiving
The line **```scapy.srp(combined_pack, timeout=1)```** sends the combined packet and waits for a response. Devices that are connected to your network and respond to the ARP request will appear in the **```answered_list```**.

The **```answered_list.summary()```** will print out a summary of all the devices that replied, showing their IP addresses and MAC addresses.

## Running the Program
The last part of the code grabs the user's input (the IP address) and passes it to the **```scan_my_network```** function to start the scanning process.

```python
user_ip_adress = get_user_input()
scan_my_network(user_ip_adress.ip_adress)
``` 




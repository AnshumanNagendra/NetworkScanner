import scapy.all as scapy

def scan(ip):
	arp_request = scapy.ARP(pdst = ip) #pdst is the ip address field
	broadcast = scapy.Ether(dst="")
	arp_request_broadcast = broadcast/arp_request #combining using "/"
	answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0] #it denotes the first element in the list because it is going to return 2 lists of data

	
	clients_list=[] #list
	for element in answered_list
		client_dict = {"IP":element[1].psrc ,"MAC":element[1].hwsrc} #dictionary
		clients_list.append(client_dict)
		print(element[1].psrc+"\t\t"+element[1].hwsrc)

def print_result(results_list):
	print("IP\t\t\tMAC Address\n-----------------")
	for client in results_list
		print(client["IP"] + "\t\t" + client["MAC"])
	
scan_result = scan("10.0.2.1/24")
print_result(scan_result)
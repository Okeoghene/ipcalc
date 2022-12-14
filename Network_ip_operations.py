ip_address = [192,166,254,195]
cidr = 30
subnet_mask = [255,255,255,0]

net_ip_placeholder = [0,0,0,0]
broadcast_holder = [255,255,255,255]
firstip = [1,0,0,1]
lastip = [1,255,255,255]

if cidr !=32:
    network_bits = cidr % 8
    network_octect = cidr // 8
    host_bits1 = 8 - network_bits
    c = list(range(network_octect))
    lenght = len(c)
    host_octect1 = 2 ** host_bits1
    host_octect2 = ip_address[lenght] // host_octect1

    for index in list(range(network_octect)):
        net_ip_placeholder[index] = ip_address[index]

    if ip_address[lenght]< host_octect1:
        net_ip_placeholder[lenght] = 0
    elif ip_address[lenght]> host_octect1:
            net_ip_placeholder[lenght] = host_octect2 * host_octect1


    for index in list(range(network_octect)):
        broadcast_holder[index] = ip_address[index]

    broadcast_holder[lenght] = ((host_octect2 + 1) * host_octect1) - 1

    for index in list(range(network_octect+1)):
        firstip[index] = net_ip_placeholder[index]

    if cidr >= 24:
        firstip[lenght] = net_ip_placeholder[lenght] +1
    else:
        firstip[3] = 1

    for index in list(range(network_octect+1)):
        lastip[index] = broadcast_holder[index]

    if cidr >= 24:
        lastip[lenght] = broadcast_holder[lenght] -1
    else:
        lastip[3] = 255

else:
    net_ip_placeholder = ip_address


host = 2 ** (32-cidr)

usable_host = host - 2

if usable_host <= 0:
    usable_host = 0

if cidr != 32:
    print(net_ip_placeholder, 'is the', host_octect2+1, 'network address in the subnet'
    "\nthe usable host range are as follows;", firstip,'-', lastip, 
    "\nthe broadcast address is,", broadcast_holder, 
    "\nthe total number of host is,", host,  
    "\nthe number of usable host is,", usable_host)
else: 
    print(net_ip_placeholder, 'is the network address in the subnet'
    '\n the usable host range are as follows;', net_ip_placeholder,'-', net_ip_placeholder, 
    "\nthe broadcast address is,", net_ip_placeholder, "the total number of host is,", host, 
    "\nthe number of usable host is,", usable_host)

print(type(host_octect2))
print(type(ip_address[lenght]))
print(type(host_octect1))
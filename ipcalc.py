ip_address = input('Enter ip address: ') #Takes input for IP ADDRESS
cidr = input('Enter CIDR: /') #Takes input for CIDR
subnet_mask = input('Enter subnet mask: ') #Takes input for SUBNET MASK


ip_address = ip_address.split('.') #Makes the IP ADDRESS a list
subnet_mask = subnet_mask.split('.') #Makes the SUBNET a list


values = [0, 128, 192, 224, 240, 248, 252, 254, 255] #It is used to define values in SUBNET MASK.
mask_holder = [] #creates an empty list.
verified_mask = [] #This holds the SUBNET MASK, if it is not faulty.
guilty_ip = False #This turns true if the IP ADDRESS is faulty.
faulty_CIDR = False #This turns true if the CIDR is faulty.
guilty_mask = False #This turns true if the SUBNET MASK is faulty.
net_ip_placeholder = [0,0,0,0]
broadcast_holder = [255,255,255,255]
firstip = [1,0,0,1]
lastip = [1,255,255,255]


if ip_address == []:
    guilty_ip = True #If IP ADDRESS is empty, it is faulty.
elif len(ip_address) != 4:
    guilty_ip = True #Confirms that the octects in IP ADDRESS are 4.
for items in ip_address:
    if items == '':
        guilty_ip = True #Verifies that the octects in IP ADDRESS are not NULL.
    else:
        items = int(items)
        if items > 255: 
            guilty_ip = True #Ensures that the values in each octects in IP ADDRESS is !> 255.
if guilty_ip == True:
    print('rexamine your ip address please') #Ends the program if the IP ADDRESS is wrong.


if cidr ==  '':
    faulty_CIDR = True # Confirms if the CIDR is a null value, if null the 'faulty_CIDR' is TRUE.
else:
    cidr = int(cidr)
    if cidr > 32 or cidr < 0:
        faulty_CIDR = True # Confirms if the CIDR is in a range of numbers 1:32, if not the 'faulty_CIDR' is TRUE.


for val1, val2 in zip(subnet_mask[:3], subnet_mask[1:]): # Compares values in SUBNET MASK with a consecuutive in the SUBNET.
    if val1 >= val2 and val1 != '':
        val1 = int(val1)
        val2 = int(val2)
        if val1 in values:
            if (val1 <= 255) and (val2 <=255):
                if (val1 != 255 and val2 == 0):
                    guilty_mask = False # Verifies that if any value of the subnet is != 255, the next value is !> 0.
                else:
                    guilty_mask = True          
else:
    guilty_mask = True # Confirms that there are 4 octets in the SUBNET MASK.

if len(subnet_mask) == 4 and subnet_mask != ['']: # Ensures that SUBBET MASK is not NULL and there are 4 octects.
    guilty_mask == False

if guilty_mask == False:
    for digits in subnet_mask:
        digits = int(digits)  #converts every digit in subnet mask to integers
        digits = bin(digits).replace('0b','') #Converts the subnet from decimal to binary
        mask_holder.append(digits)

new_subnet_mask = ''.join(mask_holder) #Converts the list to a string
new_cidr = new_subnet_mask.count('1') #This calculates the network bits SUBNET MASK (It should be same as the CIDR if available)

if guilty_mask == True and faulty_CIDR == True:
    print('Please verify the subnet and or CIDR')

if (faulty_CIDR == False and guilty_mask == False) and (new_cidr != cidr):    
    print('Please confirm that you have correctly entered one of either CIDR or SUBNET MASK') #Confirms that the new CIDR is equal to the CIDR inputed

if guilty_mask == False:
    cidr = new_cidr

if cidr !=32:
    network_bits = cidr % 8
    network_octect = cidr // 8
    host_bits1 = 8 - network_bits
    c = list(range(network_octect))
    lenght = len(c)
    host_octect1 = 2 ** host_bits1
    host_octect2 = int(ip_address[lenght]) // host_octect1

    for index in list(range(network_octect)):
        net_ip_placeholder[index] = ip_address[index]

    if int(ip_address[lenght])< host_octect1:
        net_ip_placeholder[lenght] = 0
    elif int(ip_address[lenght])> host_octect1:
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
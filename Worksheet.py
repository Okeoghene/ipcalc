ip_address = input('Enter ip address: ') #Takes input for IP ADDRESS
#cidr = input('Enter CIDR: /') #Takes input for CIDR
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
new_cidr = 17


if subnet_mask != [''] and len(subnet_mask) == 4: #Ensures that SUBBET MASK is not NULL and there are 4 octects.
    for val1, val2 in zip(subnet_mask, subnet_mask[1:]): # Compares values in SUBNET MASK with a consecuutive in the SUBNET.
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

if guilty_mask == False:
    for digits in subnet_mask:
        digits = int(digits)  #converts every digit in subnet mask to integers
        digits = bin(digits).replace('0b','') #Converts the subnet from decimal to binary
        mask_holder.append(digits)

new_subnet_mask = ''.join(mask_holder) #Converts the list to a string
new_cidr = new_subnet_mask.count('1') #This calculates the network bits SUBNET MASK (It should be same as the CIDR if available)

if guilty_mask == False:
    print(new_cidr)
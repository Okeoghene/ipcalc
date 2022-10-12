subnet_mask = '128.0.0.0' #currently acting as the subnet_mask input

subnet_mask = subnet_mask.split('.') #This converts the input to a list

mask_holder = [] #creates an empty list.

for digits in subnet_mask:
    digits = int(digits)  #converts every digit in subnet mask to integers
    digits = bin(digits).replace('0b','') #Converts the subnet from decimal to binary
    mask_holder.append(digits) #puts the binary format of the subnet into mask_holder

print(mask_holder)
subnet_mask = ''.join(mask_holder) #Converts the list to a string

new_cidr =subnet_mask.count('1') 

print(subnet_mask.count('1')) #prints the number of the 1's in the binary
print(len(subnet_mask))
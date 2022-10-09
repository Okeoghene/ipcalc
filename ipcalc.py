ip_address = input('Enter ip address: ')
cidr = int(input('Enter CIDR: /'))
subnet_mask = input('Enter subnet mask: ')

ip_address = ip_address.split('.')
subnet_mask = subnet_mask.split('.')

mask_holder = []

for digits in subnet_mask:
    digits = int(digits)
    digits = bin(digits)
    mask_holder.append(digits)

subnet_mask = mask_holder

subnet_mask = ','.join(subnet_mask)

print(subnet_mask)
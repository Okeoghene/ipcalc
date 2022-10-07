subnet_mask = '255.255.128.254' #currently acting as the subnet_mask input (Noticed if a dot is last string entered it crashes)

subnet_mask = subnet_mask.split('.') #This converts the input to a list

values = [0, 128, 192, 224, 240, 248, 252, 254, 255]

guilty_mask = False
faulty_mask = []
verified_mask = []

if subnet_mask == []:
    guilty_mask = True
elif len(subnet_mask) != 4:
    guilty_mask = True

for items in subnet_mask:
    if items == '':
        guilty_mask = True
    else:
        items = int(items)
        if items not in values:
            guilty_mask = True
        elif items > 255:
            guilty_mask = True

for val1, val2 in zip(subnet_mask, subnet_mask[1:]):
    if val1 < val2:
        guilty_mask = True
    else:
        if val1 != '255' and val2 >'0':
            guilty_mask = True

if guilty_mask == True:
   faulty_mask = subnet_mask
else:
    verified_mask = subnet_mask

subnet_mask = verified_mask

print(faulty_mask)
cidr = input('Please enter the CIDR /')
cidr = int(cidr)
values = values = [0, 128, 192, 224, 240, 248, 252, 254, 255]
placeholder = [0,0,0,0]

network_bits = cidr % 8
network_octect = cidr // 8
host_bits1 = 8 - network_bits

c = list(range(network_octect))
lenght = len(c)

for index in list(range(network_octect)):
    placeholder[index] = 255 
    
if not(cidr == 32 and network_bits == 0):
    placeholder[lenght] = values[network_bits]

print(placeholder)
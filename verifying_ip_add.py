ip_address = '7.168.256.5'
ip_address = ip_address.split('.')

guilty_ip = False
verified_ip = []

if ip_address == []:
    guilty_ip = True
elif len(ip_address) != 4:
    guilty_ip = True

for items in ip_address:
    if items == '':
        guilty_ip = True
    else:
        items = int(items)
        if items > 255:
            guilty_ip = True

if guilty_ip == True:
    print('rexamine your ip address please')
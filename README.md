# ipcalc
ipcalc is a python program that takes in 3 inputs from the ;
- ip address
- subnet mask
- CIDR

and calculates the following;

- number of usable ip address 
- network address
- broadcast address
















TO DO
- [x] Get input from user
- [ ] Take either subnet mask or CIDR
- [x] Validates inputs
- [x] Validation A (4 decimal values in the ip address each not greater than 255)
- [x] Validation B (4 decimal values in the subnet mask each not greater than 255 and is either 0, 128, 192, 224, 240, 248, 252, 254 and 255)
- [x] Validation C (CIDR is a decimal value not greater than 32)
- [x] Convert subnet mask to CIDR
- [x] Convert from CIDR to subnetmask
- [x] Calculate Network address
- [x] Calculate Broadcast address
- [x] The number of subnets
- [x] Number of usable host
- [x] First usable host and last usable host
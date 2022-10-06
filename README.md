# ipcalc
ipcalc is a python program that takes in 3 inputs from the ;
- ip address
- subnet mask
- VLSM

and calculates the following;

- number of usable ip address 
- network address
- broadcast address
















TO DO
- [x] Get input from user
- [ ] Take either subnet mask or VLSM
- [ ] Validates inputs
- [ ] Validation A (4 decimal values in the ip address each not greater than 255)
- [ ] Validation B (4 decimal values in the subnet mask each not greater than 255 and is either 0, 128, 192, 224, 240, 248, 252, 254 and 255)
- [ ] Validation C (VLSM is a decimal value not greater than 32)
- [ ] Convert subnet mask to VLSM
- [ ] Calculate Network address
- [ ] Calculate Broadcast address
- [ ] Subtract Network address from Broadcast address (Number of usable host)
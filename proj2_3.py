""" Importing required modules to solve the problem. """
from matplotlib import pyplot as plt
import mahamains

com_maharashtra = mahamains.maharashtra_reader
districts = mahamains.district_reader
# Create dictionary to pincode and their district.
com_districts = {}
# Find district for each pincode.
for district in districts:
    com_districts[district['Pincode']] = district['District']
# Create dictionary to store pincode and no: of registered companies.
pins = {}
# Find pincode and no: of registered companies in year 2015.
for i in com_maharashtra:
    x = i['Registered_Office_Address']
    x = x[-6:]
    y = i['DATE_OF_REGISTRATION']
    if y != 'NA':
        y = y[-2:]
        if x != '000000' and y == '15':
            if x in pins:
                pins[x] += 1
            else:
                pins[x] = 1
# Create dictionary to store districts and no: of registered companies.
dist_com = {}
# Calculate no: of registered companies for each district.
for pin, count in pins.items():
    if pin in com_districts:
        dist_com[com_districts[pin]] = count
# Plotting the calculated data.
plt.bar(list(dist_com.keys()), list(dist_com.values()))
plt.xlabel('DISTRICTS')
plt.ylabel('NO: OF COMPANIES')
plt.show()

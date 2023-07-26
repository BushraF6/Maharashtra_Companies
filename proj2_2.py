""" Importing the required modules to solve the problem. """
from matplotlib import pyplot as plt
import mahamains

com_maharashtra = mahamains.maharashtra_reader
# Create dictionary to store no: of registrations per year.
year = {}
# Calculate no: of registrations per year.
for company in com_maharashtra:
    y = company['DATE_OF_REGISTRATION'][-2:]
    if y != "NA":
        if int(y) < 23:
            y = '20'+y
        else:
            y = '19'+y
        if y in year:
            year[y] += 1
        else:
            year[y] = 1
# Plotting the calculated data.
plt.bar(list(year.keys()), list(year.values()))
plt.title('Company Registration per Year')
plt.xlabel('Year')
plt.ylabel('Number of Companies Registered')
plt.show()

""" Importing the required modules to solve the problem. """
from matplotlib import pyplot as plt
import mahamains

com_maharashtra = mahamains.maharashtra_reader
# Create list to store the authorized capital of companies.
aut_capital = []
# Appending the authorized capital values to aut_capital list.
for company in com_maharashtra:
    aut_capital.append(company['AUTHORIZED_CAP'])
aut_capital.sort()

plt.hist(aut_capital, bins=20)
plt.xticks(ticks=['0', '100000', '1000000', '10000000', '100000000',
                  max(aut_capital)], labels=([min(aut_capital),
                  '<1L', '1L-10L', '10L-1CR', '1CR-10CR', '>10CR']))
plt.show()

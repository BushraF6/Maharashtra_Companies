import mahamains
import matplotlib.pyplot as plt
com_maharashtra=mahamains.maharashtra_reader
year={}
for company in com_maharashtra:
    y=company['DATE_OF_REGISTRATION'][-2:]
    if y!="NA":
        if int(y)<23:
            y='20'+y
        else:
            y='19'+y
        if y in year.keys():
            year[y]+=1
        else:
            year[y]=1
plt.bar(list(year.keys()), list(year.values()))
plt.title('Company Registration per Year')
plt.xlabel('Year')
plt.ylabel('Number of Companies Registered')
plt.show() 
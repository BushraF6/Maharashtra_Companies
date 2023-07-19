import mahamains
from matplotlib import pyplot as plt

com_maharashtra=mahamains.maharashtra_reader
districts=mahamains.district_reader
com_districts={}
for i in range(len(districts)):
    com_districts[districts[i]['Pincode']]=districts[i]['District']

pin={}
for i in range(len(com_maharashtra)):
    x=com_maharashtra[i]['Registered_Office_Address']
    x=x[-6:]
    y=com_maharashtra[i]['DATE_OF_REGISTRATION']
    if y!='NA':
        y=y[-2:]
        if x[0] =='4' and y=='15':
            if x in pin.keys():
                pin[x]+=1
            else:
                pin[x]=1

dist_com={}
for key, value in pin.items():
    if key in com_districts.keys():
        if key in dist_com.keys():
            dist_com[com_districts[key]]+=value
        else:
            dist_com[com_districts[key]]=value

district=[]
count=[]
for key, value in dist_com.items():
    district.append(key)
    count.append(value)
    
plt.bar(district, count)
plt.xticks(range(len(district)), district)
plt.xlabel('DISTRICTS')
plt.ylabel('NO: OF COMPANIES')
plt.show()
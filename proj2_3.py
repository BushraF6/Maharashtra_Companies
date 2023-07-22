from matplotlib import pyplot as plt
import mahamains

com_maharashtra=mahamains.maharashtra_reader
districts=mahamains.district_reader

com_districts={}
for district in districts:
    com_districts[district['Pincode']]=district['District']

pins={}
for i in com_maharashtra:
    x=i['Registered_Office_Address']
    x=x[-6:]
    y=i['DATE_OF_REGISTRATION']
    if y!='NA':
        y=y[-2:]
        if x!='000000' and y=='15':
            if x in pins:
                pins[x]+=1
            else:
                pins[x]=1

dist_com={}
for pin, count in pins.items():
    if pin in com_districts.keys():
        dist_com[com_districts[pin]]=count

district=[]
count=[]
for key, value in dist_com.items():
    district.append(key)
    count.append(value)
    
plt.bar(district, count)
plt.xticks(range(len(district)), district, rotation='vertical')
plt.xlabel('DISTRICTS')
plt.ylabel('NO: OF COMPANIES')
plt.show()

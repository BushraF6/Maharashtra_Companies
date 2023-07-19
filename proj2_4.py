from matplotlib import pyplot as plt
import mahamains

com_maharashtra=mahamains.maharashtra_reader
com_type={}
years=[]

for company in com_maharashtra:
    if company['PRINCIPAL_BUSINESS_ACTIVITY_AS_PER_CIN'] not in com_type:
        com_type[company['PRINCIPAL_BUSINESS_ACTIVITY_AS_PER_CIN']]=0
    twenty='20'
    y=company['DATE_OF_REGISTRATION'][-2:]
    if y!='NA':
        if int(y)<23 and twenty+y not in years:
            years.append(twenty+y)
        
years=sorted(years)[13:]
com_count_year={year:com_type for year in years}

for company in com_maharashtra:
    y=company['DATE_OF_REGISTRATION'][-2:]
    if '20'+y in years:
        com_count_year['20'+y][company['PRINCIPAL_BUSINESS_ACTIVITY_AS_PER_CIN']]+=1

counts_year=[]
for company in com_type.keys():
    counts=[]
    for count in com_count_year:
        counts.append(com_count_year[count][company])
    counts_year.append(counts)

        


import csv

maharashtra_file=open('Maharashtra.csv', encoding='unicode_escape')
maharashtra_red=csv.DictReader(maharashtra_file)
maharashtra_reader=list(maharashtra_red)

districtfile=open('districts.csv', encoding='unicode_escape')
district_reader=list(csv.DictReader(districtfile))

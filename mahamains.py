""" Importing csv module to extract data. """
import csv

# Opening file and extracting data from Maharashtra file.
maharashtra_file = open('Maharashtra.csv', encoding='unicode_escape')
maharashtra_red = csv.DictReader(maharashtra_file)
maharashtra_reader = list(maharashtra_red)
# Opening file and extracting data from District file.
districtfile = open('districts.csv', encoding='unicode_escape')
district_reader = list(csv.DictReader(districtfile))

''' Running instructions:

  python preprocess_data.py CHICAGO_CRIME_DATA.csv

'''

import csv
import lib
import sys
import sklearn.ensemble

location_desc_mapper = lib.UniquenessMapper()
primary_type_mapper = lib.UniquenessMapper()

with open(sys.argv[1], 'rb') as csvfile:
    csvreader = csv.DictReader(csvfile)
    for row in csvreader:
        try:
            time_of_day = lib.date_to_num(row['Date'])
            longitude = float(row['Longitude'])
            latitude = float(row['Latitude'])
            location_desc = location_desc_mapper.get_id(row['Location Description'])
            primary_type = primary_type_mapper.get_id(row['Primary Type'])
            id = row['ID']

            print id, time_of_day, longitude, latitude, location_desc, primary_type
        except ValueError, e:
            # Ignore missing data
            pass

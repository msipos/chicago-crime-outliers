''' To use:

  python plot_map.py   CHICAGO_CRIME_DATA.csv   SPECIFIC_CRIME_ID  MAX_NUM

'''

import csv
from jinja2 import Template
import pprint
import random
import sys

specific_id = sys.argv[2]
max_num = int(sys.argv[3])

window_size = 1.0 / 100.0

main_row = None

# Find main row
i = 0
with open(sys.argv[1], 'rb') as csvfile:
    csvreader = csv.DictReader(csvfile)
    for row in csvreader:
        i += 1
        try:
            longitude = float(row['Longitude'])
            latitude = float(row['Latitude'])
            id = row['ID']

            if id == specific_id:
                main_row = row

        except ValueError, e:
            # Ignore missing data
            pass
        if i > max_num:
            break

if main_row is None:
    raise RuntimeError('No such id: ' + specific_id)

main_longitude = float(main_row['Longitude'])
main_latitude = float(main_row['Latitude'])

# Find close-by rows
other_rows = []

i = 0
with open(sys.argv[1], 'rb') as csvfile:
    csvreader = csv.DictReader(csvfile)
    for row in csvreader:
        i += 1
        try:
            longitude = float(row['Longitude'])
            latitude = float(row['Latitude'])
            id = row['ID']
            if id == specific_id: continue

            if longitude > main_longitude - window_size and longitude < main_longitude + window_size:
                if latitude > main_latitude - window_size and latitude < main_latitude + window_size:
                    other_rows.append(row)

        except ValueError, e:
            # Ignore missing data
            pass
        if i > max_num:
            break

template = Template(open('map_template.html').read())

context = {'main_lat': main_latitude, 'main_lng': main_longitude, 'main_row': pprint.pformat(main_row).replace('\n', '<br>')}

random.shuffle(other_rows)


def row_to_template_context(row):
    return { 'lat': float(row['Latitude']), 'lng': float(row['Longitude']), 'row': pprint.pformat(row).replace('\n', '<br>') }

context['other'] = [row_to_template_context(r) for r in other_rows[:30]]

print template.render(context)

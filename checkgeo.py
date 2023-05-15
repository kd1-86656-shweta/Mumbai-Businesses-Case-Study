import json
import csv
from shapely.geometry import Point, shape

# Load the GeoJSON file
with open('boundary.geojson', 'r') as f:
    geojson_data = json.load(f)

# Check if the coordinates are in the GeoJSON file
with open('buisness_locations.csv', 'r', encoding="utf-8") as f:
    reader = csv.reader(f)
    filtered_rows = []
    # Loop through each row in the CSV file
    for row in reader:
        if (row[1]=="latitude"):
            continue
        # Get the values in the second and fourth columns
        latitude = row[1]
        longitude = row[2]
        
        point = Point(float(longitude), float(latitude))

        for feature in geojson_data['features']:
            geometry = shape(feature['geometry'])
            if geometry.contains(point):
                filtered_rows.append(row)
                break
            else:
                continue
with open('buisness_locations_geojson.csv', 'w', newline='',encoding="utf-8") as outfile:
    # create a CSV writer object
    writer = csv.writer(outfile)
    # write the filtered rows to the output CSV file
    writer.writerows(filtered_rows)
                

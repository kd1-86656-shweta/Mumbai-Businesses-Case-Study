import csv
import pandas as pd

business_industry = {}
with open('Businesses_Data.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        business_industry[row[0]] = row[2]

with open('formatted_address.csv', newline='',encoding="utf-8") as infile, open('buisness_locations.csv', mode='w', newline='',encoding="utf-8") as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)

    # Get the header row and add the new column name to it
    header = next(reader)
    header.append('Industry Type')
    writer.writerow(header)

    # Iterate over the remaining rows and add the new column value to each row
    for row in reader:
        if row[0] in business_industry.keys():
            row.append(business_industry[row[0]])
            print(row[4])
            writer.writerow(row)    
    

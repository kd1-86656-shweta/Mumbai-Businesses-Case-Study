import pandas as pd
import requests
import json
import csv

my_data =[]
df = pd.read_excel("project_industry.xlsx")

# get the column named "column_name"
column_name = "name" 
column_data = df[column_name]

# iterate over the values in the column
with open('formatted_address.csv', 'w', newline='', encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'latitude','longitude','Address'])
        
    for index, value in column_data.items():
        my_list=[]
        name = value.replace(" ", "+") + '+registered+office'
        url = 'https://maps.googleapis.com/maps/api/geocode/json?address=' + name + ',Mumbai&key=Your_Key'
        print(url)
    # Send an HTTP request to the API endpoint
        response = requests.get(url)

    # Parse the JSON response
        data = response.json()
        print(data)    
        if 'results' in data and len(data['results']) > 0:
            lat = data['results'][0]['geometry']['location']['lat']
            lng = data['results'][0]['geometry']['location']['lng']
            
            # Extract the formatted address
            formatted_address = data['results'][0]['formatted_address']
            my_list.append(value)
            print(value)
            my_list.append(lat)
            my_list.append(lng)
            my_list.append(formatted_address)
            writer.writerow(my_list)
            break
            
        

    



 

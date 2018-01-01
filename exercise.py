import geopy, pandas
from geopy.geocoders import Nominatim

nom = Nominatim(scheme="http")
test1 = nom.geocode("3995 23rd St, San Francisco, CA 94114") # returns the address of that particular value
print(test1)
df = pandas.read_csv("supermarkets.csv")
df["Address"] = df["Address"] + ", "+df["City"]+", "+df["State"]+", "+df["Country"]
df["Coordinates"] = df["Address"].apply(nom.geocode) #Applies the geocode value to all the values. No need of implementing any type of loop
print(df.Coordinates[0].latitude) #prints latitude
df["Latitude"] = df["Coordinates"].apply(lambda x:x.latitude if x!= None else None) #if condition is used to check if geocode returns None
print(df)
df["Longitude"] = df["Coordinates"].apply(lambda x:x.longitude if x!= None else None) #if condition is used to check if geocode returns None
print(df)

#Read more about lambda here -> https://www.python-course.eu/lambda.php

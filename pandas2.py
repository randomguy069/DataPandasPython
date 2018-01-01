import pandas,os

df1 = pandas.read_csv("supermarkets.csv") #read csv file
print(df1)
df2 = pandas.read_json("supermarkets.json") #read json file
print(df2)
df3 = pandas.read_excel("supermarkets.xlsx") #read excel file
print(df3)
df4 = pandas.read_csv("supermarkets-commas.txt") #read a text file where values are separated by commas
print(df4)
df5 = pandas.read_csv("supermarkets-semi-colons.txt", sep = ";") # read a text file where values are separated by semi-colons
print(df5)
df6 = pandas.read_csv("http://pythonhow.com/supermarkets.csv") #reading an online CSV file
print(df6)
df7 = pandas.read_json("http://pythonhow.com/supermarkets.json") #reading online json
print(df7)

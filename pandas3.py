import pandas

df1 = pandas.read_json("supermarkets.json")
print(df1)

df1backup = df1.set_index("Address") #setting the index as Address
print(df1backup)

df1backup.loc["735 Dolores St":"332 Hill St","Country":"ID"] # the first parameter specifies from where to where the data is required and the second part is what all portion is required
df1backup.loc["332 Hill St", "Country"] #prints USA
list(df1backup.loc[:, "Country"]) #creating a list
df1backup.iloc[1:3, 1:3] #using index
df1backup.ix[3,"Name"] #print's Ben's Shop. Print's the value related to the index
df1backup.drop("Name",1)
df1backup.drop("City",1) # 1 implies column will be deleted
df1backup.drop("332 Hill St",0) #deleting a row
print(df1backup.drop(df1backup.index[0:3],0)) #deleting 3 rows
print(df1backup.drop(df1backup.columns[0:3],1)) #deleting 2 columns
print(df1backup.index)
print(df1backup.columns)

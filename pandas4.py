import pandas

df2 = pandas.read_json("supermarkets.json")
df2["Continent"] = df2.shape[0] * ["North America"] #Adding a new Column called Continent. Shape returns number of rows and columns
df2["Continent"] = df2["Country"]+", "+"North America" #Updating the continent data

df2 = df2.set_index("Address")
#To update column it is easy but to update a row you need to create a transpose
#To Create transpose
df2_t = df2.T  #converts to transpose
print(df2_t)
#bug on this line.
df2_t["My Address"] = ["My City","My Country",10,7,"My Name","My State","My Continent"] #adding the new row
df2 = df2_t.T
print(df2)

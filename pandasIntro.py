import pandas
df1 = pandas.DataFrame([[2,4,6],[10,20,30]]) #Creating a dataframe with lists. What is a dataframe?
print(df1)
df1 = pandas.DataFrame([[2,4,6],[10,20,30]],columns=["Name","Age","Class"]) #naming the columns
print(df1)
df1 = pandas.DataFrame([[2,4,6],[10,20,30]],columns=["Name","Age","Class"],index=["First Row","Second Row"]) #Naming the rows
print(df1)
df2 = pandas.DataFrame([{"Name":"John"},{"Name":"Jane"}])
print(df2)
df2 = pandas.DataFrame([{"Name":"John","Surname":"Doe"},{"Name":"Jane","Surname":"Doe"}])
print(df2)

print(df1)
print(df1.mean()) #Used to find mean

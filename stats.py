import pandas as pnd
df = pnd.read_csv("DefaultCreds-Cheat-Sheet.csv",delimiter=",")
print(df.describe())

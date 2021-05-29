import pandas as pd
import csv
df = pd.read_csv(r"C:\Users\vedan\Desktop\Data Cleaning\data.csv")
del df["pl_orbpererr1"]
print(df.shape)
del df["pl_orbpererr2"]
print(df.shape)
del df["pl_orbsmaxerr1"]
print(df.shape)
del df["pl_bmassjerr2"]
print(df.shape)
del df["pl_radjerr1"]
print(df.shape)
del df["pl_radjerr2"]
print(df.shape)
del df["pl_denserr1"]
print(df.shape)
del df["pl_denserr2"]
print(df.shape)
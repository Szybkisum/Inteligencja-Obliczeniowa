import pandas as pd

df = pd.read_csv("iris.csv")
print(df)
print(df.values[3,2])
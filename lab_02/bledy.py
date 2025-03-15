import pandas as pd
import numpy as np

df = pd.read_csv("iris_with_errors.csv")

# a

missing = [np.nan, '-', '']
df = df.replace(missing, np.nan)
print(df.isnull().sum())

# b

float_cols = df.columns[:4]
df[float_cols] = df[float_cols].astype(float)
df[float_cols] = df[float_cols].mask((df[float_cols] <= 0) | (df[float_cols] > 15), np.nan)
df[float_cols] = df[float_cols].apply(lambda col: col.fillna(col.mean()))

# c

print(df["variety"].unique())
df["variety"] = df["variety"].str.capitalize()
df["variety"] = df["variety"].replace("Versicolour", "Versicolor")
import pandas as pd
from sklearn.preprocessing import StandardScaler, MinMaxScaler
import matplotlib.pyplot as plt

def plot(data, name: str):
    colors = {'Setosa': 'blue', 'Versicolor': 'orange', 'Virginica': 'green'}
    plt.figure(figsize=(8, 8))
    for variety, color in colors.items():
        subset = data[data['variety'] == variety]
        plt.scatter(subset['sepal.length'], subset['sepal.width'], label=variety, color=color, alpha=0.7)

    plt.xlabel('Sepal length (cm)')
    plt.ylabel('Sepal width (cm)')
    plt.title(name + ' Dataset')
    plt.legend()
    plt.savefig(name + ".png")

df = pd.read_csv("iris.csv")
plot(df, "Original")

df_z_core = df
scaler = StandardScaler()
df_z_core.iloc[:, :-1] = scaler.fit_transform(df.iloc[:, :-1])
plot(df_z_core, "Z-Core Scaled")

df_min_max = df
scaler = MinMaxScaler()
df_min_max.iloc[:, :-1] = scaler.fit_transform(df.iloc[:, :-1])
plot(df_min_max, "Min-Max Normalised")

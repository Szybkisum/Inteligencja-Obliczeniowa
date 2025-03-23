from sklearn.decomposition import PCA
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("iris.csv")

X = df.iloc[:, :-1]
y = df.columns[-1:]

pca = PCA(n_components=2).fit(X)
print(pca.explained_variance_ratio_)

pca_df = pca.transform(X)

pca_df = pd.DataFrame(data=pca_df, columns=['PC1', 'PC2'])
pca_df['variety'] = df[y]

colors = {'Setosa': 'red', 'Versicolor': 'green', 'Virginica': 'blue'}
plt.figure(figsize=(8, 6))
for variety, color in colors.items():
    subset = pca_df[pca_df['variety'] == variety]
    plt.scatter(subset['PC1'], subset['PC2'], label=variety, color=color, alpha=0.7)

plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.title('PCA on Iris Dataset')
plt.legend()
plt.savefig("pca_plot.png")

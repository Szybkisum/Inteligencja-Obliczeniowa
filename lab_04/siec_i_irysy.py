import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score

df = pd.read_csv("iris.csv")
train_inputs, test_inputs, train_classes, test_classes = train_test_split(df.iloc[:, 0:4].values, df["variety"].values, train_size=0.7, random_state=295987)

scaler = StandardScaler()

scaler.fit(train_inputs)
train_data = scaler.transform(train_inputs)
test_data = scaler.transform(test_inputs)

for size in ((2,), (3,), (3,3)):

    mlp = MLPClassifier(hidden_layer_sizes=size, max_iter=3000, random_state=295987)
    mlp.fit(train_data, train_classes)

    predictions_test = mlp.predict(test_data)
    print(accuracy_score(predictions_test, test_classes))

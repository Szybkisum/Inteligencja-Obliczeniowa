from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score

iris = load_iris()
datasets = train_test_split(iris.data, iris.target, train_size=0.7, random_state=295987)
train_data, test_data, train_target, test_target = datasets
print(train_target)

scaler = StandardScaler()

scaler.fit(train_data)
train_data = scaler.transform(train_data)
test_data = scaler.transform(test_data)

for size in ((2,), (3,), (3,3)):

    mlp = MLPClassifier(hidden_layer_sizes=size, max_iter=3000, random_state=295987)
    mlp.fit(train_data, train_target)

    predictions_test = mlp.predict(test_data)
    print(accuracy_score(predictions_test, test_target))

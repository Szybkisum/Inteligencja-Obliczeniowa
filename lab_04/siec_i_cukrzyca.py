import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, ConfusionMatrixDisplay, confusion_matrix
import matplotlib.pyplot as plt

df = pd.read_csv("diabetes.csv")
train_inputs, test_inputs, train_classes, test_classes = train_test_split(df.iloc[:, 0:8].values, df["class"].values, train_size=0.7, random_state=295987)

scaler = StandardScaler()

scaler.fit(train_inputs)
train_data = scaler.transform(train_inputs)
test_data = scaler.transform(test_inputs)

mlp = MLPClassifier(hidden_layer_sizes=(6,3), max_iter=500, random_state=295987, activation="relu")
mlp.fit(train_data, train_classes)

predictions= mlp.predict(test_data)
print(accuracy_score(predictions, test_classes))

cm = confusion_matrix(test_classes, predictions)
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=mlp.classes_)
disp.plot(cmap=plt.cm.Blues)
plt.savefig("confusion_matrix.png", dpi=300, bbox_inches='tight')
plt.close()




# custom

mlp = MLPClassifier(hidden_layer_sizes=(6,4), max_iter=500, random_state=295987, activation="relu")
mlp.fit(train_data, train_classes)

predictions= mlp.predict(test_data)
print(accuracy_score(predictions, test_classes))

cm = confusion_matrix(test_classes, predictions)
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=mlp.classes_)
disp.plot(cmap=plt.cm.Blues)
plt.savefig("confusion_matrix_custom.png", dpi=300, bbox_inches='tight')
plt.close()
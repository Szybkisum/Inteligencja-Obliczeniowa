import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
import matplotlib.pyplot as plt

df = pd.read_csv("iris.csv")
train_inputs, test_inputs, train_classes, test_classes = train_test_split(df.iloc[:, 0:4].values, df["variety"].values, train_size=0.7, random_state=295987)

def classifyNN(num):
    classifier = KNeighborsClassifier(n_neighbors=num)
    classifier.fit(train_inputs, train_classes)
    print(f"Accuracy dla {num}NN: {classifier.score(test_inputs, test_classes) * 100}")
    predictions = classifier.predict(test_inputs)
    cm = confusion_matrix(test_classes, predictions)
    disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=classifier.classes_)
    disp.plot(cmap=plt.cm.Blues)
    plt.savefig("confusion_matrix_" + str(num) + ".png", dpi=300, bbox_inches='tight')
    plt.close()

for num in [3,5,11]:
    classifyNN(num)

# Naive Bayes

NB = GaussianNB()
NB.fit(train_inputs, train_classes)
print(f"Accuracy dla NB: {NB.score(test_inputs, test_classes) * 100}")
predictions = NB.predict(test_inputs)
cm = confusion_matrix(test_classes, predictions)
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=NB.classes_)
disp.plot(cmap=plt.cm.Blues)
plt.savefig("confusion_matrix_NB", dpi=300, bbox_inches='tight')
plt.close()
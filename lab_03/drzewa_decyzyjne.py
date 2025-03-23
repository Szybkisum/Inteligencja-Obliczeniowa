import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
from sklearn import tree
import matplotlib.pyplot as plt

df = pd.read_csv("iris.csv")
train_inputs, test_inputs, train_classes, test_classes = train_test_split(df.iloc[:, 0:4].values, df["variety"].values, train_size=0.7, random_state=295987)

dtc = tree.DecisionTreeClassifier()
dtc.fit(train_inputs, train_classes)

plt.figure(figsize=(14, 10))
tree.plot_tree(dtc, 
    filled=True, 
    feature_names=df.columns[:4], 
    class_names=dtc.classes_, 
    rounded=True,
    fontsize=10,
    proportion=True)
plt.savefig("decision_tree.png", dpi=300, bbox_inches='tight')
plt.close()

print(dtc.score(test_inputs, test_classes) * 100)

predictions = dtc.predict(test_inputs)
cm = confusion_matrix(test_classes, predictions)
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=dtc.classes_)
disp.plot(cmap=plt.cm.Blues)
plt.savefig("confusion_matrix.png", dpi=300, bbox_inches='tight')
plt.close()
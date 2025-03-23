import pandas as pd
from sklearn.model_selection import train_test_split

df = pd.read_csv("iris.csv")
train_set, test_set = train_test_split(df.values, train_size=0.7, random_state=295987)

train_inputs = train_set[:, 0:4]
train_classes = train_set[:, 4]
test_inputs = test_set[:, 0:4]
test_classes = test_set[:, 4]

good_predictions = 0
len = test_set.shape[0]
train_set.sort(axis=0)
print(train_set)

def classify_iris(sl, sw, pl, pw):
    if pw <= 0.6:
        return "Setosa"
    elif pw >= 1.6:
        return "Virginica"
    else:
        return "Versicolor"

for i in range(len):
    if classify_iris(*test_inputs[i, :]) == test_classes[i]:
        good_predictions += 1

accuracy = (good_predictions / len) * 100
print(good_predictions)
print(accuracy)
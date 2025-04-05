import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from tensorflow.keras.models import Sequential # type: ignore
from tensorflow.keras.layers import Dense # type: ignore
from tensorflow.keras.utils import plot_model # type: ignore

iris = load_iris()
x = iris.data
y = iris.target

# a
# Skaluje dane, tak aby spełniały standardowy rozkład normalny N(0,1)
scaler = StandardScaler()
x_scaled = scaler.fit_transform(x)

# b
# Transformuje etykiety klas na wektory binarne
encoder = OneHotEncoder(sparse_output=False)
y_encoded = encoder.fit_transform(y.reshape(-1, 1))

x_train, x_test, y_train, y_test = train_test_split(x_scaled, y_encoded, test_size=0.3, random_state=295987)

# c
# Warstwa wejściowa posiada 4 neurony, wartość wynika z x_train.shape[1] = 4, co oznacza że dane wejściowe mają 4 kolumny
# Warstwa wyjśćiowa posiada 3 neurony, wartość wynika z y_encoded.shape[1] = 3, co oznacza że dane wyjściowe mają 3 kolumny

# d
# Użycie funkcji selu utrzymuje Test Accuracy na 97.78% ale krzywa validation accuracy lepiej się łączy z krzywą train accuracy
model = Sequential([
    Dense(64, activation="selu", input_shape=(x_train.shape[1],)),
    Dense(64, activation="selu"),
    Dense(y_encoded.shape[1], activation="softmax")
])

model.compile(optimizer="sgd", loss="categorical_crossentropy", metrics=["accuracy"])

history = model.fit(x_train, y_train, batch_size=16, epochs=100, validation_split=0.2, )

test_loss, test_accuracy = model.evaluate(x_test, y_test, verbose=0)
print(f"Test Accuracy: {test_accuracy*100:.2f}%")

plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.plot(history.history['accuracy'], label='train accuracy')
plt.plot(history.history['val_accuracy'], label='validation accuracy')
plt.title('Model accuracy')
plt.ylabel('Accuracy')
plt.xlabel('Epoch')
plt.grid(True, linestyle='--', color='grey')
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(history.history['loss'], label='train loss')
plt.plot(history.history['val_loss'], label='validation loss')
plt.title('Model loss')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.grid(True, linestyle='--', color='grey')
plt.legend()
plt.savefig("2.png")

plt.tight_layout()

model.save('iris_model.keras')
plot_model(model, to_file='model_plot.png', show_shapes=True, show_layer_names=True)
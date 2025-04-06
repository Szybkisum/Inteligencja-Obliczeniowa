import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix
from tensorflow.keras.datasets import mnist # type: ignore
from tensorflow.keras.models import Sequential # type: ignore
from tensorflow.keras.layers import Dense, Conv2D, Flatten, MaxPooling2D # type: ignore
from tensorflow.keras.utils import to_categorical # type: ignore
from tensorflow.keras.callbacks import History, ModelCheckpoint # type: ignore

# Wczytanie zbioru danych
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

# Wstępne przetwarzanie danych

# a
# Funkcja reshape w tym przypadku dodaje dodatkowy wymiar do tablicy train_images
# Funkcja to_categorical zamienia etykiety klas na wektory binarne (jak OneHotEncoder)
# Funkcja np.argmax() zwraca index o największej wartości, czyli oryginalną wartość po kodowaniu one-hot
train_images = train_images.reshape((*train_images.shape, 1)).astype('float32') / 255
test_images = test_images.reshape((*test_images.shape, 1)).astype('float32') / 255
train_labels = to_categorical(train_labels)
test_labels = to_categorical(test_labels)
original_test_labels = np.argmax(test_labels, axis=1)  # Do macierzy pomyłek

# Definicja modelu

# b
# Conv2D warstwa splotowa, gdzie każdy kwadrat 3x3 jest przepuszczany przez każdy filtr oraz stosowana jest funkcja aktywacji.
# Na wyjściu dane mają kształt (26, 26, 32)
# MaxPooling warstwa łącząca, która bierze każdy kwadrat 2x2 i zamienia na pojedynczą wartość równą najwyższej w tym kwadracie.
# Na wyjściu dane mają kształt (13, 13, 32)
# Flatten spłaszcza dane 13 * 13 * 32 = (5408,)
# Dense warstwa w pełni połączona z 64 neuronami. Każda wartość jest modyfikowana o wagę i na wyjściu przechodzi przez funkcję aktywacji.
# Na wyjściu są już tylko 64 wartości
# Dense warstwa wyjściowa różniąca się ilością neuronów (10) oraz funkcją aktywacji. 
# Ostatecznie otrzymujemy 10 wartości z przedziału [0,1] sumujące się do 1 (prawdopodobieństwo)
model = Sequential([
    Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
    MaxPooling2D((2, 2)),
    Flatten(),
    Dense(64, activation='relu'),
    Dense(10, activation='softmax')
])

# Kompilacja modelu
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Trenowanie modelu
history = History()
# e
checkpoint = ModelCheckpoint(
    filepath='images_model.keras',
    monitor='val_accuracy',
    save_best_only=True,
    save_weights_only=False,
    mode='max', 
    verbose=0
)
model.fit(train_images, train_labels, epochs=5, batch_size=64, validation_split=0.2, callbacks=[history, checkpoint])

# Ewaluacja na zbiorze testowym
test_loss, test_acc = model.evaluate(test_images, test_labels)
print(f"Test accuracy: {test_acc:.4f}")

# Przewidywanie etykiet dla danych testowych
predictions = model.predict(test_images)
predicted_labels = np.argmax(predictions, axis=1)

# Macierz pomyłek
cm = confusion_matrix(original_test_labels, predicted_labels)
plt.figure(figsize=(10, 7))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
plt.xlabel('Predicted')
plt.ylabel('True')
plt.title('Confusion Matrix')
plt.tight_layout()
plt.savefig('confusion_matrix.png')
plt.close()

# Wykresy dokładności i błędu
plt.figure(figsize=(10, 5))

# Dokładność
plt.subplot(1, 2, 1)
plt.plot(history.history['accuracy'], label='Training Accuracy')
plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.grid(True, linestyle='--', color='grey')
plt.legend()

# Błąd
plt.subplot(1, 2, 2)
plt.plot(history.history['loss'], label='Training Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.grid(True, linestyle='--', color='grey')
plt.legend()

plt.tight_layout()
plt.savefig('training_metrics.png')
plt.close()

# Wyświetlenie 25 przykładowych obrazów z przewidywanymi etykietami
plt.figure(figsize=(10, 10))
for i in range(25):
    plt.subplot(5, 5, i + 1)
    plt.xticks([])
    plt.yticks([])
    plt.grid(False)
    plt.imshow(test_images[i].reshape(28, 28), cmap=plt.cm.binary)
    plt.xlabel(predicted_labels[i])
plt.tight_layout()
plt.savefig('predicted_samples.png')
plt.close()

# c
# Program najczęściej błędnie rozpoznaje 2 jako 7 lub 1 oraz 8 jako 3 lub 9

# d
# Powidziałbym że mamy przypadek przeuczenia się, ponieważ trafność dla zestawu walidacji spada a strata rośnie
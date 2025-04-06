import os
import numpy as np
from keras.preprocessing.image import load_img, img_to_array # type:ignore
from keras.callbacks import EarlyStopping, ReduceLROnPlateau # type: ignore
from keras.utils import to_categorical # type:ignore
from keras.models import Sequential # type:ignore
from keras.layers import Conv2D, MaxPooling2D, Dropout, Flatten, Dense, BatchNormalization # type:ignore
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

IMG_SIZE=(40, 40)

images = []
labels = []

for filename in os.listdir("dogs-cats-mini"):
	label = 1 if "dog" in filename else 0
	img = img_to_array(load_img("dogs-cats-mini/" + filename, target_size=IMG_SIZE))
	images.append(np.array(img))
	labels.append(label)

images = np.asarray(images) / 255.0
labels = to_categorical(np.asarray(labels))

train_images, test_images, train_labels, test_labels = train_test_split(images, labels, test_size=0.2, random_state=295987)
original_test_labels = np.argmax(test_labels, axis=1)

model = Sequential([
    Conv2D(32, (3,3), activation="relu", input_shape=(*IMG_SIZE, 3)),
    BatchNormalization(),
    MaxPooling2D((2,2)),
    Dropout(0.25),
    Conv2D(64, (3,3), activation="relu"),
    BatchNormalization(),
    MaxPooling2D((2,2)),
    Dropout(0.25),
    Conv2D(128, (3,3), activation="relu"),
    BatchNormalization(),
    MaxPooling2D((2,2)),
    Dropout(0.25),
    Flatten(),
    Dense(512, activation="relu"),
    BatchNormalization(),
    Dropout(0.5),
    Dense(2, activation="softmax")
])

model.compile(loss='categorical_crossentropy', optimizer='rmsprop', metrics=['accuracy'])

early_stop = EarlyStopping(patience=10)
learning_rate_reduction = ReduceLROnPlateau(
    monitor='val_acc', 
	patience=2, 
	verbose=1, 
    factor=0.5, 
    min_lr=0.00001
)

history = model.fit(
    train_images,
	train_labels,
    validation_split=0.2,
    epochs=5,
    batch_size=64,
    callbacks=[early_stop, learning_rate_reduction]
)

test_loss, test_acc = model.evaluate(test_images, test_labels)
print(f"Test accuracy: {test_acc:.4f}")

# Przewidywanie etykiet dla danych testowych
predictions = model.predict(test_images)
predicted_labels = np.argmax(predictions, axis=1)
label_names = {0: 'cat', 1: 'dog'}


cm = confusion_matrix(original_test_labels, predicted_labels)
plt.figure(figsize=(10, 7))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
            xticklabels=[label_names[i] for i in range(2)],
            yticklabels=[label_names[i] for i in range(2)])
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
    plt.imshow(test_images[i], cmap=plt.cm.binary)
    plt.xlabel(label_names[predicted_labels[i]])
plt.tight_layout()
plt.savefig('predicted_samples.png')
plt.close()
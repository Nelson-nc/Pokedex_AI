import numpy as np
from Pokemon_Datasets import Pokemon_dataset
from sklearn.model_selection import train_test_split


# Load Dataset
pokemon_dataset = Pokemon_dataset()

data = np.array(pokemon_dataset.data)             # X
data = data / 255.0                               # Normalize from (0, 255) to (0, 1)

labels = np.array(pokemon_dataset.labels)         # y

print("\nFinished processing and loading all images/data!")


# Split Datas
train_data, test_data, train_labels, test_labels = train_test_split(data, labels, test_size=0.2, random_state=42)

print(f"Total images found: {len(data)}")
print(f"Images for training: {len(train_data)}")
print(f"Images for testing: {len(test_data)}")

print(f"Shape of training data: {train_data.shape}")
print(f"Shape of testing data: {test_data.shape}")


# TRAIN MODEL
import keras
from keras import layers


# NN Brain
input_shape = (pokemon_dataset.IMAGE_SIZE[0], pokemon_dataset.IMAGE_SIZE[1], 3)

model = keras.Sequential([
    # First
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=input_shape),
    layers.MaxPooling2D((2, 2)),

    # Second
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),

    # Third
    layers.Conv2D(128, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),

    # Flatten
    layers.Flatten(),

    # Combining patterns First
    layers.Dense(128, activation='relu'),

    # Output
    layers.Dense(len(pokemon_dataset.pokemon_names), activation='softmax'),
])

# Learning
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
model.summary()

# Train
trained = model.fit(train_data, train_labels, epochs=10, batch_size=32)

# Losses and Accuracy
loss, accuracy = model.evaluate(test_data, test_labels, verbose='0')

print("\n\n TENSORFLOW PART \n\n")
print(f"Accuracy: {accuracy*100:.2f}%")
print(f"Loss: {loss*100:.4f}%")

# Predict
predictions = model.predict(test_data[:5])

for i, pred in enumerate(predictions):
    pokemon_pindex = np.argmax(pred)
    pokemon_pname = pokemon_dataset.pokemon_names[pokemon_pindex]

    pokemon_name = pokemon_dataset.pokemon_names[test_labels[:5][i]]

    print("\n Prediction \n")
    print(f"  - Image {i+1}:")
    print(f"    Pokedex predicted: {pokemon_pname} (True: {pokemon_name})")
    print(f"    Prediction probabilities: {pred}") # Show how confident it was

model.save("pokedex.keras")
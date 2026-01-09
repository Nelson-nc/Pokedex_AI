import sys
import numpy as np
from tensorflow import keras
from PIL import Image


IMAGE_SIZE = (64, 64)
MODEL_PATH = "pokedex.keras"
POKEMON_NAMES = ["bulbasaur", "charmander", "squirtle"]

if len(sys.argv) < 2:
    print("Error: Please provide the path to an image.")
    print("Usage: python kanto3_pokedex.py 'path/to/your/image.jpg' ")
    sys.exit(1)

image_ppath = sys.argv[1]

try:
    # Load our trained neural network
    print("Loading model...")
    model = keras.models.load_model(MODEL_PATH)

    # Open, resize, convert, expand dimentions and normalize image
    print("Opening Image...")
    image = Image.open(image_ppath)
    image = image.resize(IMAGE_SIZE)
    image_array = np.array(image)
    image_array = np.expand_dims(image_array, axis=0)
    image_array = image_array / 255.0

    # Make Predictions
    print("Predicting...")
    prediction = model.predict(image_array)

    pokemon_pindex = np.argmax(prediction)
    pokemon_pname = POKEMON_NAMES[pokemon_pindex]
    confidence = np.max(prediction)
    print("DONE")

    # Show Result
    print("\n--- Pokedex Result ---")
    print(f"Pokemon: {pokemon_pname.capitalize()}!")
    print(f"Confidence: {confidence*100:.2f}%")
    print("----------------------")

# Image Not Found
except FileNotFoundError:
    print(f"Error: Cannot find the image at '{image_ppath}'")
    print("Please check the file path and try again.")

# Model Not Found
except Exception as e:
    print(f"An error occurred: {e}")
    print(f"Train the data first? Please run 'pokedex_training.py' first to create '{MODEL_PATH}'.")

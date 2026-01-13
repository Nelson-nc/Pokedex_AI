import os
import numpy as np 
from PIL import Image

class Pokemon_dataset:
    def __init__(self) -> None:
        self.data = []
        self.labels = []

        self.DATASET_PATH = 'Pokemon_Datasets/datasets'
        self.IMAGE_SIZE = (64, 64)

        self.pokemon_names = os.listdir(self.DATASET_PATH)

        self.load_dataset()


    def load_dataset(self):

        for i, pokemon_name in enumerate(self.pokemon_names):
            label = i       # The label for the pokemon (0 = bulbasaur, 1 = charmander, 2 = squitle)
            pokemon_folder = os.path.join(self.DATASET_PATH, pokemon_name)

            for image_name in os.listdir(pokemon_folder):
                if not image_name.lower().endswith(('.png', '.jpg', '.jpeg')):  # Only allow .png, .jpeg and .jpg
                    continue

                image_path = os.path.join(pokemon_folder, image_name)
                try:
                    image = Image.open(image_path)          # Open the image with pillow
                    image = image.resize(self.IMAGE_SIZE)   # Resize the image to our IMAGE_SIZE
                    image_array = np.array(image)           # Convert the image to a numpy array

                    if len(image_array.shape) < 3:          # Skip grayscale image
                        print(f"! Skipped the grayscale image: {image_name}")
                        continue

                    # Add the prepared image and its Label to our lists
                    self.data.append(image_array)
                    self.labels.append(label)

                except Exception as e:
                    print(f"! Error processing image {image_name}: {e}")

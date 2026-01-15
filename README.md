![pokedex banner](res/Pokedex.png)

[![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=fff)](#)
[![Selenium](https://img.shields.io/badge/Selenium-43B02A?logo=selenium&logoColor=fff)](#)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-ff8f00?logo=tensorflow&logoColor=white)](#)
[![Keras](https://img.shields.io/badge/Keras-D00000?logo=keras&logoColor=fff)](#)
[![NumPy](https://img.shields.io/badge/NumPy-4DABCF?logo=numpy&logoColor=fff)](#)
[![Scikit-learn](https://img.shields.io/badge/-scikit--learn-%23F7931E?logo=scikit-learn&logoColor=white)](#)

A simple Pokedex app that predict the pokemon name based on the image.

<!-- ![pokedex](res/pokedex_image.webp) -->
it doesn't really look like this

## Usage
Get the dataset for training
```sh
cd Pokemon_Datasets
python dataset_scraper.py
```
Training the model, it should generate a pokedex.keras
```sh
cd ..
python pokedex_training.py
```
You can run it in the terminal
```sh
python kanto3_pokedex.py "image path"
```
or run a GUI made with Tkinter
```sh
python pokedex_gui.py
```

## Installation/Setup
<p>First you must have [Python](https://www.python.org) installed</p>
then install the dependences with pip for windows or pip3 for unix

```sh
pip install selenium
pip install tensorflow
pip install keras
pip install pillow
pip install opencv_python
```
<p>then make sure your project directory is setup correctly.</p>

- Pokemon_Datasets
    - datasets
        - bulbasaur
        - charmander
        - squirtle

## Future Ideas
- add script to retrive pokemon name from __pokeapi__ and automatically create folders for the amount of pokemon you want.
- fix the pokemon_gui UI (the ui doesn't look good).
- update the dataset_scraper.py to add one of each image to res/photos

## How to contribute
- fork and clone repository
- create new branch -> git checkout -b branch_name
- make changes and test
- push and submit a pull request with a good description.

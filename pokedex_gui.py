import os
import cv2
import tkinter as tk
from PIL import Image, ImageTk
from kanto3_pokedex import Pokedex


class Pokedex_Gui:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Pokedex")
        self.root.config(bg='red')
        self.imshow = True

        self.imageLabel = tk.Label(self.root, bg='gray')
        self.imageLabel.pack(pady=20)

        self.pkmLabel = tk.Label(self.root, bg='red', text='')
        self.pkmLabel.pack(pady=20)

        self.button = tk.Button(self.root, bg='blue', text='Take pic', command=self.take_picture)
        self.button.pack(pady=20)

        self.button = tk.Button(self.root, bg='blue', text='C', command=self.clear)
        self.button.pack(pady=20)

        self.capture = cv2.VideoCapture(0)

    def take_picture(self):
        imgPath = 'res/photos'
        if not os.path.exists(imgPath):
            os.makedirs(imgPath)

        _, frame = self.capture.read()
        filename = os.path.join(imgPath, "pokemon.png")
        cv2.imwrite(filename, frame)

        pokedex = Pokedex(filename)
        pokemonName, confidence = pokedex.get_pokemon()
        os.remove(filename)
        self.imshow = False

        pokemonImg = os.path.join(imgPath, f"{pokemonName}.png")
        image = Image.open(pokemonImg) .resize((400,200))
        imagetk = ImageTk.PhotoImage(image=image, size=(400,260))
        self.imageLabel.config(width=400, height=260, anchor=tk.NW, image=imagetk)
        self.imageLabel.imagetk = imagetk # type: ignore
        self.pkmLabel.config(text=f"{pokemonName}".title())

    def clear(self):
        self.imshow = True
        self.pkmLabel.config(text='')

    def update(self):
        ret, frame = self.capture.read()
        if self.imshow:
            frame = cv2.resize(frame, (400,260))
            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image = Image.fromarray(image)
            imagetk = ImageTk.PhotoImage(image=image)

            self.imageLabel.config(width=400, height=260, anchor=tk.NW, image=imagetk)
            self.imageLabel.imagetk = imagetk # type: ignore
    
        self.root.after(10, self.update)

    def run(self):
        self.update()
        self.root.mainloop()

 
if __name__ == '__main__':
    gui = Pokedex_Gui()
    gui.run()
#hacemos los imports necesarios
import tkinter as tk
import random
from tkinter import messagebox
import data as d

class Mole(d.game_window):
    def __init__(self, root, root2):
        super().__init__(root,root2)
        self.root.title("Mole") #título
        self.root.geometry("725x365") #tamaño
        self.root.iconbitmap("res\logo.ico") #logo
        self.background_image = tk.PhotoImage(file=r"res\bgCT.png") #imagen de fondo
        self.etiqueta = tk.Label(self.frame, image=self.background_image)
        self.etiqueta.image = self.background_image
        self.etiqueta.grid(row=0, column=0, rowspan=7, columnspan=5, sticky="nsew")
        #Se crean los textos para el frame
        self.pattern_label = tk.Label(self.frame, text="Mole Smash", font=("Arial", 24),anchor="center")
        self.pattern_label.grid(column=0,row=0,columnspan=4,pady=10)
        self.levelLabel=tk.Label(self.frame,text=("Level: "+str(self.abs_lvl)),font=("Arial", 12))
        self.levelLabel.grid(column=0,row=1,pady=10)
        self.pointsLabel=tk.Label(self.frame,text="Points: "+str(self.points),font=("Arial", 12))
        self.pointsLabel.grid(column=3,row=1,pady=10)
        #se crean los botones iniciales
        self.start_button = tk.Button(self.frame, text="Start", command=self.start_game)
        self.start_button.grid(column=0,row=5,padx=10,pady=10,columnspan=1)
        self.reset_button = tk.Button(self.frame, text="Reset", command=self.reset_game)
        self.reset_button.grid(column=3,row=5,padx=10,pady=10)
        self.boton_cerrar = tk.Button(self.frame, text="Back To Menu", command=self.cerrar_segunda_ventana)
        self.boton_cerrar.grid(column=0,row=6,padx=10,pady=10,columnspan=4)
        self.root.after(100,self.mostrar_instrucciones) #luego de 100 milis se muestra la ventana emergente de las instrucciones
        
    def mostrar_instrucciones(self):
        instrucciones = "Bienvenido a Mole Smash\n\nInstrucciones:\n\n1. Presiona Start para iniciar el juego\n2. Se mostrarán botones\n3. Presiona los botones rojos tan rápido cómo puedas!"
        messagebox.showinfo("Instrucciones", instrucciones)

    def reset_game(self):
        self.play_music()
        self.abs_lvl=1
        self.points=0
        self.levelLabel.config(text=("Level: "+str(self.abs_lvl)))
        self.pointsLabel.config(text="Points: "+str(self.points))
        self.pattern_label.config(text="Color Tiles")
        self.start_button.config(state=tk.NORMAL)
        self.reset_button.config(state=tk.NORMAL)
        self.game_active = False

    def add_points(self, button):
        if button.cget("bg") == "#ff0000":
            self.points += 10
            self.pointsLabel.config(text="Points: "+str(self.points))
    def hit_fake(self):
        print("hi")

    def change_level(self):
        if self.points <=100:
            self.abs_lvl = 1
        elif self.points <= 250:
            self.abs_lvl = 2
        elif self.points <= 500:
            self.abs_lvl = 3
        else:
            self.abs_lvl = 4
        return self.abs_lvl
    
    def change_button(self):
        button_list = [0,1,2,3]

        red_button = random.choice(button_list)
        button_list.remove(red_button)
        blue_button = random.choice(button_list)

        if self.abs_lvl == 4:
            button_list.remove(blue_button)
            green_button = random.choice(button_list)
            return red_button, blue_button, green_button
        else:
            return red_button, blue_button, 5

    # Create a function to change the button color
    def change_color(self):

        __level = self.change_level()
        __time = 0
        
        redHit, blueFake, greeFake = self.change_button()

        # Reset the color of all buttons to gray
        for button in buttons:
            button.configure(bg="#999999")

        if __level == 1:
            __time = 1200
        elif __level == 2:
            __time = 800
        elif __level == 3:
            __time = 600
            blue_fake = buttons[blueFake]
            # Change the color of the random button to red
            blue_fake.configure(bg="#0000ff", command=lambda: self.hit_fake())
        else:
            blue_fake = buttons[blueFake]
            # Change the color of the random button to red
            blue_fake.configure(bg="#0000ff", command=lambda: self.hit_fake())
            green_fake = buttons[greeFake]
            green_fake.configure(bg="#008000", command=lambda: self.hit_fake())
            __time = 400

        random_button = buttons[redHit]
        # Change the color of the random button to red
        random_button.configure(bg="#ff0000", command=lambda: self.add_points(random_button))

        self.root.after(__time, self.change_color)

    # Create a function to start the game
    def start_game(self):
        self.play_music()
        self.start_button.config(state=tk.DISABLED)
        self.reset_button.config(state=tk.DISABLED)
        self.game_active = True
        # Create 3 buttons
        global buttons
        buttons = [tk.Button(self.frame, width=10, height=5, bg="#999999") for _ in range(4)]

        m = 0
        for button in buttons:
            button.grid(column=m, row=2, padx=10)
            m +=1

        # Start the color changing process
        self.change_color()
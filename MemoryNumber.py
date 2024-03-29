from tkinter import messagebox as ms
import gameWindow as gw
import tkinter as tk
import random

class MemoryNumber(gw.game_window):
    def __init__(self, root, root2):
        super().__init__(root,root2)

        self.root.title("Memory") #título
        self.root.geometry("725x365") #tamaño
        self.root.iconbitmap("res\logo.ico") #logo
        self.background_image = tk.PhotoImage(file=r"res\bgCT.png") #imagen de fondo
        self.etiqueta = tk.Label(self.frame, image=self.background_image)
        self.etiqueta.image = self.background_image
        self.etiqueta.grid(row=0, column=0, rowspan=7, columnspan=5, sticky="nsew")

        #Se crean los textos para el frame
        """self.pattern_label = tk.Label(self.frame, text="Memory Number", font=("Arial", 24),anchor="center")
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
        self.boton_cerrar.grid(column=0,row=6,padx=10,pady=10,columnspan=4)"""
        self.root.after(100,self.mostrar_instrucciones) #luego de 100 milis se muestra la ventana emergente de las instrucciones

        # Create the button grid
        self.buttons = []
        for row in range(5):
            row_buttons = []
            for col in range(5):
                button = tk.Button(self.root, bg="white", command=lambda r=row, c=col: self.button_click(r, c), width=5, height=3)
                button.grid(row=row+1, column=col, padx=5, pady=5)
                row_buttons.append(button)
            self.buttons.append(row_buttons)

        # Initialize the game
        self.init_game()

    def init_game(self):
        self.play_music()

        self.start_button.config(state=tk.DISABLED)
        self.reset_button.config(state=tk.DISABLED)

        self.game_active = True

        # Generate random numbers for the buttons
        numbers = random.sample(range(1, 10), 9)
        self.button_values = {}
        
        for _, number in enumerate(numbers):
            
            row = random.randint(0,4)
            col = random.randint(0,4)
            
            while self.buttons[row][col] in self.button_values:
                row = random.randint(0,4)
                col = random.randint(0,4)

            self.button_values[self.buttons[row][col]] = number

        # Show the numbers for 3 seconds
        self.show_numbers()

    def show_numbers(self):

        for button in self.buttons:
            for b in button:
                b.config(state='disabled')

        for button, number in self.button_values.items():
            button.config(text=number)
        self.root.after(3000, self.hide_numbers)

    def hide_numbers(self):

        for button in self.button_values.keys():
            button.config(text="")

        for button in self.buttons:
            for b in button:
                b.config(state='normal')

    def button_click(self, row, col):

        button = self.buttons[row][col]
        if button in self.button_values:
            # Check if the clicked button has the next expected number
            if self.button_values[button] == self.next_number:
                self.next_number += 1
                button.config(bg="green")

                # Check if the game is over
                if self.next_number == 10:
                    self.game_over("You win!")
            else:
                self.next_number=1
                self.game_over("Wrong order!")

    def game_over(self, message):
        ms.showinfo("Game Over", message)

        for row in self.buttons:
            for button in row:
                button.config(bg="white")
        self.init_game()

    def start(self):
        self.next_number = 1
        self.root.mainloop()
        







    def mostrar_instrucciones(self):
        instrucciones = "Bienvenido a Mole Smash\n\nInstrucciones:\n\n1. Presiona Start para iniciar el juego\n2. Se mostrarán botones\n3. Presiona los botones rojos tan rápido cómo puedas!"
        ms.showinfo("Instrucciones", instrucciones)

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
import tkinter as tk
import random
import time
from tkinter import messagebox

import pygame
import data as d

class ColorTiles:

    points=0

    def __init__(self, root,root2):
        self.root = root
        self.mainRoot=root2
        self.frame=tk.Frame(root)
        self.frame.pack(fill="both",expand=True)
        self.frame.config(bg="black")
        self.root.title("Color Tiles")
        self.root.geometry("725x365")
        self.root.iconbitmap("res\logo.ico")
        self.background_image = tk.PhotoImage(file=r"res\bgCT.png")
        self.etiqueta = tk.Label(self.frame, image=self.background_image)
        self.etiqueta.image = self.background_image  # Evitar que la imagen sea eliminada por la recolección de basura
        self.etiqueta.grid(row=0, column=0, rowspan=7, columnspan=5, sticky="nsew")
        self.colors = ["red", "blue", "green", "yellow"]
        self.pattern = []
        self.user_input = []
        self.sequence_length = 3
        self.display_time = 1
        self.user_time = 7
        self.game_active = False
        self.number_buttons = []
        self.idx=0
        self.counter=0
        self.lvl=0
        self.abs_lvl=1
        self.points=0
        self.pattern_label = tk.Label(self.frame, text="Color Tiles", font=("Arial", 24),anchor="center")
        self.pattern_label.grid(column=0,row=0,columnspan=4,pady=10)
        self.levelLabel=tk.Label(self.frame,text=("Level: "+str(self.abs_lvl)),font=("Arial", 12))
        self.levelLabel.grid(column=0,row=1,pady=10)
        self.pointsLabel=tk.Label(self.frame,text="Points: "+str(self.points),font=("Arial", 12))
        self.pointsLabel.grid(column=3,row=1,pady=10)
        self.start_button = tk.Button(self.frame, text="Start", command=self.start_game)
        self.start_button.grid(column=0,row=5,padx=10,pady=10,columnspan=1)
        self.reset_button = tk.Button(self.frame, text="Reset", command=self.reset_game)
        self.reset_button.grid(column=3,row=5,padx=10,pady=10)
        self.boton_cerrar = tk.Button(self.frame, text="Back To Menu", command=self.cerrar_segunda_ventana)
        self.boton_cerrar.grid(column=0,row=6,padx=10,pady=10,columnspan=4)
        self.root.after(100,self.mostrar_instrucciones)

    def cerrar_segunda_ventana(self):
        self.set_points()
        pygame.mixer.music.stop()
        self.play_musicMain()
        self.root.destroy()
        self.mainRoot.deiconify()

    def mostrar_instrucciones(self):
        instrucciones = "Bienvenido a Color Tiles\n\nInstrucciones:\n\n1. Presiona Start para iniciar el juego\n2. Se mostrará un patrón de colores a memorizar\n3. Al cambiar la instrucción a Your Turn, puedes repetir el patrón usando los botones\n4. ¡Continúa memorizando!"
        messagebox.showinfo("Instrucciones", instrucciones)
    
    def play_music(self):
        pygame.mixer.init()
        pygame.mixer.music.load("res\innerLoop.mp3")
        pygame.mixer.music.play(-1)
    
    def gameOver(self):
        pygame.mixer.music.stop()
        pygame.mixer.music.load("res\GO.mp3")
        pygame.mixer.music.play(1)
    
    def play_musicMain(self):
        pygame.mixer.init()
        pygame.mixer.music.load("res\mainLoop.mp3")
        pygame.mixer.music.play(-1)

    def set_points(self):
        global points
        points = self.points
        d.userPoints=points

    def reset_game(self):
        self.play_music()
        self.pattern = []
        self.user_input = []
        self.sequence_length = 3
        self.display_time = 1
        self.user_time = 7
        self.idx=0
        self.counter=0
        self.abs_lvl=1
        self.points=0
        self.levelLabel.config(text=("Level: "+str(self.abs_lvl)))
        self.pointsLabel.config(text="Points: "+str(self.points))
        self.pattern_label.config(text="Color Tiles")
        self.start_button.config(state=tk.NORMAL)
        self.reset_button.config(state=tk.NORMAL)
        self.game_active = False
        self.reset_number_buttons()
        for button in self.number_buttons:
            button.destroy()
        self.number_buttons = []
    
    def reset_number_buttons(self):
        for button in self.number_buttons:
            button.destroy()
        self.number_buttons = []

    def start_game(self):
        self.play_music()
        self.start_button.config(state=tk.DISABLED)
        self.reset_button.config(state=tk.DISABLED)
        self.game_active = True
        i=0
        for color in self.colors:
            button = tk.Button(self.frame, text=color, bg=color, height=5,width=9,command=lambda color=color: self.check_input(color))
            button.grid(column=i,row=2,padx=10)
            self.number_buttons.append(button)
            i+=1
        self.play_pattern()

    def play_pattern(self):
        self.user_input = []
        self.pattern = []
        self.pattern = [random.choice(self.colors) for _ in range(self.sequence_length)]
        for button in self.number_buttons:
            button.config(state=tk.DISABLED)
        self.levelLabel.config(text=("Level: "+str(self.abs_lvl)))
        self.pointsLabel.config(text="Points: "+str(self.points))
        self.display_pattern()
        self.pattern_label.config(text="Your Turn")
        self.root.after(self.display_time * 1000, self.get_user_input)

    def display_pattern(self):
        for color in self.pattern:
            self.pattern_label.config(text=color)
            self.pattern_label.config(bg=color)
            self.root.update()
            time.sleep(1)
            self.pattern_label.config(bg="white")
            self.root.update()
            time.sleep(0.5)

    def get_user_input(self):
        if not self.game_active:
            return
        for button in self.number_buttons:
            button.config(state=tk.NORMAL)
        self.root.after(self.user_time*1000, self.check_user_pattern)
    
    def check_input(self, number):
        self.user_input.append(number)

    def correcto(self):
        self.pattern_label.config(text="Correct!")
        self.root.after(1000, self.play_pattern)

    def check_user_pattern(self):
        if not self.game_active:
            return
        for i in range(len(self.pattern)):
            self.counter+=1
            if len(self.user_input)==len(self.pattern):
                if self.user_input[i]==self.pattern[i]:
                    self.idx+=1
            else:
                self.set_points()
                self.gameOver()
                self.pattern_label.config(text="Game Over")
                self.reset_button.config(state=tk.NORMAL)
                self.game_active = False
        if self.counter==self.idx:
            self.lvl+=1
            if self.lvl==3:
                self.sequence_length += 1
                self.user_time -= 1
                self.lvl=0
                self.abs_lvl+=1
            if self.user_time<5:
                self.user_time=5
            if self.abs_lvl<3:
                self.points+=10
            elif self.abs_lvl<6:
                self.points+=15
            else:
                self.points+=25
            self.correcto()
        else:
            self.set_points()
            self.gameOver()
            self.pattern_label.config(text="Game Over")
            self.reset_button.config(state=tk.NORMAL)
            self.game_active = False
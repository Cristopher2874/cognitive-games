import tkinter as tk
import data as d
import pygame

class game_window:

    points = 0

    def __init__(self, root,root2):
        self.root = root #creamos ambas raíces
        self.mainRoot=root2
        self.frame=tk.Frame(root) #creamos el frame
        self.frame.pack(fill="both",expand=True) #lo ponemos en la ventana
        self.frame.config(bg="black") #fondo negro
        self.game_active = False #variable para saber si el usuario ya perdió
        self.lvl=0 #contador del nivel
        self.abs_lvl=1 #contador del nivel para el usuario
        self.points=0 #puntos
    
    def cerrar_segunda_ventana(self):
        self.set_points()
        pygame.mixer.music.stop()
        self.play_musicMain()
        self.root.destroy()
        self.mainRoot.deiconify()
    
    def gameOver(self):
        pygame.mixer.music.stop()
        pygame.mixer.music.load("res\GO.mp3")
        pygame.mixer.music.play(1)
    
    def play_musicMain(self):
        pygame.mixer.init()
        pygame.mixer.music.load("res\mainLoop.mp3")
        pygame.mixer.music.play(-1)
    
    def play_music(self):
        pygame.mixer.init()
        pygame.mixer.music.load("res\innerLoop.mp3")
        pygame.mixer.music.play(-1)

    def set_points(self):
        global points
        points = self.points
        d.userPoints=points

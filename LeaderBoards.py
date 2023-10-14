from tkinter import *

import pygame

class leaderboard:

    points=0

    def __init__(self,root,root2,lista):
        self.root = root
        self.mainRoot=root2
        self.frame=Frame(root)
        self.frame.pack(fill="both",expand=True)
        self.frame.config(bg="black")
        self.root.title("Top Scores")
        self.root.geometry("400x365")
        self.root.iconbitmap("res\logo.ico")
        self.background_image = PhotoImage(file=r"res\bg.png")
        self.etiqueta = Label(self.frame, image=self.background_image)
        self.etiqueta.image = self.background_image  # Evitar que la imagen sea eliminada por la recolección de basura
        self.etiqueta.grid(row=0, column=0, rowspan=7, columnspan=5, sticky="nsew")
        self.boton_cerrar = Button(self.frame, text="Back To Menu", command=self.cerrar_segunda_ventana)
        self.boton_cerrar.grid(column=0,row=5,padx=10,pady=10)
        self.userList=lista
        self.titulo = Label(self.frame, text="Best Scores:", font=("Arial", 24),bg="white",fg="blue")
        self.titulo.grid(column=0,row=0,padx=10,pady=10)
        self.renglon = "\n".join([f"{fila[0]}:........................................{fila[1]}" for fila in self.userList])
        self.puntajes=Label(self.frame,text=self.renglon, font=("Arial", 16))
        self.puntajes.grid(column=0,row=1,padx=10,pady=10)
        self.play_music()

    def cerrar_segunda_ventana(self):
        pygame.mixer.music.stop()
        self.play_musicMain()
        self.root.destroy()
        self.mainRoot.deiconify()
    
    def play_music(self):
        pygame.mixer.init()
        pygame.mixer.music.load("res\Lead.mp3")
        pygame.mixer.music.play(-1)

    def play_musicMain(self):
        pygame.mixer.init()
        pygame.mixer.music.load("res\mainLoop.mp3")
        pygame.mixer.music.play(-1)
    
        
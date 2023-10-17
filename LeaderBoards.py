# cheeck :D

from tkinter import * #importamos tkinter
import pygame #importamos pygame

class leaderboard: #creamos una clase que se llama leaderboard

    points=0 #creamos una variable que se llama puntos

    def __init__(self,root,root2,lista): #creamos un constructor que recibe dos ventanas y una lista como argumentos
        self.root = root #igualamos la ventana que recibimos a la que tenemos en la clase
        self.mainRoot=root2 #guardamos la segunda ventana como la principal para poder regresar
        self.frame=Frame(root) #creamos un frame en la segunda ventana
        self.frame.pack(fill="both",expand=True) #lo ponemos en la ventana
        self.frame.config(bg="black") #fondo negro
        self.root.title("Top Scores") #le ponemos título
        self.root.geometry("505x405") #le damos tamaño a la ventana
        self.root.iconbitmap("res\logo.ico") #ponemos el logo
        self.background_image = PhotoImage(file=r"res\bgL.png") #cargamos la imagen de fondo
        self.etiqueta = Label(self.frame, image=self.background_image) #creamos la imagen en el frame
        self.etiqueta.image = self.background_image  #refrescamos la imagen para que no se borre
        self.etiqueta.grid(row=0, column=0, rowspan=7, columnspan=5, sticky="nsew")
        self.boton_cerrar = Button(self.frame, text="Back To Menu", command=self.cerrar_segunda_ventana) #boton para cerrar ventana 2
        self.boton_cerrar.grid(column=0,row=5,padx=10,pady=10)
        self.userList=lista #guardamos la lista en una clase
        self.titulo = Label(self.frame, text="Best Scores:", font=("Arial", 24),bg="white",fg="blue") #ponemos el título
        self.titulo.grid(column=0,row=0,padx=10,pady=10)
        self.renglon = "\n".join([f"{fila[0]}:\t\t{fila[1]}" for fila in self.userList]) #hacemos la lista de puntajes con la matriz
        self.puntajes=Label(self.frame,text=self.renglon, font=("Arial", 16))
        self.puntajes.grid(column=0,row=1,padx=10,pady=10)
        self.play_music() #reproducimos la música

    def cerrar_segunda_ventana(self): #función para cerrar la ventana y regresar a la principal
        pygame.mixer.music.stop()
        self.play_musicMain()
        self.root.destroy()
        self.mainRoot.deiconify()
    
    def play_music(self): #función para poner la música de la pantalla
        pygame.mixer.init()
        pygame.mixer.music.load("res\Lead.mp3")
        pygame.mixer.music.play(-1)

    def play_musicMain(self): #función para hacer la música principal
        pygame.mixer.init()
        pygame.mixer.music.load("res\mainLoop.mp3")
        pygame.mixer.music.play(-1)
    
        
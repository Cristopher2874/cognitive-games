# cheeck :D

from tkinter import messagebox #hacemos import de las ventanas emergentes
import pygame #importamos pygame para la música
import NumPattern as patt #importamos el archivo del patrón de números
import ColorTiles as ct #importamos el archivo del patrón de colores
import LeaderBoards as lb #importamos el archivo de los puntajes
import data as d #importamos el archivo que guarda los puntos
from tkinter import * #importamos la librería tkinter para las ventanas

userList=[] #creamos una lista para gardar el usuario y su puntuación
leaderList=[] #creamos nuestra matriz para guardar cada usuario y su puntaje
userName1="Novato" #creamos una variable que guarda el nombre, por default es novato
userPoints=0 #variable para guardar los puntos

def abrirNumberPatterns(): #función para abrir la segunda venta de number patterns
    pygame.mixer.music.stop() #detenemos la música
    root.withdraw() #escondemos la ventana principal
    root2 = Toplevel(root) #creamos una ventana secundaria encima de la principal
    patt.NumPattern(root2,root) #mandamos llamar la clase de number patterns para abrir las funciones

def abrirColorTiles(): #función para abrir la segunda ventana de color tiles
    pygame.mixer.music.stop() #detenemos la música
    root.withdraw() #escondemos la ventana principal
    root2 = Toplevel(root) #creamos una ventana secundaria encima de la principal
    ct.ColorTiles(root2,root) #mandamos llamar la clase de color tiles para abrir las funciones

def ordenarUsuario(lista): #función para ordenar la lista de usuarios con el mayor puntaje al menor
    #usamos la función de sorted para ordenar la lista que recibimos como argumento
    lista_ordenada = sorted(lista, key=lambda x: x[1], reverse=True) 
    #le decimos que ordene de acuerdo al elemento 1 (puntos) de la lista con datos del usuario
    #le decimos que vaya en reversa para que sea de mayor a menor

    #en este if le decimos que si la longitud de la lista es mayor a 10, tiene que eliminar
    #aquellos elementos que sobran
    if len(lista_ordenada) > 10:
        lista_ordenada = lista_ordenada[:10]

    return lista_ordenada #nos regresa la lista ordenada

def ver_puntajes(): #función que ordena los puntajes y abre la ventana de puntos
    pygame.mixer.music.stop() #detenemos la música
    global userPoints,userList,userName1,leaderList #le decimos que va a usar las variables del inicio
    userPoints=d.userPoints #importamos el valor de los puntos del otro archivo para guardar (data.py)
    userList.append(userName1) #agregamos el nombre del usuario a la lista
    userList.append(userPoints) #agregamos los puntos a la misma lista
    leaderList.append(userList) #agregamos la lista con datos del usuario a la matriz
    userList=[] #borramos la lista donde se guardan los datos del suario
    leaderList=ordenarUsuario(leaderList) #se ordena la matriz con la función de ordenar usuario, se ordena de mayor a menor
    root.withdraw() #se esconde la ventana principal
    segunda_ventana = Toplevel(root) #se crea una segunda ventana sobre la principal
    lb.leaderboard(segunda_ventana,root,leaderList) #se manda llamar la clase de los puntajes para abrir la siguiente ventana

def obtener_nombre(): #función para obtener el nombre del tex entry
    global userName1 #usamos la variable del inicio que guarda el usuario
    userName1 = userName.get() #guardamos el valor del text entry en la variable global

def quit_game(): #función para cerrar el juego
    pygame.mixer.music.stop() #detenemos la música
    root.quit() #cerramos la ventana principal

def mostrar_instrucciones(): #función para mostrar las instrucciones en el cuadro emergente
    #hacemos una variable para guardar las instrucciones
    instrucciones = "Bienvenido a Memory Tiles\n\nInstrucciones:\n\n1. Para guardar puntaje, escribir nombre y dar click en guardar\n2. Presione Color Tiles o Number Patterns para jugar\n3. Para ver puntaje, haga click sobre Leaderboards"
    #usamos un message box para mostrar las instrucciones
    messagebox.showinfo("Instrucciones", instrucciones)

def play_music(): #función para poner la música
    pygame.mixer.init() #iniciamos el reproductor de audio
    pygame.mixer.music.load("res\mainLoop.mp3") #cargamos la canción que vamos a poner
    pygame.mixer.music.play(-1) #le decimos que repita indefinidamente la canción

play_music() #en el programa, mandamos llamar la función de música

root = Tk() #creamos la ventana
root.title("Memory Tiles") #le damos título a la ventana
root.geometry("725x365") #le damos tamaño a la ventana
root.iconbitmap("res\logo.ico") #cargamos el logo de la ventana

background_image = PhotoImage(file=r"res\bgM.png") #cargamos la imagen de fondo

frame=Frame(root) #creamos un frame
frame.pack(fill="both",expand=True) #ponemos el frame en la ventana y le decimos que es expandible
frame.config(bg="black") #le damos un fondo negro

# Crear una etiqueta en el Frame para mostrar la imagen
etiqueta = Label(frame, image=background_image)
etiqueta.image = background_image  #evitamos que la imagen se recargue para que no se borre
etiqueta.grid(row=0, column=0, rowspan=5, columnspan=5, sticky="nsew") #agregamos la imagen 

#En esta sección creamos todos los labels para crear texto, les damos características y las agregamos al frame

label = Label(frame, text="Memory Games",font=("Arial", 24))
label.grid(column=0,row=0,padx=10,pady=10,columnspan=4)

userLabel = Label(frame,text="Enter user: ")
userLabel.grid(column=2,row=1,padx=10,pady=10)


#Creamos el cuadro de texto para que el usuario escriba su nombre
userName = Entry(frame)
userName.grid(column=3,row=1,padx=10,pady=10)

#En esta sección creamos los botones que hay en el frame, les ponemos sus características y las funciones que ejecutan cada uno

saveUser = Button(frame,text="Save user", command=obtener_nombre)
saveUser.grid(row=2,column=2,padx=10,pady=10,columnspan=2)

boton = Button(frame, text="Number Patterns", command=abrirNumberPatterns)
boton.grid(column=0,row=1,padx=10,pady=10)

boton2 = Button(frame, text="Color Tiles", command=abrirColorTiles)
boton2.grid(column=1,row=1,padx=10,pady=10)

ladeboardButton=Button(frame,text="Leaderboards",command=ver_puntajes)
ladeboardButton.grid(column=0,row=2,padx=10,pady=10,columnspan=2)

quitButton=Button(frame,text="Salir",command=quit_game)
quitButton.grid(column=0,row=3,padx=10,pady=10,columnspan=4)

root.after(500,mostrar_instrucciones) #le decimos que luego de 500 milis muestre el cuadro de instrucciones

root.mainloop() #ejecutamos el ciclo de la ventana
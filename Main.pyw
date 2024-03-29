from tkinter import messagebox
import NumPattern as patt
import LeaderBoards as lb
import ColorTiles as ct
import gameWindow as gw
import MoleSmash as mo
from tkinter import *
import data as d
import pygame

userList=[] # list to save the different users
leaderList=[] # list to store the users and their score
userName1="" # default variable for the user name
userPoints=0 # default variable for the user score

def callGame(object):
    pygame.mixer.music.stop() # stop menu music
    root.withdraw() # hide the main window
    root2 = Toplevel(root) # create a new window to display the game
    object(root2,root)

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

def mostrar_instrucciones(): #función para mostrar las instrucciones en el cuadro emergente
    #hacemos una variable para guardar las instrucciones
    instrucciones = "Bienvenido a Memory Tiles\n\nInstrucciones:\n\n1. Para guardar puntaje, escribir nombre y dar click en guardar\n2. Presione Color Tiles o Number Patterns para jugar\n3. Para ver puntaje, haga click sobre Leaderboards"
    #usamos un message box para mostrar las instrucciones
    messagebox.showinfo("Instrucciones", instrucciones)

def quit_game(): #función para cerrar el juego
    pygame.mixer.music.stop() #detenemos la música
    root.quit() #cerramos la ventana principal

gw.game_window.play_musicMain(None)

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

boton = Button(frame, text="Number Patterns", command=lambda: callGame(patt.NumPattern))
boton.grid(column=0,row=1,padx=10,pady=10)

boton2 = Button(frame, text="Color Tiles", command=lambda: callGame(ct.ColorTiles))
boton2.grid(column=1,row=1,padx=10,pady=10)

ladeboardButton=Button(frame,text="Leaderboards",command=ver_puntajes)
ladeboardButton.grid(column=0,row=2,padx=10,pady=10,columnspan=2)

moleButton = Button(frame, text="Mole Smash", command=lambda: callGame(mo.Mole))
moleButton.grid(column=1,row=2, padx=10, pady=10)

quitButton=Button(frame,text="Salir",command=quit_game)
quitButton.grid(column=0,row=3,padx=10,pady=10,columnspan=4)

root.after(500,mostrar_instrucciones) #le decimos que luego de 500 milis muestre el cuadro de instrucciones

root.mainloop() #ejecutamos el ciclo de la ventana
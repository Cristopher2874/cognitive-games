import NumPattern as patt
import ColorTiles as ct
import LeaderBoards as lb
import data as d
from tkinter import *

userList=[]
leaderList=[]
userName1=0
userPoints=0

def abrir_segunda_ventana():
    root.withdraw()
    segunda_ventana = Toplevel(root)
    patt.NumPattern(segunda_ventana,root)

def abrir_tercera_ventana():
    root.withdraw()
    segunda_ventana = Toplevel(root)
    ct.ColorTiles(segunda_ventana,root)

def order_user(lista):
    lista_ordenada = sorted(lista, key=lambda x: x[1], reverse=True)

    if len(lista_ordenada) > 10:
        lista_ordenada = lista_ordenada[:10]

    return lista_ordenada

def ver_puntajes():
    global userPoints,userList,userName1,leaderList
    userPoints=d.userPoints
    print(userPoints)
    userList.append(userName1)
    userList.append(userPoints)
    leaderList.append(userList)
    userList=[]
    leaderList=order_user(leaderList)
    root.withdraw()
    segunda_ventana = Toplevel(root)
    lb.leaderboard(segunda_ventana,root,leaderList)

def obtener_nombre():
    global userName1
    userName1 = userName.get()

def quit_game():
    root.quit()

root = Tk()
root.title("Memory Tiles")
root.geometry("725x365")

background_image = PhotoImage(file=r"C:\Users\Gokus\OneDrive\Escritorio\cognitive-games\bg.png")

frame=Frame(root)
frame.pack(fill="both",expand=True)
frame.config(bg="black")

# Crear una etiqueta en el Frame para mostrar la imagen
etiqueta = Label(frame, image=background_image)
etiqueta.image = background_image  # Evitar que la imagen sea eliminada por la recolección de basura
etiqueta.grid(row=0, column=0, rowspan=5, columnspan=5, sticky="nsew")


label = Label(frame, text="Memory Games",font=("Arial", 24))
label.grid(column=0,row=0,padx=10,pady=10,columnspan=4)

userLabel = Label(frame,text="Ingrese usuario: ")
userLabel.grid(column=2,row=1,padx=10,pady=10)

userName = Entry(frame)
userName.grid(column=3,row=1,padx=10,pady=10)

saveUser = Button(frame,text="Guardar usuario", command=obtener_nombre)
saveUser.grid(row=2,column=2,padx=10,pady=10,columnspan=2)

boton = Button(frame, text="Number Patterns", command=abrir_segunda_ventana)
boton.grid(column=0,row=1,padx=10,pady=10)

boton2 = Button(frame, text="Color Tiles", command=abrir_tercera_ventana)
boton2.grid(column=1,row=1,padx=10,pady=10)

ladeboardButton=Button(frame,text="Leaderboards",command=ver_puntajes)
ladeboardButton.grid(column=0,row=2,padx=10,pady=10,columnspan=2)

quitButton=Button(frame,text="Quit Game",command=quit_game)
quitButton.grid(column=0,row=3,padx=10,pady=10,columnspan=4)

root.mainloop()
import NumPattern as patt
import ColorTiles as ct
import LeaderBoards as lb
from tkinter import *

def abrir_segunda_ventana():
    root.withdraw()
    segunda_ventana = Toplevel(root)
    frame2=Frame(segunda_ventana, width=720, height=360)
    frame2.pack(fill="both")
    frame2.config(bg="lightblue",relief="groove",bd="5")
    patt.NumPattern(segunda_ventana,frame2,root)

def abrir_tercera_ventana():
    root.withdraw()
    segunda_ventana = Toplevel(root)
    frame2=Frame(segunda_ventana, width=720, height=360)
    frame2.pack(fill="both")
    frame2.config(bg="lightblue",relief="groove",bd="5")
    ct.ColorTiles(segunda_ventana,frame2,root)

def ver_puntajes():
    root.withdraw()
    segunda_ventana = Toplevel(root)
    frame2=Frame(segunda_ventana, width=720, height=360)
    frame2.pack(fill="both")
    frame2.config(bg="lightblue",relief="groove",bd="5")
    lb.leaderboard(segunda_ventana,frame2,root)

def quit_game():
    root.quit()

root = Tk()
root.title("Memory Tiles")
root.geometry("720x360")

frame=Frame(root, width=720, height=360)
frame.pack(fill="both")
frame.config(bg="lightblue",relief="groove",bd="5")

label = Label(frame, text="Esta es la ventana principal")
label.grid(column=0,row=0,padx=10,pady=10)

boton = Button(frame, text="Number Patterns", command=abrir_segunda_ventana)
boton.grid(column=0,row=1,padx=10,pady=10)

boton2 = Button(frame, text="Color Tiles", command=abrir_tercera_ventana)
boton2.grid(column=1,row=1,padx=10,pady=10)

ladeboardButton=Button(frame,text="Leaderboards",command=ver_puntajes)
ladeboardButton.grid(column=0,row=3,padx=10,pady=10)

quitButton=Button(frame,text="Quit Game",command=quit_game)
quitButton.grid(column=0,row=4,padx=10,pady=10)

root.mainloop()
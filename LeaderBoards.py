from tkinter import *

class leaderboard:
    def __init__(self,root,frame,root2):
        self.root = root
        self.mainRoot=root2
        self.frame=frame
        self.root.title("Scores")
        self.boton_cerrar = Button(self.frame, text="Back To Menu", command=self.cerrar_segunda_ventana)
        self.boton_cerrar.grid(column=0,row=5,padx=10,pady=10,columnspan=4)
    def cerrar_segunda_ventana(self):
        self.root.destroy()
        self.mainRoot.deiconify()
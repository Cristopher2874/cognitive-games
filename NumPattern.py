import tkinter as tk
import random

class NumPattern:
    def __init__(self, root,root2):
        self.root = root
        self.mainRoot=root2
        self.frame=tk.Frame(root)
        self.frame.pack(fill="both",expand=True)
        self.frame.config(bg="black")
        self.root.title("Number Pattern")
        self.root.geometry("550x515")
        self.background_image = tk.PhotoImage(file=r"C:\Users\Gokus\OneDrive\Escritorio\cognitive-games\bg.png")
        self.etiqueta = tk.Label(self.frame, image=self.background_image)
        self.etiqueta.image = self.background_image  # Evitar que la imagen sea eliminada por la recolección de basura
        self.etiqueta.grid(row=0, column=0, rowspan=8, columnspan=5, sticky="nsew")
        self.pattern = []
        self.user_input = []
        self.sequence_length = 3
        self.display_time = 7
        self.user_time = 7
        self.game_active = False
        self.number_buttons = []
        self.idx=0
        self.counter=0
        self.lvl=0
        self.abs_lvl=1
        self.points=0
        self.pattern_label = tk.Label(self.frame, text="Presiona start\ncuando estés listo", font=("Arial", 24))
        self.pattern_label.grid(column=0,row=0,columnspan=3,pady=10)
        self.levelLabel=tk.Label(self.frame,text=("Level: "+str(self.abs_lvl)),font=("Arial", 12))
        self.levelLabel.grid(column=0,row=1,pady=10)
        self.pointsLabel=tk.Label(self.frame,text="Points: "+str(self.points),font=("Arial", 12))
        self.pointsLabel.grid(column=2,row=1,pady=10)
        self.start_button = tk.Button(self.frame, text="Start", command=self.start_game)
        self.start_button.grid(column=0,row=5,padx=10,pady=10,columnspan=1)
        self.reset_button = tk.Button(self.frame, text="Reset", command=self.reset_game)
        self.reset_button.grid(column=2,row=5,padx=10,pady=10)
        self.boton_cerrar = tk.Button(self.frame, text="Back To Menu", command=self.cerrar_segunda_ventana)
        self.boton_cerrar.grid(column=0,row=6,padx=10,pady=10,columnspan=3)

    def cerrar_segunda_ventana(self):
        self.root.destroy()
        self.mainRoot.deiconify()

    def set_points(self):
        global points
        points = self.points
    
    def get_points():
        return NumPattern.points

    def start_game(self):
        self.start_button.config(state=tk.DISABLED)
        self.reset_button.config(state=tk.DISABLED)
        self.game_active = True
        for i in range(3):
            for i in range(1, 10):
                button = tk.Button(self.frame, text=str(i), height=5,width=9, command=lambda i=i: self.check_input(i))
                button.grid(row=((i-1) // 3)+2, column=(i-1) % 3, padx=10, pady=10)
                self.number_buttons.append(button)
        self.next_pattern()
    
    def reset_game(self):
        self.pattern = []
        self.user_input = []
        self.sequence_length = 3
        self.display_time = 7
        self.user_time = 7
        self.idx=0
        self.counter=0
        self.abs_lvl=1
        self.points=0
        self.levelLabel.config(text=("Level: "+str(self.abs_lvl)))
        self.pointsLabel.config(text="Points: "+str(self.points))
        self.pattern_label.config(text="Presiona start cuando\nestés listo")
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
    
    def next_pattern(self):
        self.user_input = []
        self.pattern = []
        for _ in range(self.sequence_length):
            self.pattern.append(random.randint(1, 9))
        self.pointsLabel.config(text="Points: "+str(self.points))
        self.display_pattern()
        for button in self.number_buttons:
            button.config(state=tk.DISABLED)
        self.root.after(self.display_time * 1000, self.get_user_input)
    
    def display_pattern(self):
        pattern_str = " ".join(map(str, self.pattern))
        self.pattern_label.config(text=pattern_str)
        self.levelLabel.config(text=("Level: "+str(self.abs_lvl)))
    
    def get_user_input(self):
        if not self.game_active:
            return
        for button in self.number_buttons:
            button.config(state=tk.NORMAL)
        self.pattern_label.config(text="Your Turn")
        self.root.after(self.user_time*1000, self.check_user_pattern)
    
    def check_input(self, number):
        self.user_input.append(number)
    
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
                self.pattern_label.config(text="Game Over")
                self.reset_button.config(state=tk.NORMAL)
                self.game_active = False
        if self.counter==self.idx:
            self.lvl+=1
            if self.lvl==3:
                self.sequence_length += 1
                self.display_time -= 1
                self.user_time -= 1
                self.lvl=0
                self.abs_lvl+=1
            if self.user_time<5:
                self.user_time=5
            if self.display_time<3:
                self.display_time=3
            if self.abs_lvl<3:
                self.points+=10
            elif self.abs_lvl<6:
                self.points+=15
            else:
                self.points+=25
            self.next_pattern()
        else:
            self.set_points()
            self.pattern_label.config(text="Game Over")
            self.reset_button.config(state=tk.NORMAL)
            self.game_active = False
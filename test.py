import tkinter as tk
import random
import time

class SimonGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Simon Game")
        self.colors = ["red", "blue", "green", "yellow"]
        self.pattern = []
        self.user_input = []
        self.sequence_length = 3
        self.display_time = 10
        self.pattern_label = tk.Label(root, text="_____", font=("Arial", 24))
        self.pattern_label.pack(pady=20)
        self.start_button = tk.Button(root, text="Start", command=self.start_game)
        self.start_button.pack()
        self.root.geometry("300x300")
        self.game_active = False
    
    def start_game(self):
        self.start_button.config(state=tk.DISABLED)
        self.game_active = True
        for color in self.colors:
            button = tk.Button(self.root, text=color, bg=color, command=lambda color=color: self.check_input(color))
            button.pack(side=tk.LEFT)
        self.play_pattern()
    
    def play_pattern(self):
        self.user_input = []
        self.pattern = []
        self.pattern = [random.choice(self.colors) for _ in range(self.sequence_length)]
        self.display_pattern()
        self.root.after(self.display_time * 1000, self.get_user_input)
    
    def display_pattern(self):
        for color in self.pattern:
            self.pattern_label.config(bg=color)
            self.root.update()
            time.sleep(1)
            self.pattern_label.config(bg="white")
            self.root.update()
            time.sleep(0.5)
        self.get_user_input()
    
    def get_user_input(self):
        self.pattern_label.config(text="Your Turn")
        self.root.after(5000, self.check_user_pattern)
    
    def check_input(self, color):
        self.user_input.append(color)
    
    def check_user_pattern(self):
        if self.user_input == self.pattern:
            if len(self.user_input) == self.sequence_length:
                self.sequence_length += 1
                if self.sequence_length % 4 == 0:
                    self.display_time -= 1
                self.play_pattern()
        else:
            self.pattern_label.config(text="Game Over")
            self.start_button.config(state=tk.NORMAL)
            self.game_active = False

if __name__ == "__main__":
    root = tk.Tk()
    game = SimonGame(root)
    root.mainloop()

import tkinter as tk
from tkinter import *

BACKGROUND = "black"
TEXTCOLOR = "white"
GAME_HEIGHT = 900
GAME_WIDTH = 900
GAME_SIZE = 50


root = tk.Tk()
root.title("Snake Game")
root.geometry(f"{GAME_HEIGHT}x{GAME_WIDTH}")
root.configure(bg=BACKGROUND)



def clear_screen(container):
    for widget in container.pack_slaves():
        widget.pack_forget()
        

def first_page():
    global welcome_text, button, instructions
    clear_screen(root)
    welcome_text = tk.Label(root, text="\nWELCOME TO THE SNAKE GAME \n", font="Times 32", bg=BACKGROUND, fg = TEXTCOLOR)
    welcome_text.pack()
    
    button = tk.Button(root, text="Click this button to play the game", font="Times 20", bg=BACKGROUND, fg = TEXTCOLOR, command=play_game)
    button.pack()

    instructions_button = tk.Button(root, text="Click this button to get instructions about the game", font="Times 20", bg=BACKGROUND, fg = TEXTCOLOR, command=instructions)
    instructions_button.pack()

def play_game():
    clear_screen(root)
    
    play_button = tk.Button(root, text="START NOW", font="Times 32", bg=BACKGROUND, fg = TEXTCOLOR, command=create_canvas)
    play_button.pack()
    return_button = tk.Button(root, text="Return", font="Times 20", bg=BACKGROUND, fg = TEXTCOLOR, command=first_page)
    return_button.pack()
    
def instructions():
     clear_screen(root)
     instructions = tk.Label(root, text="\n \n \nYour mission is to eat all the apples", font="Times 20", bg=BACKGROUND, fg = TEXTCOLOR)
     instructions.pack()
     return_button = tk.Button(root, text="Return", font="Times 20", bg=BACKGROUND, fg = TEXTCOLOR, command=first_page)
     return_button.pack()
     
    
    
	
def create_canvas():
    clear_screen(root)
    canvas = Canvas(root, bg = BACKGROUND, height=900, width=900)
    canvas.pack()
    canvas.create_oval(0, 0, 50, 50, fill="red")
    canvas.create_rectangle(850, 0, 900, 50, fill = "green")
    


def main():
	first_page()

main()

root.mainloop()

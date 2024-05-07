import tkinter as tk
from tkinter import *
from customtkinter import *

BACKGROUND = "black"
TEXTCOLOR = "white"
GAME_HEIGHT = 900
GAME_WIDTH = 900
GAME_SIZE = 50
SNAKE_LENGTH = 3
UPDATE_INTERVAL = 150
current_direction = "right"


root = tk.Tk()
root.title("Snake Game")
root.geometry(f"{GAME_HEIGHT}x{GAME_WIDTH}")
root.configure(bg=BACKGROUND)

canvas = Canvas(root, bg = BACKGROUND, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()

def clear_screen(container):
    for widget in container.pack_slaves():
        widget.pack_forget()
        

def first_page():
    global current_direction, snake_coordinates
    current_direction = "right"
    snake_coordinates = []
    clear_screen(root)
    global welcome_text, button, instructions
    
    welcome_text = tk.Label(root, text="\nWELCOME TO THE SNAKE GAME \n", font="Times 32", bg=BACKGROUND, fg = TEXTCOLOR)
    welcome_text.pack()
    
    button = tk.Button(root, text="Click this button to play the game", font="Times 20", bg=BACKGROUND, fg = TEXTCOLOR, command=play_game)
    button.pack()

    instructions_button = tk.Button(root, text="Click this button to get instructions about the game", font="Times 20", bg=BACKGROUND, fg = TEXTCOLOR, command=instructions)
    instructions_button.pack()

def play_game():
    clear_screen(root)
    start_game()

def start_game():
    create_canvas()
    move_snake()
    
def instructions():
     clear_screen(root)
     instructions = tk.Label(root, text="\n \n \nYour mission is to eat all the apples", font="Times 20", bg=BACKGROUND, fg = TEXTCOLOR)
     instructions.pack()
     return_button = tk.Button(root, text="Return", font="Times 20", bg=BACKGROUND, fg = TEXTCOLOR, command=first_page)
     return_button.pack()
     
    
def create_canvas():
    clear_screen(root)
    canvas.pack()
    create_initial_snake()
    print(snake_coordinates)
    
    
def create_initial_snake():
    global snake_coordinates
    snake_coordinates = []
    x = 0
    y = (GAME_HEIGHT / 2)

    for _ in range(SNAKE_LENGTH):
        snake_coordinates.insert(0, [x, y])
        canvas.create_rectangle(x, y, x + GAME_SIZE, y + GAME_SIZE, fill="green")
        x += GAME_SIZE
        
        
def print_snake():
    canvas.delete("all")
    for x, y in snake_coordinates:
        canvas.create_rectangle(x, y, x + GAME_SIZE, y + GAME_SIZE, fill="green")
        
    
def snake_move(dir):
    global current_direction
    if dir:
        current_direction = dir
    x, y = snake_coordinates[0]

    if current_direction == "right":
        x += GAME_SIZE
    elif current_direction == "down":
        y += GAME_SIZE
    elif current_direction == "up":
        y -= GAME_SIZE
    elif current_direction == "left":
        x -= GAME_SIZE

    if x < 0 or x >= GAME_WIDTH or y < 0 or y >= GAME_HEIGHT:
        game_over()
        return

    snake_coordinates.insert(0, [x, y])
    snake_coordinates.pop()

    print_snake()
        
def move_snake():
    snake_move(current_direction)
    root.after(UPDATE_INTERVAL, move_snake)
    
def game_over():
    clear_screen(root)
    over_text = tk.Label(root, text="Game Over!", font="Times 32", bg=BACKGROUND, fg=TEXTCOLOR)
    over_text.pack()
    restart_button = tk.Button(root, text="Restart Game", font="Times 20", bg=BACKGROUND, fg=TEXTCOLOR, command=restart_game)
    restart_button.pack()

def restart_game():
    clear_screen(root)
    first_page()



root.bind('<Right>', lambda event: snake_move('right'))
root.bind('<Left>', lambda event: snake_move('left'))
root.bind('<Up>', lambda event: snake_move('up'))
root.bind('<Down>', lambda event: snake_move('down'))




def main():
	first_page()

main()

root.mainloop()
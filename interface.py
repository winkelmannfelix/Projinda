import tkinter as tk
from tkinter import *

BACKGROUND = "black"
TEXTCOLOR = "white"
GAME_HEIGHT = 900
GAME_WIDTH = 900
GAME_SIZE = 50
SNAKE_LENGTH = 3
SNAKE_SPEED = 120

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
    canvas.pack()
    create_initial_snake()
    move_snake()
    
 
    
def create_initial_snake():
    global snake_coordinates
    snake_coordinates = []
    counter = 0
    x = 0
    y = (GAME_HEIGHT/2)
    
    while counter < SNAKE_LENGTH:
        snake_coordinates.insert(0, [x, y])
        canvas.create_rectangle(x, y, x+ GAME_SIZE, y + GAME_SIZE, fill = "green")
        x += GAME_SIZE
        counter += 1
        
        
def print_snake():
    canvas.delete("all")
    for i in snake_coordinates:
        x = i[0]
        y = i[1]
        canvas.create_rectangle(x, y, x+GAME_SIZE, y+GAME_SIZE, fill = "green")


def move_snake():
    global current_direction
    snake_move(current_direction)
    root.after(SNAKE_SPEED, move_snake)  # Move the snake every 100 ms
  
    
def snake_move(dir):
    global current_direction
    x = snake_coordinates[0][0]
    y = snake_coordinates[0][1]

    if dir == "right":
        if current_direction != "left":
            x += GAME_SIZE
            canvas.create_rectangle(x, y, x+GAME_SIZE, y+GAME_SIZE, fill = "green")
            snake_coordinates.insert(0, [x, y])
            
            snake_coordinates.pop()
            current_direction = "right"
        
    elif dir == "down":
        if current_direction != "up":
            y += GAME_SIZE
            canvas.create_rectangle(x, y, x+GAME_SIZE, y+GAME_SIZE, fill = "green")
            snake_coordinates.insert(0, [x, y])
            
            snake_coordinates.pop()
            current_direction = "down"
        
        
    elif dir == "up":
        if current_direction != "down":
            y -= GAME_SIZE
            canvas.create_rectangle(x, y, x+GAME_SIZE, y+GAME_SIZE, fill = "green")
            snake_coordinates.insert(0, [x, y])
            
            snake_coordinates.pop()
            current_direction = "up"
        
    elif dir == "left":
        if current_direction != "right":
            x -= GAME_SIZE
            canvas.create_rectangle(x, y, x+GAME_SIZE, y+GAME_SIZE, fill = "green")
            snake_coordinates.insert(0, [x, y])
            
            snake_coordinates.pop()
            current_direction = "left"
    
    print_snake()
        



root.bind('<Right>', lambda event: snake_move('right'))
root.bind('<Left>', lambda event: snake_move('left'))
root.bind('<Up>', lambda event: snake_move('up'))
root.bind('<Down>', lambda event: snake_move('down'))




def main():
	first_page()

main()

root.mainloop()
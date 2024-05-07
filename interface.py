import tkinter as tk
from tkinter import *

BACKGROUND = "black"
TEXTCOLOR = "white"
GAME_HEIGHT = 900
GAME_WIDTH = 900
GAME_SIZE = 50
SNAKE_LENGTH = 3
SNAKE_SPEED = 120
SNAKE_COLOR = "green"

current_direction = "right"
snake_move_setup = None
flag_game_over = False


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
    global welcome_text, button, instructions, current_direction, snake_coordinates
    clear_screen(root)
    welcome_text = tk.Label(root, text="\nWELCOME TO THE SNAKE GAME \n", font="Times 32", bg=BACKGROUND, fg = TEXTCOLOR)
    welcome_text.pack()
    
    button = tk.Button(root, text="Click this button to play the game", font="Times 20", bg=BACKGROUND, fg = TEXTCOLOR, command=play_game)
    button.pack()

    instructions_button = tk.Button(root, text="Click this button to get instructions about the game", font="Times 20", bg=BACKGROUND, fg = TEXTCOLOR, command=instructions)
    instructions_button.pack()

def play_game():
    clear_screen(root)
    
    play_button = tk.Button(root, text="START NOW", font="Times 32", bg=BACKGROUND, fg = TEXTCOLOR, command=main)
    play_button.pack()
    return_button = tk.Button(root, text="Return", font="Times 20", bg=BACKGROUND, fg = TEXTCOLOR, command=first_page)
    return_button.pack()
    
def instructions():
     clear_screen(root)
     instructions = tk.Label(root, text="\n \n \nYour mission is to eat all the apples", font="Times 20", bg=BACKGROUND, fg = TEXTCOLOR)
     instructions.pack()
     return_button = tk.Button(root, text="Return", font="Times 20", bg=BACKGROUND, fg = TEXTCOLOR, command=first_page)
     return_button.pack()
     
    
    
def main():
    global snake_move_setup, flag_game_over
    clear_screen(root)
    canvas.pack()
    if snake_move_setup is not None:
            root.after_cancel(snake_move_setup)
            snake_move_setup = None
    create_initial_snake()
    flag_game_over = False
    move_snake()

def restart_game():
        global current_direction, snake_coordinates, snake_move_setup

        if snake_move_setup is not None:
            root.after_cancel(snake_move_setup)
            snake_move_setup = None
        main()
        #current_direction = "right"  
        #clear_screen(root) 
        #canvas.pack()  
        #create_initial_snake() 
        #move_snake()

def game_over():
        global snake_move_setup, flag_game_over
        flag_game_over = True
        if snake_move_setup is not None:
            root.after_cancel(snake_move_setup)
            snake_move_setup = None

        clear_screen(root)
        over_text = tk.Label(root, text="Game Over!", font="Times 32", bg=BACKGROUND, fg=TEXTCOLOR)
        over_text.pack()
        restart_button = tk.Button(root, text="Restart Game", font="Times 20", bg=BACKGROUND, fg=TEXTCOLOR, command=restart_game)
        restart_button.pack()
        main_menu_button = tk.Button(root, text="Return to main menu", font="Times 20", bg="blue", fg=TEXTCOLOR, command=first_page)
        main_menu_button.pack()
    
 
    
def create_initial_snake():
    global snake_coordinates
    snake_coordinates = []
    counter = 0
    x = 0
    y = (GAME_HEIGHT/2)
    
    while counter < SNAKE_LENGTH:
        snake_coordinates.insert(0, [x, y])
        canvas.create_rectangle(x, y, x+ GAME_SIZE, y + GAME_SIZE, fill = SNAKE_COLOR)
        x += GAME_SIZE
        counter += 1
        
        
def print_snake():
    canvas.delete("all")
    for i in snake_coordinates:
        x = i[0]
        y = i[1]
        canvas.create_rectangle(x, y, x+GAME_SIZE, y+GAME_SIZE, fill = SNAKE_COLOR)


def move_snake():
    global current_direction, snake_move_setup
    snake_move(current_direction)
    snake_move_setup = root.after(SNAKE_SPEED, move_snake)
  
    
def snake_move(dir):
    global current_direction, snake_move_setup, flag_game_over
    if flag_game_over:
         return
    x = snake_coordinates[0][0]
    y = snake_coordinates[0][1]

    if dir == "right":
        if current_direction != "left":
            x += GAME_SIZE   
            current_direction = "right"
        
    elif dir == "down":
        if current_direction != "up":
            y += GAME_SIZE
            current_direction = "down"
        
        
    elif dir == "up":
        if current_direction != "down":
            y -= GAME_SIZE    
            current_direction = "up"
        
    elif dir == "left":
        if current_direction != "right":
            x -= GAME_SIZE
            current_direction = "left"

    if x < 0 or x >= GAME_WIDTH or y < 0 or y >= GAME_HEIGHT:
        game_over()
        return
    
    canvas.create_rectangle(x, y, x+GAME_SIZE, y+GAME_SIZE, fill = SNAKE_COLOR)
    snake_coordinates.insert(0, [x, y])
    snake_coordinates.pop()
    print_snake()




root.bind('<Right>', lambda event: snake_move('right'))
root.bind('<Left>', lambda event: snake_move('left'))
root.bind('<Up>', lambda event: snake_move('up'))
root.bind('<Down>', lambda event: snake_move('down'))



first_page()

root.mainloop()
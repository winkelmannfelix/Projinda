import tkinter as tk
from tkinter import *
import random

BACKGROUND = "black"
TEXTCOLOR = "white"
GAME_HEIGHT = 900
GAME_WIDTH = 900
GAME_SIZE = 50
SCOREBOARD_HEIGHT = 50
SNAKE_LENGTH = 3
SNAKE_SPEED = 120
SNAKE_COLOR = "green"
SNAKE2_COLOR = "pink"
APPLE_COLOR = "red"

current_direction = "right"
snake_move_setup = None
flag_game_over = False
apple_position = []


root = tk.Tk()
root.title("Snake Game")
root.geometry(f"{GAME_HEIGHT}x{GAME_WIDTH}")
root.configure(bg=BACKGROUND)

scoreboard_frame = tk.Frame(root, bg=BACKGROUND, height=SCOREBOARD_HEIGHT)
scoreboard_frame.pack(fill=X)

canvas = Canvas(root, bg = BACKGROUND, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()

snake1_score_label = tk.Label(scoreboard_frame, text="Snake 1 Score: 0", font="Times 20", bg=BACKGROUND, fg=TEXTCOLOR)
snake2_score_label = tk.Label(scoreboard_frame, text="Snake 2 Score: 0", font="Times 20", bg=BACKGROUND, fg=TEXTCOLOR)
snake1_score_label.pack(side=LEFT, padx=10)
snake2_score_label.pack(side=RIGHT, padx=10)

def generate_apple():
    global apple_position
    while True:
        x = random.randint(0, (GAME_WIDTH // GAME_SIZE) - 1) * GAME_SIZE
        y = random.randint(0, (GAME_HEIGHT // GAME_SIZE) - 1) * GAME_SIZE
        apple_position = [x, y]
        if apple_position not in snake_coordinates:
            break
        
def eat_apple():
    canvas.delete("all")
    generate_apple()


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
    
    play_button = tk.Button(root, text="START NOW", font="Times 32", bg=BACKGROUND, fg = TEXTCOLOR, command=lambda: main("singleplayer"))
    play_button.pack()
    
    play_button = tk.Button(root, text="START NOW multiplayer", font="Times 32", bg=BACKGROUND, fg = TEXTCOLOR, command=lambda: main("multiplayer"))
    play_button.pack()
    
    return_button = tk.Button(root, text="Return", font="Times 20", bg=BACKGROUND, fg = TEXTCOLOR, command=first_page)
    return_button.pack()
    
def instructions():
     clear_screen(root)
     instructions = tk.Label(root, text="\n \n \nYour mission is to eat all the apples", font="Times 20", bg=BACKGROUND, fg = TEXTCOLOR)
     instructions.pack()
     return_button = tk.Button(root, text="Return", font="Times 20", bg=BACKGROUND, fg = TEXTCOLOR, command=first_page)
     return_button.pack()
     
    
    
def main(gametype):
    global snake_move_setup, flag_game_over, current_direction, current2_direction, theGametype, snake1_points, snake2_points
    theGametype = gametype
    current_direction  = "right"
    current2_direction = "right"
    snake1_points = 0
    snake2_points = 0
    clear_screen(root)
    scoreboard_frame.pack(fill=X)
    canvas.pack()
    snake1_score_label.config(text="Snake 1 Score: 0")  
    if theGametype == "multiplayer":
        snake2_score_label.config(text="Snake 2 Score: 0")
    if snake_move_setup is not None:
            root.after_cancel(snake_move_setup)
            snake_move_setup = None
    create_initial_snake()
    generate_apple()
    flag_game_over = False
    move_snake()

def restart_game():
        global current_direction, snake_coordinates, snake_move_setup

        if snake_move_setup is not None:
            root.after_cancel(snake_move_setup)
            snake_move_setup = None
        scoreboard_frame.pack(fill=X)
        main(theGametype)
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

        scoreboard_frame.pack_forget()
        clear_screen(root)
        over_text = tk.Label(root, text="Game Over!", font="Times 32", bg=BACKGROUND, fg=TEXTCOLOR)
        over_text.pack()
        score_text_one = tk.Label(root, text=f"Final Score:\nSnake 1: {snake1_points} points", font="Times 20", bg=BACKGROUND, fg=TEXTCOLOR)
        score_text_one.pack()
        if theGametype == "multiplayer":
            score_text_two = tk.Label(root, text=f"Snake 2: {snake2_points} points", font="Times 20", bg=BACKGROUND, fg=TEXTCOLOR)
            score_text_two.pack()
            if snake1_points > snake2_points:
                winner = tk.Label(root, text="Snake 1 wins, you rock!", font="Times 24", bg=BACKGROUND, fg=TEXTCOLOR)
            elif snake2_points > snake1_points:
                winner = tk.Label(root, text="Snake 2 wins, you're very cool!", font="Times 24", bg=BACKGROUND, fg=TEXTCOLOR)
            else:
                winner = tk.Label(root, text="It's a Tie!", font="Times 24", bg=BACKGROUND, fg=TEXTCOLOR)
        winner.pack()
        restart_button = tk.Button(root, text="Restart Game", font="Times 20", bg=BACKGROUND, fg=TEXTCOLOR, command=restart_game)
        restart_button.pack()
        main_menu_button = tk.Button(root, text="Return to main menu", font="Times 20", bg=BACKGROUND, fg=TEXTCOLOR, command=first_page)
        main_menu_button.pack()
    
 
    
def create_initial_snake():
    global snake_coordinates, snake2_coordinates
    snake_coordinates = []
    snake2_coordinates = []
    counter = 0
    x = 0
    y2 = 50
    y = (GAME_HEIGHT/2)
    
    while counter < SNAKE_LENGTH:
        snake_coordinates.insert(0, [x, y])
        canvas.create_rectangle(x, y, x+ GAME_SIZE, y + GAME_SIZE, fill = SNAKE_COLOR)
        
        if theGametype == "multiplayer":
            snake2_coordinates.insert(0, [x, y2])
            canvas.create_rectangle(x, y2, x+ GAME_SIZE, y2 + GAME_SIZE, fill = SNAKE2_COLOR)
        x += GAME_SIZE
        
        counter += 1
        
        
def print_snake():
    canvas.delete("all")
    canvas.create_rectangle(apple_position[0], apple_position[1], apple_position[0] + GAME_SIZE, apple_position[1] + GAME_SIZE, fill=APPLE_COLOR)
    for i in snake_coordinates:
        x = i[0]
        y = i[1]
        canvas.create_rectangle(x, y, x+GAME_SIZE, y+GAME_SIZE, fill = SNAKE_COLOR)
    if snake2_coordinates:
        for i in snake2_coordinates:
            x = i[0]
            y = i[1]
            canvas.create_rectangle(x, y, x+GAME_SIZE, y+GAME_SIZE, fill = SNAKE2_COLOR)


def move_snake():
    global current_direction, current2_direction, snake_move_setup
    snake_move(current_direction, snake_coordinates)
    if snake2_coordinates:
        snake_move(current2_direction, snake2_coordinates)
    snake_move_setup = root.after(SNAKE_SPEED, move_snake)
  
    
def snake_move(dir, coordinates):
    global current_direction, current2_direction, snake_move_setup, flag_game_over, snake1_points, snake2_points
    if flag_game_over:
         return
    x = coordinates[0][0]
    y = coordinates[0][1]
    
    if coordinates == snake2_coordinates:
        direction = current2_direction
    else:
        direction = current_direction
        

    if dir == "right" and direction != "left":
        x += GAME_SIZE
        direction = "right"
        
    elif dir == "down" and direction != "up":
        y += GAME_SIZE
        direction = "down"
        
    elif dir == "up" and direction != "down":
        y -= GAME_SIZE
        direction = "up"
        
    elif dir == "left" and direction != "right":
        x -= GAME_SIZE
        direction = "left"
        
    else:
        if direction == "right":
            x += GAME_SIZE
            
        elif direction == "down":
            y += GAME_SIZE
            
        elif direction == "up":
            y -= GAME_SIZE
            
        elif direction == "left":
            x -= GAME_SIZE
     

    if x < 0 or x >= GAME_WIDTH or y < 0 or y >= GAME_HEIGHT:
        game_over()
        return
    
    if any(coordinate == [x, y] for coordinate in snake2_coordinates) or any(point == [x, y] for point in snake_coordinates):
        game_over()

    
    if x == apple_position[0] and y == apple_position[1]:
        eat_apple()
        coordinates.insert(0, [x, y])
        if coordinates == snake2_coordinates:
            snake2_points += 1
            snake2_score_label.config(text=f"Snake 2 Score: {snake2_points}")
        else:
            snake1_points += 1
            snake1_score_label.config(text=f"Snake 1 Score: {snake1_points}")

        
    
    if coordinates == snake2_coordinates:
        current2_direction = direction
    else:
        current_direction = direction
    
    canvas.create_rectangle(x, y, x+GAME_SIZE, y+GAME_SIZE, fill = SNAKE_COLOR)
    coordinates.insert(0, [x, y])
    coordinates.pop()
    print_snake()



root.bind('<Right>', lambda event: snake_move('right', snake_coordinates))
root.bind('<Left>', lambda event: snake_move('left', snake_coordinates))
root.bind('<Up>', lambda event: snake_move('up', snake_coordinates))
root.bind('<Down>', lambda event: snake_move('down', snake_coordinates))

root.bind('<d>', lambda event: snake_move('right', snake2_coordinates))
root.bind('<a>', lambda event: snake_move('left', snake2_coordinates))
root.bind('<w>', lambda event: snake_move('up', snake2_coordinates))
root.bind('<s>', lambda event: snake_move('down', snake2_coordinates))




first_page()

root.mainloop()
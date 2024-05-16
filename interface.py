import tkinter as tk
from tkinter import *
import random
from PIL import ImageTk, Image

BACKGROUND = "black"
TEXTCOLOR = "white"
GAME_HEIGHT = 900
GAME_WIDTH = 900
GAME_SIZE = 50
SNAKE_LENGTH = 3
SNAKE_SPEED = 120
SNAKE_COLOR = "green"
SNAKE2_COLOR = "pink"
APPLE_COLOR = "red"
OBSTACLE_COLOR = "grey"

current_direction = "right"
snake_move_setup = None
flag_game_over = False
apple_position = []
obstacle_coordinates = []


root = tk.Tk()
root.title("Snake Game")
root.geometry(f"{GAME_HEIGHT}x{GAME_WIDTH}")
root.configure(bg=BACKGROUND)

canvas = Canvas(root, bg = BACKGROUND, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()

apple_image = Image.open("apple.png") 
apple_image = apple_image.resize((GAME_SIZE, GAME_SIZE), Image.LANCZOS) 
apple_image = ImageTk.PhotoImage(apple_image)

def generate_apple():
    global apple_position
    while True:
        x = random.randint(0, (GAME_WIDTH // GAME_SIZE) - 1) * GAME_SIZE
        y = random.randint(0, (GAME_HEIGHT // GAME_SIZE) - 1) * GAME_SIZE
        apple_position = [x, y]
        if apple_position not in snake_coordinates:
            if apple_position not in snake2_coordinates:
                if apple_position not in obstacle_coordinates:
                    break
        
                   
def eat_apple():
    canvas.delete("apple")
    generate_apple()


def create_obstacles():
    global obstacle_coordinates
    obstacle_coordinates = [[100, 650], [100+GAME_SIZE, 650], [100, 650+GAME_SIZE], [100+GAME_SIZE, 650+GAME_SIZE]
                            , [100, 50], [100+GAME_SIZE, 50], [100+GAME_SIZE*2, 50], [100+GAME_SIZE*3, 50], [100+GAME_SIZE*4, 50],
                            [500, 150], [500+ GAME_SIZE, 150], [500+ GAME_SIZE*2, 150], [500+ GAME_SIZE*3, 150], [500+ GAME_SIZE*3, 150], [500+ GAME_SIZE*4, 150], [500+ GAME_SIZE*5, 150],
                            [500, 250], [500+ GAME_SIZE, 250], [500+ GAME_SIZE*2, 250], [500+ GAME_SIZE*3, 250], [500+ GAME_SIZE*3, 250], [500+ GAME_SIZE*3, 300],
                            [500+GAME_SIZE*5, 200], [500+GAME_SIZE*5, 200+GAME_SIZE], [500+GAME_SIZE*5, 200+GAME_SIZE*2],
                            [550, 800], [600, 750], [650, 700], [700, 650], [750, 600]]
    
        

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
    
    play_button = tk.Button(root, text="START NOW with obstacles", font="Times 32", bg=BACKGROUND, fg = TEXTCOLOR, command=lambda: main("obstacles"))
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
    if theGametype ==  "obstacles":
        create_obstacles()
    clear_screen(root)
    canvas.pack()
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

        clear_screen(root)
        over_text = tk.Label(root, text="Game Over!", font="Times 32", bg=BACKGROUND, fg=TEXTCOLOR)
        over_text.pack()
        restart_button = tk.Button(root, text="Restart Game", font="Times 20", bg=BACKGROUND, fg=TEXTCOLOR, command=restart_game)
        restart_button.pack()
        main_menu_button = tk.Button(root, text="Return to main menu", font="Times 20", bg="blue", fg=TEXTCOLOR, command=first_page)
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
    # canvas.create_rectangle(apple_position[0], apple_position[1], apple_position[0] + GAME_SIZE, apple_position[1] + GAME_SIZE, fill=APPLE_COLOR)
    canvas.create_image(apple_position[0], apple_position[1], image=apple_image, anchor="nw", tags="apple") 
    
    if theGametype == "obstacles":
        for i in obstacle_coordinates:
            x = i[0]
            y = i[1]
            canvas.create_rectangle(x, y, x+GAME_SIZE, y+GAME_SIZE, fill = OBSTACLE_COLOR)

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
        
    if any(coordinate == [x, y] for coordinate in obstacle_coordinates):
        game_over()

    
    if x == apple_position[0] and y == apple_position[1]:
        eat_apple()
        coordinates.insert(0, [x, y])
        if coordinates == snake2_coordinates:
            snake2_points += 1
        else:
            snake1_points += 1
        print(f"snake 1 has {snake1_points}")

        print(f"snake 2 has {snake2_points}")
        print("\n")

        
    
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
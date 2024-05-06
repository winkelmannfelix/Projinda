import tkinter as tk

BACKGROUND = "black"
TEXTCOLOR = "white"


root = tk.Tk()
root.title("Snake Game")
root.geometry("900x900")
root.configure(bg=BACKGROUND)

def clear_screen(container):
    for widget in container.pack_slaves():
        widget.pack_forget()

def first_page():
    global welcome_text, button, instructions
    welcome_text = tk.Label(root, text="\n WELCOME TO THE SNAKE GAME \n", font="Times 32", bg=BACKGROUND, fg = TEXTCOLOR)
    welcome_text.pack()
    
    button = tk.Button(root, text="Click this button to play the game", font="Times 20", bg=BACKGROUND, fg = TEXTCOLOR, command=play_game)
    button.pack()

    instructions = tk.Button(root, text="Click this button to get instructions about the game", font="Times 20", bg=BACKGROUND, fg = TEXTCOLOR, command=play_game)
    instructions.pack()

def play_game():
    clear_screen(root)
    
    next_label = tk.Label(root, text="Now the game should start", font="Times 32", bg=BACKGROUND, fg = TEXTCOLOR)
    next_label.pack()
    

    

def main():
	first_page()

main()

root.mainloop()

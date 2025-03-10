import random
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

# splash screen
def main():
    home = tk.Tk()

    height = 430
    width = 530
    x = (home.winfo_screenwidth() // 2) - (width // 2)
    y = (home.winfo_screenheight() // 2) - (height // 2)
    home.geometry(f'{width}x{height}+{x}+{y}')
    home.overrideredirect(True)
    home.config(background="#2F6C60")
    
    sub_label = tk.Label(home, text="SCISSORS", bg="#2F6C60", font=("Showcard Gothic", 45, "bold"), fg="#FFFFFF")
    sub_label.place(x=60, y=135)

    welcome_label = tk.Label(home, text="ROCK", bg="#2F6C60", font=("Showcard Gothic", 55, "bold"), fg="light grey")
    welcome_label.place(x=150, y=70)

    sub_label = tk.Label(home, text="PAPER", bg="#2F6C60", font=("Kristen ITC", 15, "bold"), fg="#FFFFFF")
    sub_label.place(x=335, y=125)
    
    progress_label = tk.Label(home, text="Loading....", font=("Trebuchet MS", 10, "bold"), fg="black", bg="white")
    progress_label.place(x=5, y=400)

    progress_style = ttk.Style()
    progress_style.configure("red.Horizontal.TProgressbar", background="#108cff")

    progress = ttk.Progressbar(home, orient=tk.HORIZONTAL, length=530, mode='determinate', style="red.Horizontal.TProgressbar")
    progress.place(x=0, y=423)

    def load():
        for i in range(101):
            progress['value'] = i
            home.update_idletasks()
            home.after(50)  # Simulate a delay
            

        home.destroy()
        start_game()

    home.after(1000, load)  # Start loading after 1 second
    home.mainloop()

# game 
def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "You win!"
    else:
        return "You lose!"

def play_game(user_choice):
    computer_choice = get_computer_choice()
    result = determine_winner(user_choice, computer_choice)

    result_label.config(text=f"You chose: {user_choice}\nComputer chose: {computer_choice}\n{result}")

    if result == "You win!":
        scores['user'] += 1
    elif result == "You lose!":
        scores['computer'] += 1

    score_label.config(text=f"Score - You: {scores['user']}, Computer: {scores['computer']}")

def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.destroy()

def start_game():
    global root, result_label, score_label, scores

    root = tk.Tk()
    root.title("Rock Paper Scissors")

    height = 430
    width = 530
    x = (root.winfo_screenwidth() // 2) - (width // 2)
    y = (root.winfo_screenheight() // 2) - (height // 2)
    root.geometry(f'{width}x{height}+{x}+{y}')
    root.overrideredirect(False)
    root.config(background="#2F6C60")

    scores = {'user': 0, 'computer': 0}

    frame = tk.Frame(root)
    frame.pack(pady=20)

    rock_button = tk.Button(frame, text="Rock",  bg="#2F6C60", command=lambda: play_game("rock"))
    rock_button.grid(row=0, column=0, padx=10, sticky="nsew")

    paper_button = tk.Button(frame, text="Paper", command=lambda: play_game("paper"))
    paper_button.grid(row=0, column=1, padx=10, sticky="nsew")

    scissors_button = tk.Button(frame, text="Scissors", command=lambda: play_game("scissors"))
    scissors_button.grid(row=0, column=2, padx=10, sticky="nsew")

    frame.grid_columnconfigure(0, weight=1)
    frame.grid_columnconfigure(1, weight=1)
    frame.grid_columnconfigure(2, weight=1)

    result_label = tk.Label(root, text="", font=("Helvetica", 14))
    result_label.pack(pady=20, expand=True)

    score_label = tk.Label(root, text="Score - You: 0, Computer: 0", font=("Helvetica", 14))
    score_label.pack(pady=20, expand=True)

    root.protocol("WM_DELETE_WINDOW", on_closing)
    root.mainloop()

if __name__ == "__main__":
    main()
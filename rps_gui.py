rps_gui.py
mport tkinter as tk
import random
from tkinter import messagebox

choices = ["Rock", "Paper", "Scissors"]
emojis = {"Rock": "✊", "Paper": "✋", "Scissors": "✌️"}
player_score = 0
computer_score = 0
player_name = ""

def start_game():
    global player_name
    player_name = name_entry.get().strip()
    if not player_name:
        messagebox.showwarning("Name Required", "Please enter your name to start.")
        return
    start_frame.pack_forget()
    game_frame.pack(pady=20)

def play(player_choice):
    global player_score, computer_score
    computer_choice = random.choice(choices)

    player_label.config(text=f"{player_name}: {emojis[player_choice]}")
    computer_label.config(text=f"Computer: {emojis[computer_choice]}")

    if player_choice == computer_choice:
        result_label.config(text="It's a tie!", fg="blue")
    elif (player_choice == "Rock" and computer_choice == "Scissors") or \
         (player_choice == "Paper" and computer_choice == "Rock") or \
         (player_choice == "Scissors" and computer_choice == "Paper"):
        result_label.config(text="You win this round!", fg="green")
        player_score += 1
    else:
        result_label.config(text="Computer wins this round!", fg="red")
        computer_score += 1

    score_label.config(text=f"Score: {player_name} {player_score} - {computer_score} Computer")

    if player_score == 3 or computer_score == 3:
        if player_score > computer_score:
            result_label.config(text=f"🎉 {player_name} won the match!", fg="green")
        else:
            result_label.config(text="💻 Computer won the match!", fg="red")
        disable_buttons()

def disable_buttons():
    for btn in buttons:
        btn.config(state="disabled")

def reset_game():
    global player_score, computer_score
    player_score = 0
    computer_score = 0
    player_label.config(text=f"{player_name}: ")
    computer_label.config(text="Computer: ")
    result_label.config(text="Make your move!", fg="black")
    score_label.config(text=f"Score: {player_name} 0 - 0 Computer")
    for btn in buttons:
        btn.config(state="normal")

root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("450x500")
root.config(bg="#fafafa")

start_frame = tk.Frame(root, bg="#fafafa")
start_frame.pack(pady=50)

tk.Label(start_frame, text="Enter Your Name:", font=("Arial", 16), bg="#fafafa").pack(pady=10)
name_entry = tk.Entry(start_frame, font=("Arial", 16))
name_entry.pack(pady=5)
tk.Button(start_frame, text="Start Game", font=("Arial", 14), bg="#4CAF50", fg="white",
          command=start_game).pack(pady=20)

game_frame = tk.Frame(root, bg="#fafafa")

title_label = tk.Label(game_frame, text="Rock Paper Scissors", font=("Arial", 22, "bold"), bg="#fafafa")
title_label.pack(pady=10)

button_frame = tk.Frame(game_frame, bg="#fafafa")
button_frame.pack(pady=10)

buttons = []
for choice in choices:
    btn = tk.Button(button_frame, text=choice, font=("Arial", 14), width=10,
                    bg="#333", fg="white", command=lambda c=choice: play(c))
    btn.pack(side="left", padx=5)
    buttons.append(btn)

player_label = tk.Label(game_frame, text="You: ", font=("Arial", 16), bg="#fafafa")
player_label.pack(pady=10)

computer_label = tk.Label(game_frame, text="Computer: ", font=("Arial", 16), bg="#fafafa")
computer_label.pack(pady=10)

result_label = tk.Label(game_frame, text="Make your move!", font=("Arial", 16), bg="#fafafa")
result_label.pack(pady=10)

score_label = tk.Label(game_frame, text="Score: 0 - 0", font=("Arial", 16), bg="#fafafa")
score_label.pack(pady=10)

reset_btn = tk.Button(game_frame, text="Reset Game", font=("Arial", 14), bg="#2196F3", fg="white",
                      command=reset_game)
reset_btn.pack(pady=10)

root.mainloop()
Add Rock-Paper-Scissors GUI code

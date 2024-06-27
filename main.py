"""
This file is for our new theme: Who wants to be a millionaire game
Create by: Miqayel Postoyan
Date: 28 jun
"""
from tkinter import *
import random


def restart_game_window(game_over_window):
    """
    Function: restart_game_window
    Brief: Restarts the game window after game over.
    Params:
        game_over_window (Tk): The window to destroy.
    Return: None
    """
    game_over_window.destroy()
    start_main()


def show_game_result(root, user_name, won):
    """
    Function: show_game_result
    Brief: Shows game result (win or lose), updates records, and displays top 10 records.
    Params:
        root (Tk): Main game window to destroy.
        user_name (str): User's name.
        won (bool): True if user won, False otherwise.
    Return: None
    """
    root.destroy()
    over = Tk()
    over.title('Who Wants to Be a Millionaire')
    over.geometry('800x500+200+200')
    over.config(bg="#101E39")
    over.resizable(width=False, height=False)

    earnings_index = len(monetary_scale_labels) - coin[0] if 0 <= len(monetary_scale_labels) - coin[0] < len(monetary_scale_labels) else 0
    earnings = monetary_scale_labels[earnings_index]

    if won:
        win_label = Label(over, text="Congratulations, You Win!", font=("Helvetica", 27), bg="#101E39", fg="white")
        win_label.place(x=100, y=150)
    else:
        lose_label = Label(over, text=f"You lose {earnings} $", font=("Helvetica", 30), bg="#101E39", fg="white")
        lose_label.place(x=120, y=150)

    with open("record.txt", "a") as f:
        f.write(f"{user_name} {earnings} $\n")

    with open("record.txt", "r") as f:
        records = f.readlines()

    sorted_records = sorted(records, key=lambda x: int(x.split(' ')[1].replace('.', '')), reverse=True)
    top_10_records = sorted_records[:10]

    with open("record.txt", "w") as f:
        f.writelines(sorted_records)

    records_label = Label(over, text="Top 10 Records:", font=("Helvetica", 20), bg="#101E39", fg="white")
    records_label.place(x=550, y=30)

    records_text = Text(over, font=("Helvetica", 17), bg="#101E39", fg="white", relief=FLAT)
    records_text.place(x=570, y=70, relwidth=0.8, relheight=0.6)
    records_text.insert("1.0", ''.join(top_10_records))
    records_text.config(state=DISABLED)

    restart_button = Button(over, text="Restart", font=("Helvetica", 20), bg="#204A94", fg="white", command=lambda: restart_game_window(over))
    restart_button.place(x=200, y=300)

    exit_button = Button(over, text="Exit", font=("Helvetica", 20), bg="#204A94", fg="white", command=over.destroy)
    exit_button.place(x=330, y=300)

    over.mainloop()


def check_answer(button_text, correct_answer, coin, root):
    """
    Function: check_answer
    Brief: Checks if the selected answer is correct and updates game state accordingly.
    Params:
        button_text (str): Text of the selected button.
        correct_answer (str): Correct answer for the current question.
        coin (list): List containing the number of correct answers.
        root (Tk): Main game window.
    Return: None
    """
    if button_text == correct_answer:
        coin[0] += 1
        move_character(character_label, character_vertical_position)
        if coin[0] == 10:
            show_game_result(root, user_name, won=True)
    else:
        show_game_result(root, user_name, won=False)


def handle_next_question(root, selected_answer, correct_answer, coin):
    """
    Function: handle_next_question
    Brief: Handles the logic after selecting an answer (check correctness, move character, show result).
    Params:
        root (Tk): Main game window.
        selected_answer (str): Answer chosen by the player.
        correct_answer (str): Correct answer for the current question.
        coin (list): List containing the number of correct answers.
    Return: None
    """
    check_answer(selected_answer, correct_answer, coin, root)
    display_question(root)


def display_question(root):
    """
    Function: display_question
    Brief: Displays a random question with multiple-choice answers.
    Params:
        root (Tk): Main game window.
    Return: None
    """
    main_frame = Frame(root, bg="#101E39", highlightcolor="#4D5057")
    main_frame.place(x=0, y=60, relwidth=0.75, relheight=0.9)

    question = random.choice(questions_list)
    questions_list.pop(questions_list.index(question))
    question_text = question[0]

    questions_label = Text(main_frame, font=("Helvetica", 20), bg="#101E39", fg="white", relief=FLAT)
    questions_label.place(x=70, y=150, relwidth=0.8, relheight=0.2)
    questions_label.insert("1.0", question_text)
    questions_label.tag_configure("center", justify='center')
    questions_label.tag_add("center", "1.0", "end")
    questions_label.config(state=DISABLED)

    button1 = Button(main_frame, text=question[1], font=("Helvetica", 20), bg="#101E39", fg="white",
                     command=lambda: handle_next_question(root, question[1], question[5], coin))
    button1.place(relx=0.1, rely=0.5)

    button2 = Button(main_frame, text=question[2], font=("Helvetica", 20), bg="#101E39", fg="white",
                     command=lambda: handle_next_question(root, question[2], question[5], coin))
    button2.place(relx=0.6, rely=0.5)

    button3 = Button(main_frame, text=question[3], font=("Helvetica", 20), bg="#101E39", fg="white",
                     command=lambda: handle_next_question(root, question[3], question[5], coin))
    button3.place(relx=0.1, rely=0.7)

    button4 = Button(main_frame, text=question[4], font=("Helvetica", 20), bg="#101E39", fg="white",
                     command=lambda: handle_next_question(root, question[4], question[5], coin))
    button4.place(relx=0.6, rely=0.7)


def move_character(character_label, character_vertical_position):
    """
    Function: move_character
    Brief: Moves a character label vertically on the screen.
    Params:
        character_label (Label): Label representing the character.
        character_vertical_position (list): List containing the vertical position of the character.
    Return: None
    """
    character_vertical_position[0] -= 50
    character_label.place(x=5, y=character_vertical_position[0])


def display_monetary_scale(root):
    """
    Function: display_monetary_scale
    Brief: Displays a monetary scale on the right side of the game window.
    Params:
        root (Tk): Main game window.
    Return: None
    """
    global monetary_scale_labels
    monetary_scale_labels = ["5.000.000", "3.000.000", "1.000.000", "750.000", "500.000", "125.000", "64.000", "16.000", "5.000", "1.000"]
    main_frame = Frame(root, bg="#204A94", highlightcolor="#4D5057")
    main_frame.place(relx=0.75, y=0, relwidth=0.25, relheight=1)

    for index, amount in enumerate(monetary_scale_labels):
        label = Label(main_frame, text=f"{len(monetary_scale_labels) - index}.     {amount}", bg="#204A94", fg="#B8C4BD", font=("Helvetica", 14))
        label.pack(anchor='w', padx=30, pady=10)

    global character_vertical_position
    character_vertical_position = [450]

    global character_label
    character_label = Label(main_frame, text="⮕")
    character_label.place(x=5, y=character_vertical_position[0])


def start_game(main_menu):
    """
    Function: start_game
    Brief: Starts the game after getting user input (name).
    Params:
        main_menu (Tk): Main menu window.
    Return: None
    """
    global user_name
    user_name = name_entry_field.get()
    main_menu.destroy()
    game_window = Tk()
    game_window.title('Who Wants to Be a Millionaire')
    game_window.geometry('800x500+200+200')
    game_window.config(bg="#101E39")
    game_window.resizable(width=False, height=False)

    display_monetary_scale(game_window)
    display_question(game_window)

    game_window.protocol("WM_DELETE_WINDOW", lambda: show_game_result(game_window, user_name, won=False))

    game_window.mainloop()


def display_main_menu():
    """
    Function: display_main_menu
    Brief: Displays the main menu where the user can enter their name and start the game.
    Params: None
    Return: None
    """
    main_menu = Tk()
    main_menu.title('Who Wants to Be a Millionaire')
    main_menu.geometry('800x500+200+200')
    main_menu.config(bg="#474B82")
    main_menu.resizable(width=False, height=False)

    name_label = Label(main_menu, text="Your name⬇", font=("Helvetica", 35), bg="#474B82", fg="#FFFFFF")
    name_label.place(relx=0.3, rely=0.3)

    global name_entry_field
    name_entry_field = Entry(main_menu, bg="#FFFFFF", width=41, highlightthickness=5, highlightcolor="#8CA4C2")
    name_entry_field.place(relx=0.3, rely=0.45)

    play_button = Button(main_menu, text="Play game", bg="#99B2DA", height=1, width=12, font=("Helvetica", 15),
                         command=lambda: start_game(main_menu))
    play_button.place(x=300, y=270)

    main_menu.mainloop()


def load_questions_from_file():
    """
    Function: load_questions_from_file
    Brief: Loads questions from a file into a list.
    Params: None
    Return: List of questions and answers.
    """
    questions_list = []
    with open("a.txt") as f:
        for line in f:
            questions_list.append(line.strip().split('-'))
    return questions_list


def start_main():
    """
    Function: start_main
    Brief: Starts the main function to initialize the game.
    Params: None
    Return: None
    """
    global questions_list
    questions_list = load_questions_from_file()
    global coin
    coin = [1]
    display_main_menu()


if __name__ == "__main__":
    """
    Function: main
    Brief: Entry point of the program.
    """
    start_main()

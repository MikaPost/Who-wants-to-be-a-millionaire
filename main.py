from tkinter import *
import random


def get_list_questions():
    list_questions = []
    with open("a.txt") as f:
        for line in f:
            list_questions.append(line.strip().split('-'))
    return list_questions


# def mama(slak, slak_ver):
#     slak_ver[0] -= 50
#     slak.place(x=5, y=slak_ver[0])


def monetary_scale(root):
    ml = ["5.000.000", "3.000.000", "1.000.000", "750.000", "500.000", "125.000", " 64.000", "16.000", "5.000", "1.000"]
    div = Frame(root, bg="#204A94", highlightcolor="#4D5057")
    div.place(relx=0.75, y=0, relwidth=0.25, relheight=1)

    for index, amount in enumerate(ml):
        label = Label(div, text=f"{len(ml) - index}.     {amount}", bg="#204A94", fg="#B8C4BD", font=("Helvetica", 14))
        label.pack(anchor='w', padx=30, pady=10)

    # slak_ver = [460]
    #
    # slak = Label(div, text="⮕")
    # slak.place(x=5, y=slak_ver[0])
    #
    # button = Button(root, text="123", width=5, font=("Helvetica", 15), command=lambda: mama(slak, slak_ver))
    # button.place(x=100, y=340)


def true_or_wrong(button_text, correct_answer, coin):
    if button_text == correct_answer:
        coin[0] += 1
    else:
        exit()


def next_question(root, selected_answer, correct_answer, coin):
    true_or_wrong(selected_answer, correct_answer, coin)
    questions(root)


def questions(root):
    div = Frame(root, bg="#101E39", highlightcolor="#4D5057")
    div.place(x=0, y=60, relwidth=0.75, relheight=0.9)

    question = random.choice(list_questions)
    list_questions.pop(list_questions.index(question))
    question_text = question[0]

    # Create a Text widget to handle multiline questions
    questions_label = Text(div, font=("Helvetica", 20), bg="#101E39", fg="white", relief=FLAT)
    questions_label.place(x=70, y=150, relwidth=0.8, relheight=0.2)  # Adjust relwidth to leave space

    questions_label.insert("1.0", question_text)
    questions_label.tag_configure("center", justify='center')
    questions_label.tag_add("center", "1.0", "end")
    questions_label.config(state=DISABLED)

    button1 = Button(div, text=question[1], font=("Helvetica", 20), bg="#101E39", fg="white",
                     command=lambda: next_question(root, question[1], question[5], coin))
    button1.place(relx=0.2, rely=0.5)

    button2 = Button(div, text=question[2], font=("Helvetica", 20), bg="#101E39", fg="white",
                     command=lambda: next_question(root, question[2], question[5], coin))
    button2.place(relx=0.6, rely=0.5)

    button3 = Button(div, text=question[3], font=("Helvetica", 20), bg="#101E39", fg="white",
                     command=lambda: next_question(root, question[3], question[5], coin))
    button3.place(relx=0.2, rely=0.7)

    button4 = Button(div, text=question[4], font=("Helvetica", 20), bg="#101E39", fg="white",
                     command=lambda: next_question(root, question[4], question[5], coin))
    button4.place(relx=0.6, rely=0.7)


def game(user_name, menu):
    menu.destroy()
    root = Tk()
    root.title('Who Wants to Be a Millionaire')
    root.geometry('800x500+200+200')
    root.config(bg="#101E39")
    root.resizable(width=False, height=False)

    monetary_scale(root)
    questions(root)

    # button = Button(root, text="50/50", width=5, font=("Helvetica", 15))
    # button.place(x=10, y=10)

    root.mainloop()


def root_menu():
    menu = Tk()
    menu.title('Who Wants to Be a Millionaire')
    menu.geometry('800x500+200+200')
    menu.config(bg="#474B82")
    menu.resizable(width=False, height=False)

    # Label for user prompt
    name_label = Label(menu, text="Your name⬇", font=("Helvetica", 35), bg="#474B82", fg="#FFFFFF")
    name_label.place(relx=0.3, rely=0.3)

    # Entry widget for user input
    name_entry = Entry(menu, bg="#FFFFFF", width=41, highlightthickness=5, highlightcolor="#8CA4C2")
    name_entry.place(relx=0.3, rely=0.45)

    # Button to start the game
    play_button = Button(menu, text="Play game", bg="#99B2DA", height=1, width=12, font=("Helvetica", 15),
                         command=lambda: game(name_entry.get(), menu))
    play_button.place(x=300, y=270)

    # game(name_entry.get(), menu)

    menu.mainloop()


def main():
    global list_questions
    list_questions = get_list_questions()
    global coin
    coin = [0]
    root_menu()


if __name__ == "__main__":
    main()

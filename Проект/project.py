from tkinter import *
from tkinter import ttk
from colorama import Fore, Back, Style
import random

print(Fore.RED + """░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░▄▄▄▄▄▄░░░░░░░░░░░░░░░░░░░
░░░░░▄█████████▄▄░░░░░░░░▄▄░░░░░
░░░░███████████████▄▄░░░░▄██▄░░░
░░░▄█████████████████████████░░░
░▄██████████████████████████▀░░░
░███░░░░░░░░░░░░░░░░░░░█░░░░░░░░
░███░███████████████████░░░░░░░░
░███░░▀████───████────█▀░░░░░░░░
░███░░░▀▄▄▄▄▄▀░▀▄▄▄▄▄▀▀▀▄░░░░░░░
░░██░░░░░░░░░░░░░░░░░░░░░▀▄░░░░░
░░▄█░░░░░▄▀█▀▀▀▄▄▄░░░░░▄▀░░▀▄░░░
░█░░░░░▄▀──█───█──▀█▄▄░▀▀░░░░▀▄░
░▀▄▄░░█────█───█───█──▀▀▄░░▄▀▀▀░
░░░█░██▄▄▄▄█▄▄▄█▄▄▄█▄▄▄▄▄█▄▄▀░░░
░░░█░█████████████▄▄░░░░░░░░░░░░
░░░█░█████████████████████████▄░
░░░█░███████████████▀▀░░░░░░░░█░
░░░█░██████████▀▀░░░░░░░░░░░░░█░
░░░█░██████▀░░░░░░░░░░░░░░░░░░█░
░░░█░███▀░░░░░░░░░░░░░░░░░░░░░█░
░░░█░█▀░░░░░░░░░░░░░░░░░░░░░░░█░
░░░█░░░░░░░░░░░░░░▀▄░▀▄░░░░░░░█░
░░░█░░░░░░░░░░░░▄▄▄▀▄▄▀░░░░░░░█░
░░░█░░░░░░░░░░░░░░░░░░░░░░░░░░█░
░░░█░░░░░░░░░░░░░░░░░░░░░░░░░░█░
░░░█░░░░░░░░░░░░░░░░░░░░░░░░░░█░
░░░█░░░░░░░░░░░░░░░░░░░░░░░░░░█░
░░░█░░░░░░░░░░░░░░░░░░░░░░░░░░█░
░░░█░░░░░░░░░░░░░░░░░░░░░░░░░░█░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░█▀▄░█░█▄░█░█░█░█░░█▀░█▀▄░█▀░█▀▄░▄▀▀░█░
░█░█░█░█▀██░█▀▄░█░░█▀░█▀▄░█▀░█▀▄░█░█░▀░
░▀▀░░▀░▀░░▀░▀░▀░▀▀░▀▀░▀▀░░▀▀░▀░▀░░▀▀░▀░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
""")

chars = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
upper_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lowwer_letters = 'abcdefghijklnopqrstuvwxyz'
numbers_chars = '0123456789'
special_chars = '+-/*!&$#?=@<>'

program = Tk()
program.title('Магнум опус.')
program.config(bg = 'lightgray')
program.geometry("+400+200")
program.resizable(False, True)

main_txt= Label(program, text="PassGenerator", font=("Arial Bold", 40))
main_txt.grid(column=0, row=0, padx=10)
small_txt= Label(program, text="PassGenerator - программа для создания уникальных паролей с учётом параметров", font=("Arial Bold", 15))
small_txt.grid(column=0, row=1, padx=10)

def main():
    count = message.get()
    randomizer = 0
    password = ''
    while count != 0:
        randomizer = random.randint(1, 4)
        randomizer = str(randomizer)
        if randomizer == '1':
            if numbers.get() == 1:
                password += str(random.randint(0, 9))
                count -= 1
        elif randomizer == '2':
            if big_letter.get() == 1:
                password += random.choice(upper_letters)
                count -= 1
        elif randomizer == '3':
            if small_letter.get() == 1:
                password += random.choice(lowwer_letters)
                count -= 1
        elif randomizer == '4':
                if special_letter.get() == 1:
                    password += random.choice(special_chars)
                    count -= 1
    print(password)
    result["text"] = password


def select_01():
    numbers_alg = 0
    print('Числа отключены')


def select_02():
    big_letters = 0
    print('Заглавные буквы отключены')


def select_03():
    small_letters = 0
    print('Строчные буквы отключены')


def select_04():
    special_letters = 0
    print('Специальные символы отключены')


numbers_alg = 'y'
big_letters = 'y'
small_letters = 'y'
special_letters = 'y'


numbers = IntVar()
check_numbers = ttk.Checkbutton(variable=numbers, text="Числа")
check_numbers.grid(column=0, row=2, ipadx=10, pady=5)
big_letter = IntVar()
check_big_letter = ttk.Checkbutton(variable=big_letter, text="Заглавные буквы ")
check_big_letter.grid(column=0, row=3, ipadx=10, pady=5)
small_letter = IntVar()
check_small_letter = ttk.Checkbutton(variable=small_letter, text="Строчные буквы ")
check_small_letter.grid(column=0, row=4, ipadx=10, pady=5)
special_letter = IntVar()
check_special_chars = ttk.Checkbutton(variable=special_letter, text="Специальные символы ")
check_special_chars.grid(column=0, row=5, ipadx=10, pady=5)


smaller_txt= Label(program, text="Ввод длины:", font=("Arial Bold", 15))
smaller_txt.grid(column=0, row=6, padx=10)
message = IntVar()
lenght = Entry(program, width=10, textvariable=message)
lenght.grid(column=0, row=7)
lenght.pack


btn = ttk.Button(text="Сгенерировать", command=main)
btn.grid(column=0, row=8, ipadx=10, pady=5)


result = Label(program, text='', font=("Arial Bold", 15))
result.grid(column=0, row=9, padx=10)


program.mainloop()


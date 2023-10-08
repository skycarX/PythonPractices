import random

lenght = int(input())
numbers = input('y/n') #1
big_letters = input('y/n') #2
small_letters = input('y/n') #3
special_letters = input('y/n' ) #4

chars = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
upper_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lowwer_letters = 'abcdefghijklnopqrstuvwxyz'
numbers_chars = '0123456789'
special_chars = '+-/*!&$#?=@<>'

randomizer = 0
password = ''
for i in range(lenght):
    randomizer = random.randint(1, 4)
    randomizer = str(randomizer)
    if randomizer == '1':
        if numbers == 'y':
            password += str(random.randint(0, 9))
    elif randomizer == '2':
        if big_letters == 'y':
            password += random.choice(upper_letters)
    elif randomizer == '3':
        if small_letters == 'y':
            password += random.choice(lowwer_letters)
    elif randomizer == '4':
            if special_letters == 'y':
                password += random.choice(special_chars)
print(password)
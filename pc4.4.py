import random
import string


def generate_random_string(length):
    letters = string.ascii_lowercase
    rand_string = ''.join(random.choice(letters) for i in range(length))
    print("Сгенерированная строка из ", length, "символов:", rand_string)

def user_symbol():
	symbol=str(input("Введите символ: "))


generate_random_string(8)
user_symbol()

from colorama import Fore, Back, Style
import words
import random
answer = random.choice(words.ukrainian_words)
user = input("Введіть слово\n")
result = Fore.BLACK + ""
limit = 6
while limit != 0:
    limit -=1
    for i in range(5):
        if user[i] == answer[i]:
            result += Back.GREEN + user[i]  + " "
        elif user[i] in answer:
            result += Back.YELLOW + user[i] + " "
        else:
            result += Style.RESET_ALL  + user[i] + " " + Fore.BLACK

    print (result + Style.RESET_ALL)
    if answer == user:
        break
    user = input("Введіть слово\n")
    result = Fore.BLACK + ""
if limit == 0:
    print("Ви програли")
    print("Загадане слово", answer)
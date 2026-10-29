
import random

choices = ["камінь", "ножиці", "папір"]

while True:
   
    user = input("\nОберіть камінь, ножиці, папір або стоп: ").lower()

    
    if user == "стоп":
        print("Гру завершено!")
        break

    
    if user not in choices:
        print("Помилка! Невірний вибір.")
        continue

    
    computer = random.choice(choices)

    print("Ваш вибір:", user)
    print("Вибір комп'ютера:", computer)

    
    if user == computer:
        print("Нічия!")

    elif (
        (user == "камінь" and computer == "ножиці") or
        (user == "ножиці" and computer == "папір") or
        (user == "папір" and computer == "камінь")
    ):
        print("Ви перемогли!")

    else:
        print("Комп'ютер переміг!")


import functions
import operations


while True:
    choice = input("\nНатисніть Enter для обчислення або стоп для виходу: ")

    if choice.lower() == "стоп":
        print("Програму завершено.")
        break

    operations.calculate()

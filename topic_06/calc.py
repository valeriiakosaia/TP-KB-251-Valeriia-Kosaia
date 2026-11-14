import functions
import operations
import logging

logging.basicConfig(
    filename="topic_06/calculator.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s",
    encoding="utf-8"
)

while True:
    choice = input("\nНатисніть Enter для обчислення або стоп для виходу: ")

    if choice.lower() == "стоп":
        logging.info("Програму завершено")
        print("Програму завершено.")
        break

    operations.calculate()

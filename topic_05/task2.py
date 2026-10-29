
import requests

url = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json"


currencies = ["EUR", "USD", "PLN"]

while True:
    currency = input("\nОберіть валюту (EUR, USD, PLN) або стоп: ").upper()

   
    if currency == "СТОП":
        print("Програму завершено!")
        break

   
    if currency not in currencies:
        print("Помилка! Невірна валюта.")
        continue

   
    try:
        amount = float(input("Введіть суму: ").replace(",", "."))

        if amount < 0:
            print("Сума не може бути від'ємною!")
            continue

    except ValueError:
        print("Помилка! Введіть число.")
        continue

   
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()

       
        for item in data:
            if item["cc"] == currency:
                rate = item["rate"]
                date = item["exchangedate"]
                break
        else:
            print("Курс валюти не знайдено!")
            continue
    
        result = amount * rate

        print("Дата курсу:", date)
        print("Курс 1", currency, "=", rate, "грн")
        print(amount, currency, "=", round(result, 2), "грн")

    except requests.exceptions.RequestException:
        print("Помилка підключення до НБУ!")
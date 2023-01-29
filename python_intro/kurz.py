import httpx

url = "https://www.cnb.cz/cs/financni-trhy/devizovy-trh/kurzy-devizoveho-trhu/kurzy-devizoveho-trhu/denni_kurz.txt"
res = httpx.get(url)
rows = res.text.split("\n")

rows = rows[2:-1]

data = {}

for r in rows:
    cols = r.split("|")
    curr = cols[-2]
    rate = cols[-1]
    amount = cols[-3]
    rate = rate.replace(",", ".")
    rate = float(rate)
    amount = float(amount)
    rate = rate / amount
    data[curr] = rate

exchange = input("Z cizi na CZK => a \nZ CZK na cizi => b\na/b: ")

if exchange == "a":
    user_curr = input("\nZadej pocatecni menu: ")
    user_amount = input(f"Zadej castku v {user_curr}: ")

    user_amount = float(user_amount)

    result = user_amount * data[user_curr]
    result = round(result, 2)
    print(f"Vysledna castka je {result} CZK")

elif exchange == "b":
    user_amount = input("\nZadej castku v CZK: ")
    user_amount = float(user_amount)
    user_curr = input("Zadej cilovou menu: ")

    result = (user_amount / data[user_curr])
    result = round(result, 2)
    print(f"Vysledna castka je {result} {user_curr}")
else:
    print(":(")

print("\n\nVlastni vylepseni: 🐈")

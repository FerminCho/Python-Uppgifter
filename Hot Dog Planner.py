import math

product_cost = {
    "Hotdog package": 20.95,
    "Vegan hotdog package": 34.95,
    "Drink": 13.95
}

print("       Hot Dog Planner")
print("----------------------------")

print("How many students wants:\n")
two_hotdogs = int(input("Two ordinary hotdogs? "))
print("")
three_hotdogs = int(input("Three ordinary hotdogs? "))
two_vegan_hotdogs = int(input("Two vegan hotdogs? "))
three_vegan_hotdogs = int(input("Three vegan hotdogs? "))

hotdogs = (two_hotdogs * 2) + (three_hotdogs * 3)
vegan_hotdogs = (two_vegan_hotdogs * 2) + (three_vegan_hotdogs * 3)
number_of_students = two_hotdogs + three_hotdogs + two_vegan_hotdogs + three_vegan_hotdogs

number_of_hotdog_packages = math.ceil(hotdogs / 8)
number_of_vegan_hotdog_packages = math.ceil(vegan_hotdogs / 4)

hotdogs_cost = number_of_hotdog_packages * product_cost["Hotdog package"]
vegan_hotdogs_cost = number_of_vegan_hotdog_packages * product_cost["Vegan hotdog package"]
drinks_cost = number_of_students * product_cost["Drink"]

full_cost = math.ceil((hotdogs_cost + vegan_hotdogs_cost + drinks_cost) * 100) / 100

items = [
    {"amount": number_of_hotdog_packages, "item": "HOT DOGS", "cost": round(hotdogs_cost, 2)},
    {"amount": number_of_vegan_hotdog_packages, "item": "VEGAN", "cost": round(vegan_hotdogs_cost, 2)},
    {"amount": number_of_students, "item": "DRINKS", "cost": round(drinks_cost, 2)},
]


print("-" * 28)
print("AMOUNT  ITEM            COST")
i = 0
for row in items:
    cost_str = str(row["cost"]).rstrip('0').rstrip('.')
    length = 16 - len(str(row["amount"]))
    print(f"{row["amount"]:<{len(str(row["amount"]))}} {row["item"]:<{str(length)}} {cost_str:>9}")
    i += 1
cost = str(full_cost).rstrip('0').rstrip('.')
print("-" * 28)
print("TOTAL: " + cost + ":-")


print("")
print("Lista zakupów:")

shopping_list = {
    "Piekarnia" : ["chleb", "bułki", "ciasto", "tort"],
    "Warzywniak" : ["marchew", "seler", "rukola", "ziemniaki", "pietruszka"]
}


print(f"{shopping_list}")
print("")
shopping_list_len = 0

for shop in shopping_list:
    shopping_list_len = len(shopping_list.get(shop)) + shopping_list_len
    print(f"Idę do {shop}, kupuję tu następujące rzeczy: {shopping_list.get(shop)}")

print("")

for shop in shopping_list:
    shopping_list_upper = [word.upper() for word in shopping_list.get(shop)]
    print(f"Idę do {shop.upper()}, kupuję tu następujące rzeczy: {shopping_list_upper}")

print("")

print(f"W sumie kupuję {shopping_list_len} produktów.")
print("")

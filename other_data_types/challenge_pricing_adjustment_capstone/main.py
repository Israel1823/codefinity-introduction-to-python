# Inventário de supermercado
grocery_inventory = {
    "Milk": ("Dairy", 3.50, 8),
    "Eggs": ("Dairy", 5.50, 30),
    "Bread": ("Bakery", 2.99, 15),
    "Apples": ("Produce", 1.50, 50)
}

# Obter o preço dos ovos
eggs_price = grocery_inventory["Eggs"][1]

# Verificar se o preço é maior que 5
if eggs_price > 5:
    print("Eggs are too expensive, reducing the price by $1.")
    # Reduzir o preço em 1 (mantendo categoria e quantidade)
    grocery_inventory["Eggs"] = ("Dairy", eggs_price - 1, grocery_inventory["Eggs"][2])
else:
    print("The price of Eggs is reasonable.")

# Mostrar inventário atualizado
print("Updated Inventory:", grocery_inventory)
# Adicionar "Tomatoes"
grocery_inventory.update({"Tomatoes": ( "Produce", 1.20, 30,)})
# Mostrar inventário atualizado
print ("Inventory after adding Tomatoes:", grocery_inventory)
#Chequando o estoque do leite
milk_stock = grocery_inventory["Milk"][2]
if milk_stock < 10:
    print("Milk needs to be restocked. Increasing stock by 20 units.")
    grocery_inventory["Milk"] = (
        grocery_inventory["Milk"][0],
        grocery_inventory["Milk"][1],
        milk_stock + 20,
    )
else:
    print("Milk has sufficient stock.")
#Vereficando o preço da maça
apples_price = grocery_inventory ["Apples"][1]
if apples_price >2:
    print("Apples removed the stock are expensive")
    print("Invetory updated", grocery_inventory)
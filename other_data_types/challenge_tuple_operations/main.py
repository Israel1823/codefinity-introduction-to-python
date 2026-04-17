# Current inventory on shelf
shelf = ("apples", "oranges", "bananas", "apples", "grapes", "bananas", "apples")

#task 1 count quantity apples
apple_count = shelf.count("apples")
print("Number of Apples:", shelf.count ("apples"))
#task 2 count the first banana quantity
banana_index = shelf.index ("bananas")
print ("First Banana Index:", (banana_index))
#task 3 Check if the number of apples is less than 5.
apples = shelf.count ("apples")
if apples <5:
    print("Apples need to be restocked.")
else:
    print("Apples are sufficiently stocked.")
    #task 4 Check if the number of grapes?
grapes = shelf.count ("grapes")
if grapes <2:
    print("Grapes need to be restocked.")
else:
    print("Grapes are sufficiently stocked.")
   #task 5 Check if the number of orage?
if "oranges" in shelf:
    orange_index = shelf.index ("oranges")
    print("Oranges are at index:", (orange_index))
else:
    print("Oranges are out of stock.")
#task 6 Check if the number of stock!
print("Number of Apples:", (apples))
print("First Banana Index:", (banana_index))

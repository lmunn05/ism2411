# Self assesment questions 
# 1. One thing that surprised me about Python lists is how easily you can manipulate and organize data. I didn't realize that you could add, remove, sort, and access specific items using just a few lines of code. It makes working with larger amounts of information much more efficient.

# 2. One business situation where Python lists could be useful is managing inventory at a retail store. Instead of manually tracking products and updating quantities in Excel, you could use Python lists to organize products, identify items that are running low, and calculate inventory totals. This could save time and reduce the amount of manual work involved in keeping track of inventory.

# Exercise 1 : build a list

print("-- Exercise 1 : Build a List --")

inventory = ["pen", "notebook", "stapler", "tape", "marker"]
print(inventory)
print(len(inventory))

# Excercise 2 

print("--- Excercise 2: Index Practice--- ")
print(inventory[0])
print(inventory[-1])

middle = len(inventory) // 2 
print(inventory[middle])

# Excercise 3 

print("-- Exercise 3 --")
print(inventory[:3])
print(inventory[-2:])
print(inventory[::2])

# Exercise 4

print("--- Exercise 4: List methods ---")

inventory.append("envelope")
print(inventory)

inventory.remove("tape")
print(inventory)

inventory.sort()
print(inventory)

# Exercise 5 
print("-- Exercise 5: Tuple comparison--")
coords= (40.7128, -74.0060)

try:
    coords[0] = 99
except TypeError as error:
    print(f"TypeError caught: {error}")
    print("Tuples protect coordinates from being changed by accident")

print(coords)

print("-- Excericse 6: List average Sales -- ")

sales = [100, 250, 75, 480, 200]
total = sum(sales)
count = len(sales)
average = total / count
print(f"Total sales: {total}")
print(f"Number of sales: {count}")
print(f"Average sales:{average}")
print(f"Best sale: {max(sales)}")
print(f"Worst sale: {min(sales)}")

print("-- Exercise 7: Accumalator pattern --")

prices = [9.99, 14.99, 4.99, 24.99, 1.99]

discounted = []
for price in prices:
    discounted.append(round(price * 0.9, 2))

print(prices)
print(discounted)

print("--Excerice 8: Filter--")

sales = [340,127,589,204,467,88,731,315,62,490]

high_sales=[]

for amount in sales:
    if amount > 300:
        high_sales.append(amount)

print(high_sales)
print(f"Count: {len(high_sales)}")
print("Average:", sum(high_sales) / len(high_sales))
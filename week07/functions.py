# Self assesment questions

#1- The first error i spotted was the missing comma in for sale in sales. It became pretty obvious after looking at the code and sort of explaining to the duck and this showed me the obvious missing syntax. This showed me that i am always looking at syntax when debugging first.

#2 - apply_discount(price,rate) applys a discount based off what tier and price the customer is in if they arenet hitting those certain inputs it will return the original price. A colleuge could use this if they knew what inputs and outputs to expect.

#3 - I did use AI on some parts of todays lab to help me better understand the code and logic i was writing. Although i need to get better in the future with being able to independently understand what im writing.

def calculate_tax(price,rate):
    return price * rate

# Calling the function

tax1 = calculate_tax(100, 0.07)
tax2= calculate_tax (250, 0.08)

print(f"Tax for $100 at 7%: ${tax1:.2f}")
print(f"Tax for $250 at 8%: ${tax2:.2f}")
print(f"Tax for $350 at 5%: ${calculate_tax(350,0.05):.2f}")

# Exercise 2 

def apply_discount (price, tier):
    if tier == "gold":
        return price * 0.85
    elif tier == "silver":
        return price * 0.90
    elif tier == "bronze":
        return price * 0.95
    else: 
        return price

# Calling the function with different tiers
original_price = 200

for tier in ["gold", "silver", "bronze", "none"]:
    print(f"{tier}: ${apply_discount(original_price,tier):.2f}")

# Exercise 3

def final_price(price, tax_rate, discount_tier):
    discounted_price = apply_discount(price, discount_tier)
    tax= calculate_tax(discounted_price, tax_rate)
    return discounted_price + tax

# Calling the final_price function
print(f"final_price(200, 0.07, 'gold') = ${final_price(200, 0.07, 'gold'):.2f}")

# Exercise 4 

orders = [(200, 'gold'), (150, 'silver'), (80, 'bronze'), (500, 'home')]

rate = 0.07
for price, tier in orders:
    total = final_price(price, rate, tier)
    print(f"Price: ${price}| Tier: {tier} | Total: ${total:.2f}")

# Exercise 5 

sales = [120, 80, 250, 175, 90]

# Bug 1: Add each sale instead of replacing the total
total = 0
for sale in sales:
    total += sale

print(f"Total: ${total}")

# Bug 2: Add the missing colon after the for loop
count = 0
for sale in sales:
    count += 1

print(f"Count: {count}")

# Bug 3: Use < instead of <= to avoid an invalid index
i = 0
while i < len(sales):
    print(sales[i])
    i += 1

# Exercise 6

x= 100

def double_it():
    x= 999 # local x 
    return x * 2 

print(x)
print(double_it())
print(x)



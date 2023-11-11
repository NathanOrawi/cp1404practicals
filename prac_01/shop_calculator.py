total_item_price = 0
items = int(input("Number of items: "))
while items < 0:
    print("Invalid number of items!")
    items = int(input("Number of items: "))
for i in range(items):
    items_price = float(input("Price of item: "))
    total_item_price += items_price
print(f"Total price for {items} item(s) is ${total_item_price:.2f}")
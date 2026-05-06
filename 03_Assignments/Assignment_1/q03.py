products = [
    {"id": 101, "name": "Laptop", "price": 55000, "stock": 12},
    {"id": 102, "name": "Phone", "price": 30000, "stock": 7},
    {"id": 103, "name": "Tablet", "price": 22000, "stock": 0},
    {"id": 104, "name": "Smartwatch", "price": 12000, "stock": 25},
    {"id": 105, "name": "Camera", "price": 45000, "stock": 3},
]

in_stock = []
out_of_stock = []

for p in products:
    if p["stock"] > 0:
        in_stock.append(p)
    else:
        out_of_stock.append(p)

for p in products:
    if p["price"] > 30000:
        discount = p["price"] * 0.10
        p["final_price"] = p["price"] - discount
    else:
        p["final_price"] = p["price"]

product_names = []
for p in products:
    product_names.append(p["name"])
product_names.sort()

id_to_details = {}
for p in products:
    id_to_details[p["id"]] = (p["name"], p["final_price"])

max_price = 0
costliest_item = ""
for p in products:
    if p["final_price"] > max_price:
        max_price = p["final_price"]
        costliest_item = p["name"]

max_stock = 0
max_stock_item = ""
for p in products:
    if p["stock"] > max_stock:
        max_stock = p["stock"]
        max_stock_item = p["name"]

cheap_items = [p for p in products if p["final_price"] < 30000]

print("In Stock:", in_stock)
print("Out of Stock:", out_of_stock)
print("Sorted Names:", product_names)
print("ID Mapping:", id_to_details)
print("Costliest Item:", costliest_item)
print("Max Stock Item:", max_stock_item)
print("Items below 30000:", cheap_items)
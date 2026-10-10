orders = ["ყავა", "ჩაი", "ყავა", "წვენი", "ჩაი", "ყავა", "წყალი"]
unique_orders = []
for drinks in orders:
    if drinks not in unique_orders:
        unique_orders.append(drinks)
print (f"უნიკალური: {unique_orders}")

sixshire = [(i, orders.count(i)) for i in unique_orders]
print(f"სიხშირე: {sixshire}")

popular_drink, max_count = sixshire[0]
for drink, count in sixshire:
    if count > max_count:
        popular_drink, max_count = drink, count
print(f"ყველაზე პოპულარული: {popular_drink} ({max_count}-ჯერ)")

print(f"ბოლო სამი შეკვეთა: {orders[ :-4:-1]}")
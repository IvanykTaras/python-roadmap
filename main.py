orders = [
    {"id": 1, "total": 120, "paid": True},
    {"id": 2, "total": 80, "paid": True},
    {"id": 3, "total": 200, "paid": False},
    {"id": 4, "total": 150, "paid": True},
]

orders_filtered = [o["id"] for o in orders if o["paid"] and o["total"] > 100]
print(orders_filtered)  # Output: [1, 4]


items = ["apple", "banana", "cherry", "date"]

unque_items = set()

for item in items:
    if item in unque_items:
        print("Duplicate: ", item)
        break
    unque_items.add(item)
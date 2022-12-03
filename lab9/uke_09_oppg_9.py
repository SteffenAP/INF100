def displayInventory(inv):
    print("Inventory:")
    total_inv = 0
    for key, total in inv.items():
        print(f"{total} {key}")
        total_inv += total
    return total_inv

stuff = {"rope": 1, "torch": 6, "gold coin": 42, "dagger": 1, "arrow": 12}
print(displayInventory(stuff))
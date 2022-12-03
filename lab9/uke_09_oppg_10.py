def displayInventory(inv):
    print("Inventory:")
    total_inv = 0
    for key, total in inv.items():
        print(f"{total} {key}")
        total_inv += total
    return total_inv

def addToInventory(inventory, addedItems):
    for item in range(len(addedItems)):
        if addedItems[item] in inventory:
            for key in inventory:
                if addedItems[item] == key:
                    inventory[key] += 1
        else:
            inventory.update({addedItems[item] : 1})
    return inventory

inv = {"gold coin": 42, "rope": 1}
dragonLoot = ["gold coin", "dagger", "gold coin", "gold coin", "ruby"]
inv = addToInventory(inv, dragonLoot)
print(displayInventory(inv))
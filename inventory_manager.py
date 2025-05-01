import data


class FruitInventoryManager:
    def add_item(self, item, quantity):
        if quantity <= 0:
            return False
        else:
            if item in data.inventory:
                data.inventory[item] += quantity
            else:
                data.inventory[item] = quantity
            return True

    def remove_item(self, item, quantity):
        if quantity <= 0:
            return False
        elif item in data.inventory:
            if data.inventory[item] >= quantity:
                data.inventory[item] -= quantity
                return True
            elif data.inventory[item] == quantity:
                del data.inventory[item]
                return True
        return False

    def view_inventory(self):
        return data.inventory

    def get_stock(self, item):
        return data.inventory.get(item, 0)


def main():
    manager = FruitInventoryManager()

    while True:
        print("\nInventory Manager")
        print("1. Add Item")
        print("2. Remove Item")
        print("3. View Inventory")

        try:
            choice = input("Choose an option: ")

            if choice == "1":
                item = input("Enter item name: ").lower()
                if item == "":
                    print("\nPlease enter the Fruit name.")
                else:
                    quantity = int(input("Enter quantity: "))
                    if manager.add_item(item, quantity):
                        print(f"\nAdded {quantity} of {item}.")
                    else:
                        print("\nInvalid quantity. Item not added.")

            elif choice == "2":
                item = input("Enter item name to remove: ").lower()
                if item == "":
                    print("\nPlease enter the Fruit name.")
                else:
                    quantity = int(input("Enter quantity to remove: "))
                    result = manager.remove_item(item, quantity)
                    if result:
                        print(f"\nSuccessfully removed {quantity} of {item}.")
                    else:
                        if quantity <= 0:
                            print("\nInvalid removal quantity.")
                        elif item not in data.inventory:
                            print(f"\n{item} not found.")
                        else:
                            available = data.inventory.get(item, 0)
                            print(f"Can't remove {item} of {quantity}. \
                                Only {available} available.")

            elif choice == "3":
                inventory = manager.view_inventory()
                if not inventory:
                    print("\nNo item found.")
                else:
                    print("\nInventory List:")
                    for item, qty in inventory.items():
                        if qty > 0:
                            print(f"{qty} of {item}(s)")

        except ValueError as ve:
            print(f"\nInput error: {ve}")
        except Exception as e:
            print(f"\nAn unexpected error occurred: {e}")


if __name__ == "__main__":
    main()

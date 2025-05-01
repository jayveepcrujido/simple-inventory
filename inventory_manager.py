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

import unittest
import data
from inventory_manager import FruitInventoryManager


class TestInventoryManager(unittest.TestCase):

    def setUp(self):
        data.inventory.clear()
        self.manager = FruitInventoryManager()

    def test_view_empty_inventory(self):
        inventory = self.manager.view_inventory()
        self.assertEqual(inventory, {})

    def test_add_item(self):
        self.manager.add_item("apples", 10)
        self.assertEqual(self.manager.get_stock("apples"), 10)

    def test_add_item_negative_quantity(self):
        result = self.manager.add_item("orange", -3)
        self.assertFalse(result)
        self.assertNotIn("orange", data.inventory)


if __name__ == "__main__":
    unittest.main()

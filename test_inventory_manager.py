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

    def test_add_item_zero_quantity(self):
        result = self.manager.add_item("avocado", 0)
        self.assertFalse(result)
        self.assertNotIn("avocado", data.inventory)

    def test_remove_item(self):
        self.manager.add_item("bananas", 5)
        result = self.manager.remove_item("bananas", 5)
        self.assertTrue(result)
        self.assertEqual(self.manager.get_stock("bananas"), 0)


if __name__ == "__main__":
    unittest.main()

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

    def test_remove_item_zero_quantity(self):
        self.manager.add_item("mango", 5)
        result = self.manager.remove_item("mango", 0)
        self.assertFalse(result)
        self.assertEqual(data.inventory["mango"], 5)

    def test_remove_item_negative_quantity(self):
        self.manager.add_item("cherry", 5)
        result = self.manager.remove_item("cherry", -2)
        self.assertFalse(result)
        self.assertEqual(data.inventory["cherry"], 5)

    def test_remove_more_than_available(self):
        self.manager.add_item("grapes", 3)
        result = self.manager.remove_item("grapes", 5)
        self.assertFalse(result)
        self.assertEqual(self.manager.get_stock("grapes"), 3)

    def test_view_inventory(self):
        self.manager.add_item("oranges", 7)
        inventory = self.manager.view_inventory()
        self.assertIn("oranges", inventory)
        self.assertEqual(inventory["oranges"], 7)


if __name__ == "__main__":
    unittest.main()

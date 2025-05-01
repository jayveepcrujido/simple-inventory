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


if __name__ == "__main__":
    unittest.main()

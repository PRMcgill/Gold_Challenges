
import pytest
import unittest
import repo


class ChallengeOneTests(unittest.TestCase):

    def test_repo_add_item_should_add_a_meal(self):
        self.meal_number = '1'
        self.name = 'Grilled Cheese'
        self.description = 'Two grilled pieces of bread with melted cheese inbetween'
        self.ingredients = 'Bread, Cheese'
        self.price = '$1'
        repo.add_item(self.meal_number, self.name,
                      self.description, self.ingredients, self.price)
        actual = len(repo.menu)
        expected = 1
        self.assertEqual(actual, expected)

    def test_repo_show_menu_menu_should_equal(self):
        actual = len(repo.show_menu())
        expected = 1
        self.assertEqual(actual, expected)

    def test_repo_delete_item_should_delete_item(self):
        self.meal_number = '1'
        self.name = 'Grilled Cheese'
        self.description = 'Two grilled pieces of bread with melted cheese inbetween'
        self.ingredients = 'Bread, Cheese'
        self.price = '$1'
        repo.add_item(self.meal_number, self.name,
                      self.description, self.ingredients, self.price)
        self.assertTrue(repo.delete_item(self.name))

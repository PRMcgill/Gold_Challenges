import unittest
import pytest
import repo

class ChallengeThreeTests(unittest.TestCase):
    
    
    def test_repo_add_outing_should_add_outing(self):
        self.event_type = 'Golf'
        self.people_attending = '5'
        self.date = '03/23/2019'
        self.cost_per_person = '50'
        z = repo.Menu_functions()
        z.add_outing(self.event_type, self.people_attending, self.date, self.cost_per_person)
        actual = len(repo.outings)
        expected = 1
        self.assertEqual(actual,expected)
    
    def test_repo_show_outings_outings_should_equal(self): 
        y = repo.Menu_functions()
        actual = len(y.show_outings())
        expected = 1
        self.assertEqual(actual, expected)

    

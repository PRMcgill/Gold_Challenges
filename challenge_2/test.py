import unittest
import pytest
import repo


tr = repo.RepoFunctions()


class ChallengeTwoTests(unittest.TestCase):

    def test_repo_add_claim_should_add_a_claim(self):
        self.claim_id = '1'
        self.claim_type = "Auto"
        self.description = "Car exploded while sitting in the driveway."
        self.claim_amount = "$5000"
        self.date_of_incident = "02/12/2019"
        self.date_of_claim = "02/14/2019"
        self.is_valid = "True"

        tr.add_claim(self.claim_id, self.claim_type, self.description,
                     self.claim_amount, self.date_of_incident,
                     self.date_of_claim, self.is_valid)
        actual = len(repo.claims)
        expected = 1
        self.assertEqual(actual, expected)

    def test_repo_see_claims_see_claims_should_equal(self):
        actual = len(tr.see_claims())
        expected = 1
        self.assertEqual(actual, expected)

    def test_repo_take_next_claim_should_remove_first_claim(self):
        self.claim_id = '1'
        self.claim_type = 'Auto'
        self.description = 'Ran over a person in traffic.'
        self.claim_amount = '$2000'
        self.date_of_incident = '01/01/2019'
        self.date_of_claim = '01/02/2019'
        self.is_valid = 'False'
        tr.add_claim(self.claim_id, self.claim_type, self.description,
                     self.claim_amount, self.date_of_incident,
                     self.date_of_claim, self.is_valid)
        tr.take_next_claim()
        actual = len(repo.claims)
        expected = 1
        self.assertEqual(actual, expected)

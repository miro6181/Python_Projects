#! /usr/bin/python3

import unittest

from christmas_exchange import ChristmasExchange, Participant

class ParticipantTest(unittest.TestCase):
    def setUp(self):
        self.giver = Participant('giver', 'T')
        self.getter = Participant('getter1', '1T')
    
    def test_valid_assignee(self):
        self.assertTrue(self.giver.is_valid_assignee(self.getter))
        self.giver.assignee = self.getter
        self.giver.add_to_prior()
        self.assertFalse(self.giver.is_valid_assignee(self.getter))

        self.getter2 = Participant('getter2', '2T')
        self.giver.assignee = self.getter2
        self.giver.add_to_prior()
        self.assertFalse(self.giver.is_valid_assignee(self.getter))

        self.getter3 = Participant('getter3', '3T')
        self.giver.assignee = self.getter3
        self.giver.add_to_prior()
        self.assertFalse(self.giver.is_valid_assignee(self.getter))

        self.getter4 = Participant('getter4', '4T')
        self.giver.assignee = self.getter4
        self.giver.add_to_prior()
        self.assertTrue(self.giver.is_valid_assignee(self.getter))



class ChristmasExchangeTest(unittest.TestCase):
    def setUp(self):
        self.participants = {'Person1':'H1', 'Person2':'H1', 'Person3':'H2', 'Person4':'H2', 'Person5':'H3', 'Person6': 'H4'}
        self.exch = ChristmasExchange(participants=self.participants)

    def test_load(self):
        self.assertEqual(self.participants, {participant.name:participant.household for participant in self.exch.participants})

    def test_assignments(self):
        assignments = self.exch.generate_assignments()

        for assignment in assignments:
            self.assertNotEqual(assignments[assignment], assignment)
            self.assertNotEqual(assignments[assignment].name, assignment.name)
            self.assertNotEqual(assignments[assignment].household, assignment.household)
        
        for participant in self.exch.participants:
            self.assertTrue(participant in assignments.keys())
            self.assertTrue(participant in assignments.values())



if __name__ == '__main__':
    unittest.main()
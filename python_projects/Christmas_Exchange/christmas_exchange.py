#! /usr/bin/python3

import argparse
import random
import json
from datetime import datetime

class Participant():
    def __init__(self, name, household, prior_assignments = []):
        self.name = name
        self.household = household
        self.prior_assignments = prior_assignments
        self.assignee = None
    
    def is_valid_assignee(self, assignee):
        # Valid assignee if not in priors, or household
        return not assignee.name in self.prior_assignments and assignee.household != self.household
    
    def add_to_prior(self):
        # Insert at front of list, pop last element if we have 3 on it already.
        self.prior_assignments.insert(0, self.assignee.name)
        if len(self.prior_assignments) > 3:
            self.prior_assignments.pop()


class ChristmasExchange():
    def __init__(self, participants=None, in_file=None):
        self.config_file = in_file
        self.assignments = {}

        # Add participants to participants list
        if self.config_file:
            self.participants = self.load_json(self.config_file)
        elif participants:
            self.participants = self.load_participants(participants)
        else:
            raise "Please provide a valid list of participants."

    def generate_assignments(self):
        # Hang until we have a valid set of assignments
        while not self.verify():
            self.assignments = {}
            # Loop through all participants, create list of valid assignees, randomly pick on and assign it
            for participant in self.participants:
                valid_assignees = [assignee for assignee in self.participants if participant.is_valid_assignee(assignee)]
                participant.assignee = random.choice(valid_assignees)
                self.assignments[participant] = participant.assignee
        else:
            # Once we have a valid assignment list, add to priors and write to config file
            self.add_priors()
            if self.config_file:
                self.write_json(self.config_file)
            return self.assignments

    def verify(self):
        # Verify each participant is a giver, and receiver, and their assignee is valid
        valid = True
        for participant in self.participants:
            if (participant in self.assignments.keys() and participant in self.assignments.values()) and (participant.is_valid_assignee(participant.assignee)):
                continue
            else:
                return False
        return valid
    
    def add_priors(self):
        # Add each participant assignee to priors
        for participant in self.participants:
            participant.add_to_prior()

    def print_assignments(self):
        for assignment in self.assignments:
            print(f'{assignment.name} : {self.assignments[assignment].name}')

    def load_participants(self, participants):
        out_particpants = []
        for participant in participants:
            out_particpants.append(Participant(participant, participants[participant]))
        return out_particpants
    
    def load_json(self, in_file):
        out_particpants = []
        with open(in_file, 'r') as json_file:
            data = json.load(json_file)
            participants = data['participants']
            # Create participant object for each participant
            for participant in participants:
                out_particpants.append(Participant(participant['name'], participant['household'], participant['prior_assignments']))
            
            # If a timestamp exists, check it to see if the years are the same as now, if so exit
            if data.get('timestamp'):
                try:
                    ts = datetime.strptime(data['timestamp'], '%Y-%m-%d %H:%M:%S.%f')
                    if ts.year == datetime.now().year:
                        print("Already ran the generator this year. Adjust timestamp to override. Here are this year's assignments:\n")
                        print({participant.name:participant.prior_assignments[0] for participant in out_particpants if participant.prior_assignments})
                        exit()
                except ValueError:
                    print("Corrupted timestamp in config file.")
                    exit()
        return out_particpants

    def write_json(self, out_file):
        # Write participants to file
        out_dict = {'participants': []}
        with open(out_file, 'w') as out_file:
            out_dict['timestamp'] = str(datetime.now())
            for participant in self.participants:
                out_dict['participants'].append({'name': participant.name, 'household': participant.household, 'prior_assignments': participant.prior_assignments})
            json.dump(out_dict, out_file)


if __name__ == '__main__':
    argparser = argparse.ArgumentParser()
    argparser.add_argument('-p', '--participants', default={'Michael':'ME', 'Ellie':'ME', 'Darci':'DE', 'Erik':'DE', 'Phil':'PC', 'Chelsy':'PC', 'Reanne':'R'})
    argparser.add_argument('-f', '--file', default=None)
    args = argparser.parse_args()
    
    christmas_exchange = ChristmasExchange(args.participants, args.file)
    christmas_exchange.generate_assignments()
    christmas_exchange.print_assignments()


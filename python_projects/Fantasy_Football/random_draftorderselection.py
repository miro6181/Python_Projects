#! /usr/bin/python3

import random
import argparse

def generate_order(in_players):
    rand_nums = list(range(1, len(in_players) + 1))
    
    # Randomize: shuffle numbers and players list 1000 times
    for i in range(1000):
        random.shuffle(rand_nums)
        random.shuffle(in_players)

    order = dict(zip(in_players, rand_nums))
    # Sort by draft number and print
    res = {k: v for k, v in sorted(order.items(), key=lambda item: item[1])}
    for player in res:
        print(f'{res[player]}. {player}')

if __name__ == '__main__':
    argparser = argparse.ArgumentParser()
    argparser.add_argument('-p', '--players', default=["Michael", "Jessica", "Brent", "Darci", "Dave", "Angel", "Barb", "Todd", "Chelsy/Phil", "David", "Erik", "Nick"])
    args = argparser.parse_args()

    generate_order(args.players)


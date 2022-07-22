#! /usr/bin/python3

import random
import argparse

def generate_order(in_players):
    num_players = len(in_players)
    rand_nums = random.sample(range(1, num_players + 1), num_players)

    order = dict(zip(in_players, rand_nums))
    res = {k: v for k, v in sorted(order.items(), key=lambda item: item[1])}
    for player in res:
        print(f'{player}: {res[player]}')

if __name__ == '__main__':
    argparser = argparse.ArgumentParser()
    argparser.add_argument('-p', '--players', default=["Michael", "Jessica", "Brent", "Darci", "Dave", "Angel", "Barb", "Todd", "Chelsy/Phil", "David", "Erik", "Nick"])
    args = argparser.parse_args()

    generate_order(args.players)


# encoding: utf-8

import argparse


parser = argparse.ArgumentParser(description='AdventOfCode validator.')
parser.add_argument('-day', type=int, help='day to select')
parser.add_argument('--riddle', action='store_true')
parser.add_argument('--solution', action='store_true', default=False)
parser.add_argument('-part', type=int, default=1, help='part to submit')
parser.add_argument('-sol', type=str, default='0', help='submitted solution')


def print_riddle(day):
    with open('./day{:0>2}/riddle.md'.format(day)) as r:
        print r.read()


def test_solution(solution, day, part):
    with open('./day{:0>2}/solution.txt'.format(day)) as r:
        sol1, sol2 = r.readlines()
    if part == 1:
        return solution == sol1.strip()
    if part == 2:
        return solution == sol2.strip()


if __name__ == '__main__':
    args = parser.parse_args()
    if args.riddle and args.solution:
        raise Exception('You must choose between getting '
                        'a riddle and validating a solution!')
    if args.riddle:
        print_riddle(args.day)

    if args.solution:
        if test_solution(args.sol, args.day, args.part):
            print 'Correct solution! Your guess was {}.'.format(args.sol)
        else:
            print 'Your guess is wrong! Your guess was {}.'.format(args.sol)

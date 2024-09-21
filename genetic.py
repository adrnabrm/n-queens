"""
Adrian Abraham
Moon
CECS 451
9/20/24

This program will solve the n-queens problem, where given a board we must place n amount of queens on an n by n board in a way that they are not on the same row, column, or diagonal. This approach will use a genetic algorithm, meaning that we take an amount of different states of boards and perform selection, crossover, and mutation on each of them until we get the final board.
"""

import board
import time
import math
import random

def genetic(n, states):
    """
    Runs a genetic algorithm on states of the board
    :param n:
        Integer representing the amount of queens on the board for the n-queens problem
    :param states:
        A list of different Board objects to be modified using the genetic algorithm
    :return:
        A list of modified Board objects from the input states
    """

    # calculate probability of choosing the states using fitness value / sum fitness value
    num_pairs = math.comb(n, 2)
    sum_fitness = sum([num_pairs - s.get_fitness() for s in states])
    probs = [(num_pairs - s.get_fitness()) / sum_fitness for s in states]
    ranges = [sum(probs[:i]) for i in range(8)] + [1]

    # randomly choose 8 states using that probability
    new_states = []
    for i in range(8):
        rand = random.random()
        for j in range(1, len(ranges)):
            if rand < ranges[j]:
                new_states.append(states[j - 1])
                break

    # choosing split points to perform cross over
    split_points = [random.randint(0, n - 1) for i in range(4)]
    new_encodings = []

    for i in range(0, 8, 2):
        split_pt = split_points[i // 2]
        new_encodings.append(f'{new_states[i].encode()[:split_pt]}{new_states[i + 1].encode()[split_pt:]}')
        new_encodings.append(f'{new_states[i + 1].encode()[:split_pt]}{new_states[i].encode()[split_pt:]}')

    # randomly mutate one char of each new state
    for i, encoding in enumerate(new_encodings):
        encoding = list(encoding)
        encoding[random.randint(0, n - 1)] = str(random.randint(0, n - 1))
        new_encodings[i] = ''.join(encoding)

    # changing each old state to the new one using the newly made encodings
    for i in range(len(states)):
        states[i].decode(new_encodings[i])

    return states



def create_states(n):
    """
    Creates 8 states of n amount of queens to be used in the genetic algorithm
    :param n:
        Integer representing how many queens will be on each Board object
    :return:
        A list of Board objects as states
    """
    states = []
    for i in range(8):
        states.append(board.Board(n))
    return states

def main():
    """
    Represents the main starting point of the program
    """
    start_time = time.time()
    n = 5
    states = create_states(n)
    solving = True

    # running the genetic algorithm on the list of states, once solution is found we will print the running time and the final solution to the n-queens problem
    while solving:
        states = genetic(n, states)
        for s in states:
            if s.get_fitness() == 0:
                print(f'Running time: {round((time.time() - start_time) * 1000)}ms')
                s.print_map()
                solving = False
                break


if __name__ == '__main__':
    main()
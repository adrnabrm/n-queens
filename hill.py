"""
Adrian Abraham
Moon
CECS 451
9/20/24

This program will solve the n-queens problem, where given a board we must place n amount of queens on an n by n board in a way that they are not on the same row, column, or diagonal. This approach will use a hill-climing method, meaning we will move each queen on the board, take the board that has the highest fitness value, and repeat the process by moving queens until we reach a solution.
"""

import board
import time

def local_search_space(b, n):
    """
    Finds the optimal board using a hill-climb approach, meaning we will find the most optimal board by moving queens around and calculating how well each board performs in solving the problem
    :param b:
        A Board object to be modified
    :param n:
        An integer representing the amount of queens we have
    :return:
        The most optimal Board after moving each queen around.
    """
    optimal = b

    # for each queen, we will move it around on their respective rows and calculate its fitness score to determine if it is more optimal than the original
    for i in range(n):
        encoding = list(b.encode())
        for j in range(n):
            encoding[i] = str(j)
            new_encode = ''.join(encoding)
            temp = board.Board(n)
            temp.decode(new_encode)
            if temp.get_fitness() < optimal.get_fitness():
                optimal = temp

    return optimal

def main():
    """
    Represents the starting point of the program
    """

    start_time = time.time()
    n = 5
    b = board.Board(n)
    count = 0

    # performing a hill-climb approach in solving the n-queens problem
    while b.get_fitness() != 0:
        b = local_search_space(b, n)
        count += 1
        # if we reach a Board that cannot be solved due to a plateau after 100 tries, we will reset the board and try again
        if count > 100:
            b = board.Board(n)
            count = 0

    # printing the final result
    print(f'Running time: {round((time.time() - start_time) * 1000)}ms')
    b.print_map()

if __name__ == '__main__':
    main()
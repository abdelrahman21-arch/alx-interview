"""
N queens
"""

import sys


class SolveNqueen:
    """class to solve nqueen problem"""

    @staticmethod
    def nqueen(nqueens):
        """

        Args:
            nqueens: the number of queens

        Returns: list of solutions

        """
        col = set()
        pos_diag = set()  # r + c
        neg_diag = set()  # r - c
        queens = []  # empty list to store queens positon
        solutions = []

        def backtrack(r):
            if r == nqueens:
                solutions.append(queens[:])
                return True

            for c in range(nqueens):

                if c in col or (r + c) in pos_diag or (r - c) in neg_diag:
                    continue
                col.add(c)
                pos_diag.add(r + c)
                neg_diag.add(r - c)
                queens.append([r, c])  # store the postion of each queen

                backtrack(r + 1)

                # Remove the queen and backtrack
                col.remove(c)
                pos_diag.remove(r + c)
                neg_diag.remove(r - c)
                queens.pop()


        backtrack(0)

        return solutions


if __name__ == "__main__":
    if len(sys.argv) > 2:
        print("Usage: nqueens N\n")
        exit(1)
    try:
        n = int(sys.argv[1])

    except ValueError:
        print("N must be a number\n")
        exit(1)

    if n < 4:
        print("N must be at least 4\n")
        exit(1)

    instance = SolveNqueen()
    all_solutions = instance.nqueen(n)

    for solution in all_solutions:
        print(solution)

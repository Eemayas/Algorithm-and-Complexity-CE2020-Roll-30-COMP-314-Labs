import unittest


def is_safe(board, x, y, n):
    for i in range(n):
        if board[i][y] == 1:
            return False

    row = x
    col = y
    while row >= 0 and col >= 0:
        if board[row][col] == 1:
            return False
        row -= 1
        col -= 1

    row = x
    col = y
    while row >= 0 and col < n:
        if board[row][col] == 1:
            return False
        row -= 1
        col += 1

    return True


def check_n_queen(board, row, n):
    if row == n:
        return True

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            if (check_n_queen(board, row+1, n)):
                return True
            board[row][col] = 0
    return False


def n_queen(n):
    board = [[0 for _ in range(n)] for _ in range(n)]
    solution_found = check_n_queen(board, 0, n)
    return solution_found, board


class TestNQueen(unittest.TestCase):

    def test_n_queen(self):
        n = 8
        solution_found, board = n_queen(n)
        self.assertTrue(solution_found)

        # Verify that there is exactly one queen in each row and each column
        for i in range(n):
            self.assertEqual(sum(board[i]), 1)
            self.assertEqual(sum(board[j][i] for j in range(n)), 1)

        # Verify that no two queens attack each other
        self.assertTrue(self.verify_no_attack(board, n))

    def verify_no_attack(self, board, n):
        for i in range(n):
            for j in range(n):
                if board[i][j] == 1:
                    # Check vertical
                    for k in range(n):
                        if k != i and board[k][j] == 1:
                            return False
                    # Check diagonal (top-left to bottom-right)
                    row, col = i, j
                    while row >= 0 and col >= 0:
                        if row != i and col != j and board[row][col] == 1:
                            return False
                        row -= 1
                        col -= 1
                    row, col = i, j
                    while row < n and col < n:
                        if row != i and col != j and board[row][col] == 1:
                            return False
                        row += 1
                        col += 1
                    # Check diagonal (top-right to bottom-left)
                    row, col = i, j
                    while row >= 0 and col < n:
                        if row != i and col != j and board[row][col] == 1:
                            return False
                        row -= 1
                        col += 1
                    row, col = i, j
                    while row < n and col >= 0:
                        if row != i and col != j and board[row][col] == 1:
                            return False
                        row += 1
                        col -= 1
        return True


if __name__ == "__main__":
    unittest.main()

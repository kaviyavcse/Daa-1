def is_safe(board, row, col):
    for prev_row in range(row):
        placed = board[prev_row]

        # Same column
        if placed == col:
            return False

        # Same diagonal
        if abs(prev_row - row) == abs(placed - col):
            return False

    return True


def solve_n_queens(n):
    board = [-1] * n
    solutions = []
    backtrack_count = [0]

    def backtrack(row):
        if row == n:
            solutions.append(board[:])
            return

        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col
                backtrack(row + 1)
                board[row] = -1   # Undo
                backtrack_count[0] += 1

    backtrack(0)
    return solutions, backtrack_count[0]


def display_board(solution, n):
    print(" +" + "---+" * n)

    for row in range(n):
        print(" |", end="")
        for col in range(n):
            if solution[row] == col:
                print(" Q |", end="")
            else:
                print(" . |", end="")
        print()
        print(" +" + "---+" * n)


# Solve for N = 5 and N = 7
for n in [5, 7]:
    solutions, backtracks = solve_n_queens(n)

    print(f"\nN = {n}: {len(solutions)} solutions, {backtracks} backtracks")

    # Display all solutions only for N = 5
    if n == 5:
        print(f"\nAll solutions for {n}-Queens:")
        for i, sol in enumerate(solutions, 1):
            print(f"\nSolution {i}: {sol}")
            display_board(sol, n)

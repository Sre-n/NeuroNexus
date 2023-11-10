# Tic-Tac-Toe Board Representation
class TicTacToe:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]

    def display_board(self):
        for row in self.board:
            print('|'.join(row))
            print('-' * 5)

    def is_empty(self, row, col):
        return self.board[row][col] == ' '

    def make_move(self, row, col, player):
        if self.is_empty(row, col):
            self.board[row][col] = player
            return True
        else:
            return False

    def is_winner(self, player):
        # Check rows and columns
        for i in range(3):
            if all(self.board[i][j] == player for j in range(3)) or all(self.board[j][i] == player for j in range(3)):
                return True

        # Check diagonals
        if all(self.board[i][i] == player for i in range(3)) or all(self.board[i][2 - i] == player for i in range(3)):
            return True

        return False

    def is_full(self):
        return all(cell != ' ' for row in self.board for cell in row)

# Minimax Algorithm with Alpha-Beta Pruning
def minimax(board, depth, alpha, beta, maximizing_player):
    result = evaluate_board(board)

    if result is not None:
        return result

    if maximizing_player:
        max_eval = float('-inf')
        for i in range(3):
            for j in range(3):
                if board.is_empty(i, j):
                    board.make_move(i, j, 'X')
                    eval = minimax(board, depth + 1, alpha, beta, False)
                    board.make_move(i, j, ' ')  # Undo the move
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break  # Beta cutoff
        return max_eval
    else:
        min_eval = float('inf')
        for i in range(3):
            for j in range(3):
                if board.is_empty(i, j):
                    board.make_move(i, j, 'O')
                    eval = minimax(board, depth + 1, alpha, beta, True)
                    board.make_move(i, j, ' ')  # Undo the move
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break  # Alpha cutoff
        return min_eval

def evaluate_board(board):
    if board.is_winner('X'):
        return 1
    elif board.is_winner('O'):
        return -1
    elif board.is_full():
        return 0
    else:
        return None

def find_best_move(board):
    best_val = float('-inf')
    best_move = None

    for i in range(3):
        for j in range(3):
            if board.is_empty(i, j):
                board.make_move(i, j, 'X')
                move_val = minimax(board, 0, float('-inf'), float('inf'), False)
                board.make_move(i, j, ' ')  # Undo the move

                if move_val > best_val:
                    best_val = move_val
                    best_move = (i, j)

    return best_move

if __name__ == "__main__":
    # Example Usage
    game_board = TicTacToe()

    while not game_board.is_full():
        # Player 'X' (Maximizer) makes a move
        row, col = map(int, input("Enter 'X' move (row and column separated by space): ").split())
        if game_board.make_move(row, col, 'X'):
            game_board.display_board()
            if game_board.is_winner('X'):
                print("Player 'X' wins!")
                break
            elif game_board.is_full():
                print("It's a tie!")
                break

        # Player 'O' (Minimizer) makes a move
        print("Player 'O' (AI) is making a move...")
        best_move = find_best_move(game_board)
        game_board.make_move(*best_move, 'O')
        game_board.display_board()

        if game_board.is_winner('O'):
            print("Player 'O' (AI) wins!")
            break

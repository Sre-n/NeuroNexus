import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")

        self.board = [""] * 9
        self.current_player = "X"

        self.buttons = []
        for i in range(3):
            for j in range(3):
                button = tk.Button(root, text="", font=("Arial", 24), width=5, height=2,
                                   command=lambda row=i, col=j: self.on_click(row, col))
                button.grid(row=i, column=j)
                self.buttons.append(button)

        self.reset_button = tk.Button(root, text="Reset", command=self.reset_game)
        self.reset_button.grid(row=3, columnspan=3)

        self.computer_symbol = "O"
        self.user_symbol = "X"

        if self.current_player == self.computer_symbol:
            self.play_computer()

    def on_click(self, row, col):
        index = row * 3 + col
        if self.board[index] == "" and not self.check_winner():
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player)
            if self.check_winner():
                messagebox.showinfo("Game Over", "Its a tie")
                self.reset_game()
            elif "" not in self.board:
                messagebox.showinfo("Game Over", "It's a tie!")
                self.reset_game()
            else:
                self.current_player = self.user_symbol if self.current_player == self.computer_symbol else self.computer_symbol
                if self.current_player == self.computer_symbol:
                    self.play_computer()

    def play_computer(self):
        best_score = float("-inf")
        best_move = -1

        for i in range(9):
            if self.board[i] == "":
                self.board[i] = self.computer_symbol
                score = self.minimax(self.board, 0, False)
                self.board[i] = ""

                if score > best_score:
                    best_score = score
                    best_move = i

        if best_move != -1:
            self.board[best_move] = self.computer_symbol
            self.buttons[best_move].config(text=self.computer_symbol)
            if self.check_winner():
                messagebox.showinfo("Game Over", "Computer wins!")
                self.reset_game()
            elif "" not in self.board:
                messagebox.showinfo("Game Over", "It's a tie!")
                self.reset_game()
            else:
                self.current_player = self.user_symbol

    def minimax(self, board, depth, is_maximizing):
        scores = {"X": -1, "O": 1, "Tie": 0}

        result = self.check_winner(board)
        if result:
            return scores[result]

        if is_maximizing:
            best_score = float("-inf")
            for i in range(9):
                if board[i] == "":
                    board[i] = self.computer_symbol
                    score = self.minimax(board, depth + 1, False)
                    board[i] = ""
                    best_score = max(score, best_score)
            return best_score
        else:
            best_score = float("inf")
            for i in range(9):
                if board[i] == "":
                    board[i] = self.user_symbol
                    score = self.minimax(board, depth + 1, True)
                    board[i] = ""
                    best_score = min(score, best_score)
            return best_score

    def check_winner(self, board=None):
        if board is None:
            board = self.board

        for i in range(0, 9, 3):  # Check rows
            if board[i] == board[i + 1] == board[i + 2] != "":
                return board[i]

        for i in range(3):  # Check columns
            if board[i] == board[i + 3] == board[i + 6] != "":
                return board[i]

        if board[0] == board[4] == board[8] != "" or board[2] == board[4] == board[6] != "":
            return board[4]

        if "" not in board:
            return "Tie"

        return ""




    def reset_game(self):
        for i in range(9):
            self.board[i] = ""
            self.buttons[i].config(text="")
        self.current_player = "X"
        if self.current_player == self.computer_symbol:
            self.play_computer()

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()


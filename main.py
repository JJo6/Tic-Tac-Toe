import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        
        self.player1_name = tk.StringVar()
        self.player2_name = tk.StringVar()

        self.setup_players()
        self.current_player = "X"
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.buttons = []

        for i in range(3):
            row_buttons = []
            for j in range(3):
                button = tk.Button(root, text=" ", font=("Helvetica", 20), width=8, height=4,
                                   command=lambda row=i, col=j: self.make_move(row, col), bg="black", fg="white")
                button.grid(row=i+1, column=j, padx=5, pady=5)
                row_buttons.append(button)
            self.buttons.append(row_buttons)

    def setup_players(self):
        player1_label = tk.Label(self.root, text="Player 1 (X):", fg="white", bg="black")
        player1_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")
        player1_entry = tk.Entry(self.root, textvariable=self.player1_name)
        player1_entry.grid(row=0, column=1, padx=5, pady=5)

        player2_label = tk.Label(self.root, text="Player 2 (O):", fg="white", bg="black")
        player2_label.grid(row=0, column=2, padx=5, pady=5, sticky="e")
        player2_entry = tk.Entry(self.root, textvariable=self.player2_name)
        player2_entry.grid(row=0, column=3, padx=5, pady=5)

    def make_move(self, row, col):
        if self.board[row][col] == " ":
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)
            if self.check_win(self.current_player):
                winner = self.player1_name.get() if self.current_player == "X" else self.player2_name.get()
                messagebox.showinfo("Tic Tac Toe", f"{winner} wins!")
                self.reset_board()
            elif all(cell != " " for row in self.board for cell in row):
                messagebox.showinfo("Tic Tac Toe", "It's a draw!")
                self.reset_board()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def check_win(self, mark):
        # Check rows, columns, and diagonals for a win
        return any(all(cell == mark for cell in row) for row in self.board) or \
               any(all(row[i] == mark for row in self.board) for i in range(3)) or \
               all(self.board[i][i] == mark for i in range(3)) or \
               all(self.board[i][2 - i] == mark for i in range(3))

    def reset_board(self):
        self.current_player = "X"
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text=" ")

if __name__ == "__main__":
    root = tk.Tk()
    root.configure(bg="black")
    game = TicTacToe(root)
    root.mainloop()

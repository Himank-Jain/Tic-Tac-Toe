import tkinter as tk
from tkinter import messagebox
import random

class TicTacToe:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Tic Tac Toe")
        self.root.geometry("300x300")
        self.initialize_gui()
        self.mode = 0
        self.board = [[' ' for i in range(3)] for i in range(3)]
        self.current_player = 'X'

    def initialize_gui(self):
        self.buttons = [[None for i in range(3)] for i in range(3)]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(self.root, width=5, height=5,
                                               command=lambda row=i, col=j: self.make_move(row, col))
                self.buttons[i][j].grid(row=i, column=j, sticky='nsew')

        for i in range(3):
            self.root.grid_rowconfigure(i, weight=1)
            self.root.grid_columnconfigure(i, weight=1)

        twoplayer_button = tk.Button(self.root, height=5, width=15, text="Two Player", command=lambda: self.set_mode(0))
        twoplayer_button.grid(row=1, column=4)

        computer_button = tk.Button(self.root, height=5, width=15, text="Against Computer", command=lambda: self.set_mode(1))
        computer_button.grid(row=2, column=4)

        reset_button = tk.Button(self.root, height=5, width=15, text="Reset",
                                    command=lambda: self.set_mode(0))
        reset_button.grid(row=0, column=4)


    def make_move(self, row, col):
        if self.board[row][col] == ' ':
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text='X' if self.current_player == 'X' else "O",
                                           state=tk.DISABLED)

            if self.check_winner():
                messagebox.showinfo("Tic Tac Toe", f"{self.current_player} wins!")
                self.reset_game()
            elif self.is_board_full():
                messagebox.showinfo("Tic Tac Toe", "It's a tie!")
                self.reset_game()
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'
                if self.mode == 1 and self.current_player == 'O':
                    self.computer_move()

    def computer_move(self):
        empty_cells = [(i, j) for i in range(3) for j in range(3) if self.board[i][j] == ' ']
        if empty_cells:
            row, col = random.choice(empty_cells)
            self.make_move(row, col)

    def set_mode(self, mode):
        self.mode = mode
        self.reset_game()


    def check_winner(self):
        # Check rows, columns, and diagonals
        for i in range(3):
            if all(cell == self.current_player for cell in self.board[i]) or all(
                    self.board[j][i] == self.current_player for j in range(3)):
                return True
        if all(self.board[i][i] == self.current_player for i in range(3)) or all(
                self.board[i][2 - i] == self.current_player for i in range(3)):
            return True
        return False
    def is_board_full(self):
        return all(all(cell != ' ' for cell in row) for row in self.board)

    def reset_game(self):
        for i in range(3):
            for j in range(3):
                self.board[i][j] = ' '
                self.buttons[i][j].config(text='', state=tk.NORMAL)

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    game = TicTacToe()
    game.run()

class TicTacToeGame:
    def __init__(self):
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.current_player = "X"
        self.winner = None

    def play(self, row, col):
        if self.board[row][col] != " " or self.winner:
            return False  

        self.board[row][col] = self.current_player
        if self.check_winner():
            self.winner = self.current_player
            return True

        self.current_player = "O" if self.current_player == "X" else "X"
        return True

    def check_winner(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != " ":
                return True
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != " ":
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != " ":
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != " ":
            return True
        return False

    def is_draw(self):
        return all(cell != " " for row in self.board for cell in row) and self.winner is None

class TicTacToe:
    def play(self, moves):
        size = 3
        rows = [0] * size
        cols = [0] * size
        diagonal = 0
        antidiagonal = 0
        player = 1

        for row, column in moves:
            rows[row] += player
            cols[column] += player

            if row == column:
                diagonal += player

            if row + column == size -1:
                antidiagonal += player


            if any(abs(complete) == size for complete in [rows[row], cols[column], diagonal, antidiagonal]):
                return "Player 1" if player == 1 else "Player 2"

            player *= -1

        return "Draw" if len(moves) == size * size else "Pending"

moves = [[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]]
game = TicTacToe()
print(game.play(moves)) # Player 2


# 00 01 02 r1
# 10 11 12 r2
# 20 21 22 r3
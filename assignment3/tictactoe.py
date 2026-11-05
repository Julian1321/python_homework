class TictactoeException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)


class Board:
    valid_moves = [
        "upper left", "upper center", "upper right",
        "middle left", "center", "middle right",
        "lower left", "lower center", "lower right"
    ]

    def __init__(self):
        self.board_array = [
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]
        ]
        self.turn = "X"
    
    def __str__(self):
        lines = []
        for row in self.board_array:
            lines.append(f" {row[0]} | {row[1]} | {row[2]} ")
        return "\n-----------\n".join(lines)

    def move(self, move_string):
        if move_string not in Board.valid_moves:
            raise TictactoeException("That's not a valid move.")

        move_index = Board.valid_moves.index(move_string)
        row = move_index // 3
        column = move_index % 3

        if self.board_array[row][column] != " ":
            raise TictactoeException("That spot is taken.")

        self.board_array[row][column] = self.turn

        if self.turn == "X":
           self.turn = "O"
        else:
            self.turn = "X"
    
    def whats_next(self):
        lines = []

        for i in range(3):
            lines.append(self.board_array[i])
            lines.append([
                self.board_array[0][i],
                self.board_array[1][i],
                self.board_array[2][i],
            ])
    
        lines.append([
            self.board_array[0][0],
            self.board_array[1][1],
            self.board_array[2][2],
        ])

        lines.append([
            self.board_array[0][2],
            self.board_array[1][1],
            self.board_array[2][0],
        ])

        for line in lines:
            if line == ["X", "X", "X"]:
                return (True, "X wins!")
            if line == ["O", "O", "O"]:
                return (True, "O wins!")

        if all (
            cell != " "
            for row in self.board_array
            for cell in row
        ):
            return (True, "Cat's Game.")

        return (False, f"{self.turn}'s turn.")

if __name__ == "__main__":
    board = Board()

    print("Welcome to Tic-Tac-Toe!")

    while True:
        print("\n" + str(board))

        game_over, message = board.whats_next()
        print(message)

        if game_over:
            break
        
        move = input(f"Player {board.turn}, enter your move: ").lower().strip()

        try:
            board.move(move)
        except TictactoeException as e:
            print(str(e))
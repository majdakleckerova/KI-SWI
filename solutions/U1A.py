def check_winner(board: list[list[str]]) -> str | None:
    # Zkontroluj řádky
    for row in board:
        if row[0] != "" and row[0] == row[1] == row[2]:
            return row[0]
    
    # Zkontroluj sloupce
    for col in range(3):
        if board[0][col] != "" and board[0][col] == board[1][col] == board[2][col]:
            return board[0][col]
    
    # Zkontroluj diagonály
    if board[0][0] != "" and board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]
    if board[0][2] != "" and board[0][2] == board[1][1] == board[2][0]:
        return board[0][2]
    
    # Nikdo nevyhrál
    return None
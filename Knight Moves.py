def knight(position):
    position = position.upper()
    column, row = ord(position[0]) - ord('A') + 1, int(position[1])
    
    moves = [
        (column - 2, row - 1), (column - 2, row + 1),
        (column - 1, row - 2), (column - 1, row + 2),
        (column + 1, row - 2), (column + 1, row + 2),
        (column + 2, row - 1), (column + 2, row + 1)
    ]

    valid_moves = [(chr(c + ord('A') - 1), r) for c, r in moves if 1 <= c <= 8 and 1 <= r <= 8]

    return sorted(valid_moves)

#input
current_position = input().strip()

#output
for move in knight(current_position):
    print(move[0] + str(move[1]))

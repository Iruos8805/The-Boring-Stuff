def chessValue(chessset):
    position = list(chessset.keys())
    piece = list(chessset.values())
    chess = {
        'bpawn': '8', 'wpawn': '8',
        'brook': '2', 'wrook': '2',
        'bknight': '2', 'wknight': '2',
        'bbishop': '2', 'wbishop': '2',
        'bking': '1', 'wking': '1',
        'bqueen': '1', 'wqueen': '1'  
    }

    for i in position:
        if int(i[0]) >= 9 or int(i[0]) <= 0 or i[1] > 'h':
            return False

    for i in piece:
        if i[0] not in ['b', 'w']:
            return False
        if i[1:] not in ['knight', 'bishop', 'rook', 'king', 'queen', 'pawn']:
            return False

    if sum(piece.count(piece) for piece in chess.values()) > len(piece):
        return False

    return True 



chessboard = {
    'bking': 'e1', 'wking': 'e8',
    'brook': 'a1', 'wrook': 'h8',
    'bknight': 'b1', 'wknight': 'g8',
    'bbishop': 'c1', 'wbishop': 'f8',
    'bqueen': 'd1', 'wqueen': 'd8',
    'bpawn': 'a2', 'wpawn': 'h7'
}

print(chessValue(chessboard))  

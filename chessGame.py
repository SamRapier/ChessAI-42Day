import piece

def startingPieces(colour):
    tmpPieces = []

    if colour == "W":
        y = 0
        y2 = 1
    elif colour == "B": 
        y = 7
        y2 = 6
    else:
        print("ERROR - colour is not valid")
        return []

    # adding pawns
    for i in range(8):
        tmpPieces.append(piece.Pawn(i, y2, colour))

    # adding rooks
    tmpPieces.append(piece.Rook(0, y, colour))
    tmpPieces.append(piece.Rook(7, y, colour))

    # adding knights
    tmpPieces.append(piece.Knight(1, y, colour))
    tmpPieces.append(piece.Knight(6, y, colour))

    # adding bishops
    tmpPieces.append(piece.Bishop(2, y, colour))
    tmpPieces.append(piece.Bishop(5, y, colour))

    # adding queen
    tmpPieces.append(piece.Queen(3, y, colour))

    # adding king
    tmpPieces.append(piece.King(4, y, colour))


    return tmpPieces

def gameSetup():
    whitePieces = startingPieces("W")
    blackPieces = startingPieces("B")

    return [whitePieces, blackPieces]


gamePieces = gameSetup()
print(gamePieces)
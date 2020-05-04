class Piece():
    """ Super Class for a piece on a chess board
        - Has a position
        - Has a list of legal moves
        - Can perform a move
        - Has functions to find legal moves vertically, horizontally, diagonally
    """

    def __init__(self, x, y):
        """Initialises the position of the piece and the legal moves list"""
        self.position = (x, y)
        self.legalMoves = []
        self.firstMove = True
        self.directionLock = False

    def move(self, x, y, gameState):
        """ Boilerplate code for a move
            - x, y are the co-ords of the new potential position
            - Move is made if it is legal
            - Need to check if another piece is in the position
        """
        # checks if a move is legal 
        if (x,y) in self.legalMoves:
            self.position = (x,y)
        
        # check if a piece should be taken
        if (x,y) in gameState:
            #TODO: needs work
            print("Piece is taken")

        if self.firstMove:
            self.firstMove = False

    def findVertical(self, dist, gameState):
        """ finds the legal vertical moves
            - dist is the maximum distance vertical the piece can move, if negative there is no maximum
            - gameState holds the position of all the other pieces
        """
        # gets the position so it can be manipulated in for the logic 
        # without changing the actual position
        x, y = self.position

        # if dist is <1 there is no maximum number of moves
        if dist < 0:
            max_pos = 7
            min_pos = 0
        else:
            # bounds check
            # set the maximum to the distance plus the current position
            max_pos = y + dist
            min_pos = y - dist

            if max_pos > 7:
                max_pos = 7

            if min_pos < 0:
                min_pos = 0            


        # move up the board
        tmp_y = y
        # add each position to legal moves 
        while (tmp_y < max_pos):
            tmp_y += 1

            if not self.checkLegality(x, tmp_y, gameState):
                break
            
        # can only move backwards if there is no direction lock
        if not self.directionLock:
            # move down the board
            tmp_y = y
            while (tmp_y > min_pos):
                tmp_y += 1

                if not self.checkLegality(x, tmp_y, gameState):
                    break


    def findHorizontal(self, dist, gameState):
        """ finds the legal Horizontal moves
            - dist is the maximum distance horizontal the piece can move, if negative there is no maximum
            - gameState holds the position of all the other pieces
        """
        # gets the position so it can be manipulated in for the logic 
        # without changing the actual position
        x,y = self.position

        # sets the maximum & minimum position that the piece can move
        if dist < 0:
            max_pos = 7
            min_pos = 0
        else:
            # bounds check
            max_pos = x + dist
            min_pos = x - dist

            if max_pos > 7:
                max_pos = 7

            if min_pos < 0:
                min_pos = 0

    
        # test right moves
        tmp_x = x
        while(tmp_x < max_pos):
            tmp_x += 1

            if not self.checkLegality(tmp_x, y, gameState):
                break
        
        # test left moves
        tmp_x = x
        while (tmp_x > min_pos):
            tmp_x -= 1

            if not self.checkLegality(tmp_x, y, gameState):
                break
    
    def findDiagonal(self, dist, gameState):
        """ finds the legal Diagonal moves
            - dist is the maximum distance diagonal the piece can move, if negative there is no maximum
            - gameState holds the position of all the other pieces
        """
        # gets the position so it can be manipulated in for the logic 
        # without changing the actual position
        x,y = self.position

        # sets the maximum & minimum position that the piece can move
        if dist < 0:
            max_pos_x, max_pos_y = 7
            min_pos_x, min_pos_y = 0
        else:
            max_pos_x = x + dist
            min_pos_x = x - dist
            max_pos_y = y + dist
            min_pos_y = y - dist
            
            # bounds check
            if max_pos_x > 7:
                max_pos_x = 7

            if max_pos_y > 7:
                max_pos_y = 7

            if min_pos_x < 0:
                min_pos_x = 0

            if min_pos_y < 0:
                min_pos_y = 0

        # diagonal, up-right
        tmp_y = y
        tmp_x = x
        while (tmp_x < max_pos_x and tmp_y < max_pos_y):
            tmp_x += 1
            tmp_y += 1

            if not self.checkLegality(self, tmp_x, tmp_y, gameState):
                break
        
        # diagonal, up left
        tmp_y = y
        tmp_x = x         
        while (tmp_x > min_pos_x and tmp_y < max_pos_y):
            tmp_x -= 1
            tmp_y += 1

            if not self.checkLegality(self, tmp_x, tmp_y, gameState):
                break


        # can only move backwards if there is no direction lock
        if not self.directionLock:
            # diagonal, down left
            tmp_y = y
            tmp_x = x         
            while (tmp_x > min_pos_x and tmp_y > min_pos_y):
                tmp_x -= 1
                tmp_y -= 1

                if not self.checkLegality(self, tmp_x, tmp_y, gameState):
                    break

                
            # diagonal, down right
            tmp_y = y
            tmp_x = x         
            while (tmp_x < max_pos_x and tmp_y > min_pos_y):
                tmp_x += 1
                tmp_y -= 1

                if not self.checkLegality(self, tmp_x, tmp_y, gameState):
                    break


    def checkLegality(self, x, y, gameState):
        # if no piece is in this position, it is a legal move
        if(x, y) not in gameState:
            self.legalMoves.append((x, y))
            return True
        
        # if there is a piece in the way, it is only legal if it is an enemy piece 
        # however, no more positions can be added since pieces cannot jump
        else:
            # TODO: check if it is enemy piece
            self.legalMoves.append((x, y))
            return False


class Queen(Piece):
    """ Class for the queen piece, can move vertiaclly, horizontally, diagonally any number of squares
    """

    def findLegalMoves(self, gameState):
        """ Adds any legal move for the queen to the legal move list
            - Takes the gameState as an input
            - Finds vertical moves
            - Finds horizontal moves
            - Finds diagonal moves
        """

        self.findVertical(-1, gameState)
        self.findHorizontal(-1, gameState)
        self.findDiagonal(-1, gameState)

class Rook(Piece):
    """ Class for the rook piece, can move vertiaclly, horizontally any number of squares
    """

    def findLegalMoves(self, gameState):
        """ Adds any legal move for the rook to the legal move list
            - Takes the gameState as an input
            - Finds vertical moves
            - Finds horizontal moves
        """
        self.findVertical(-1, gameState)
        self.findHorizontal(-1, gameState)

class Bishop(Piece):
    """ Class for the rook piece, can move diagonally any number of squares
    """

    def findLegalMoves(self, gameState):
        """ Adds any legal move for the bishop to the legal move list
            - Takes the gameState as an input
            - Finds diagonal moves
        """
        self.findDiagonal(-1, gameState)


class King(Piece):
    """ Class for the King piece, can move vertiaclly, horizontally, diagonally 1 square
    """

    def findLegalMoves(self, gameState):
        """ Adds any legal move for the King to the legal move list
            - Takes the gameState as an input
            - Finds vertical moves
            - Finds horizontal moves
            - Finds diagonal moves
        """

        self.findVertical(1, gameState)
        self.findHorizontal(1, gameState)
        self.findDiagonal(1, gameState)

        # Need to add castling capability


# TODO: fix pawn piece
class Pawn(Piece):
    """ Class for the pawn piece, currently checks for any legal pawn moves
    """

    def __init__(self, x, y):
        super().__init__(x, y)
        self.directionLock = True

    def findLegalMoves(self, gameState):
        """ Adds any legal move to the legal move list
            - Takes the gameState as an input
            - Checks for the special two square starting move
            - checks for attacks
            - TODO: Needs to check for En passant rule
            - TODO: Needs to check for Promotion
            - TODO: Currently only from whites perspective
        """

        # first mve allows pawn to move 2 steps forward
        if self.firstMove:
            self.findVertical(2, gameState)
        else:
            self.findVertical(1, gameState)

        # TODO: pawn can attack diagonally, not currently correct
        self.findDiagonal(1, gameState)

# TODO: Knight piece

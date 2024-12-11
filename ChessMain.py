'''
Main driver file. Responsible for handling user input and displaying current GameState object.
'''
import pygame as p
import ChessEngine

WIDTH = HEIGHT = 512 # Could be 400
DIMENSION = 8 # 8x8 chess board
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15 # For animations
IMAGES = {}

'''
Initialize a global directionary of images. This will only be called once.
'''
def loadImages():
    pieces = ['wp', 'wR', 'wN', 'wB', 'wQ', 'wK', 'bp', 'bR', 'bN', 'bB', 'bQ', 'bK']
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load('images/' + piece + '.png'), (SQ_SIZE, SQ_SIZE)) # You can access an image by saying 'IMAGES['wp']'

'''
The main driver for the code. This will handle user input and updating the graphics
'''
def main():
    p.init()
    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color('white'))
    gs = ChessEngine.GameState()
    validMoves = gs.getValidMoves()
    moveMade = False # Flag variable for when a move is made

    loadImages() # Only do this once, before the while loop
    running = True
    sqSelected = () # No square is selected, keep track of the last user click (tuple: (row, col))
    playerClicks = [] # Keep track of player clicks (two tuples: [(6,4), (4, 4)])

    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
            # Mouse handler
            elif e.type == p.MOUSEBUTTONDOWN:
                location = p.mouse.get_pos() # (x, y) location of the mouse cursor
                col = location[0]//SQ_SIZE
                row = location[1]//SQ_SIZE
                if sqSelected == (row, col):
                    sqSelected = () # Deselect
                    playerClicks = [] # Clear player clicks
                else:
                    sqSelected = (row, col)
                    playerClicks.append(sqSelected) # Append for 1st and 2nd clicks
                if len(playerClicks) == 2: # After the 2nd click
                    move = ChessEngine.Move(playerClicks[0], playerClicks[1], gs.board)
                    print(move.getChessNotation())
                    for i in range(len(validMoves)):
                        if move == validMoves[i]:
                            gs.makeMove(move)
                            moveMade = True
                            sqSelected = () # Reset user clicks
                            playerClicks = []
                    if not moveMade:
                        playerClicks = [sqSelected]
            # Key handlers
            elif e.type == p.KEYDOWN:
                if e.key == p.K_z: # Undo when 'z' is pressed
                    gs.undoMove()
                    moveMade = True

        if moveMade:
            validMoves = gs.getValidMoves()
            moveMade = False

        drawGameState(screen, gs)
        clock.tick(MAX_FPS)
        p.display.flip()

'''
Responsible for graphics within a current game state.
'''
def drawGameState(screen, gs):
    drawBoard(screen) # Draw squares on the board
    drawPieces(screen, gs.board) # Draw pieces on the squares

'''
Draw the squares on the board.
'''
def drawBoard(screen):
    colors = [p.Color('white'), p.Color('gray')]
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            color = colors[((r+c) % 2)]
            p.draw.rect(screen, color, p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))

'''
Draws the pieces on the board using the current GameState.board
'''
def drawPieces(screen, board):
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            piece = board[r][c]
            if piece != '--': # Not an empty square
                screen.blit(IMAGES[piece], p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))

if __name__ == '__main__':
    main()
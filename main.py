from graphics import *
from staticValues import *
from settingsWindow import *
from classBoard import *
from functionHumanStrategy import *
from functionAiStrategy import *
from functionEvaluation import *
from classPlayer import *
import messages

def main():
    """This is the main function"""

    # Getting the settings fot the current gameplay from the setup window
    playerOneStrategy, playerOneColor, playerTwoStrategy, playerTwoColor, rows, cols = settingsDraw()

    # Setting up the game
    width = min(cols*100, MAX_WIDTH)
    height = (width / cols) * rows
    gameWindow = GraphWin("Connect Four", width, height)
    gameWindow.setBackground("white")
    gameWindow.setCoords(0, 0, width, height)
    board = Board(rows, cols, gameWindow, width, height)
    board.draw()
    player1 = Player(1, playerOneColor, playerOneStrategy, board)
    player2 = Player(2, playerTwoColor, playerTwoStrategy, board)

    # Main game loop
    while not gameWindow.isClosed():

        player1.move()
        if board.isOver():
            break

        player2.move()
        if board.isOver():
            break

    gameWindow.close()


# Running the main function
if __name__ == "__main__":
    main()

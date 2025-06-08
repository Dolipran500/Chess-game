# Chess Game in Python
#### Video Demo: `https://youtu.be/p-_If_-Gz2Y`
#### Description:
This project is a Python-based implementation of a game of chess using the `pygame` library. Although incomplete (still in development), it allows two players to compete against each other with a graphical user interface that visualizes the chessboard and pieces. The game includes basic move input and automatic move logging.
The bulk of the game was designed in Thonny, and some minor corrections and implementations were in the CS50 Codespace.

## Features
Playable against another human player
Graphical user interface using `PyGame`
- Basic move input
- The ability to capture pieces
- Move Logging
## Technology
Thonny: This was my primary development framework. I have used it before in CS50 assignments, as it's simple enough and performs well for simple GUI programs.
### Prerequisites
**Python 3.x:** This project is compatible with Python 3.8 and later versions. Ensure that Python is installed on your system.

**`pygame 2.0.1` Library:** The game relies on the `pygame` library for rendering the graphical interface. If `pygame` is not installed, **you will _need_ to install it**.

## How Does it work ?
### ChessEngine Overview

The <code style="color : Aqua">ChessEngine</code> is _crucial_ for managing the logic and state of the chess game. It consists of two main classes: **gamestate** and **Move**.

1. <code style="color : Gold">Gamestate Class</code>

The gamestate class encapsulates the current state of the chess game, including mapping the board and the history of moves made.

2. <code style="color : Gold">MakeMove</code> Method:

This method updates the board by moving a piece from its start position to its end position. It also records the move in movelog. The board’s state is modified by setting the starting position to "--" (an empty square) and placing the piece at the ending position.


The <code style="color : Gold">Move</code> class represents a single move in the chess game. It includes methods for converting between board coordinates and chess notation (**(6,4)** to **(e2)**). In chess, fields on the board are described by two symbols, one of them being number between 1-8 (which is corresponding to rows) and the second one being a letter between a-f (corresponding to columns), in order to use this notation we need to map our [row][col] coordinates to match the ones used in chess.

<code style="color : Gold">getChessNotation</code> Method:
Converts the move into algebraic chess notation. It handles captures by appending an "x" and represents pawn moves simply by the destination square.

### chess_main Overview
The <code style="color : Aqua">chess_main</code> is where the bulk of the program is written and activated.

<code style="color : Gold">loadimages()</code>:
Loads and scales images for each chess piece and stores them in the IMAGES dictionary (should be with the sent file).

<code style="color : Gold">drawgamestate(screen, gs)</code>:
Calls drawboard and drawpieces to update the display with the current game state.

<code style="color : Gold">drawboard(screen)</code>:
Draws the chessboard with alternating colors.

<code style="color : Gold">drawpieces(screen, board)</code>:
Draws the chess pieces on the board according to the board state.

<code style="color : Gold">drawMoveLog(screen, gs, font)</code>:
Draws a panel to the right of the chessboard displaying the log of moves made in the game. It organizes and renders text entries of the moves.

<code style="color : Gold">main()</code>:
The central function that initializes pygame, sets up the display, handles the game loop, processes user input, updates the game state, and refreshes the display. It captures mouse events for moving pieces and calls relevant functions to update the game state and user interface.

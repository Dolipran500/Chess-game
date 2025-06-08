import pygame as p #this module is essential for the program to function
import sys
import ChessEngine #importing the engine responsible for
MOVE_LOG_PANEL_WIDTH = 250
MOVE_LOG_PANEL_HEIGHT = 512
BOARD_WIDTH = BOARD_HEIGHT = 512
DIMENSION = 8 #square shape for the board(8x8)
SQ_SIZE = BOARD_HEIGHT // DIMENSION
MAX_FPS = 60 #locked fps
IMAGES ={}
#initialise a dictionary for images
def loadimages():
    pieces=["wp","bp","bQ","bK","bR","bN","bB","wQ","wK","wR","wB","wN"]
    for piece in pieces:
        IMAGES[piece]= p.transform.scale(p.image.load("images/" + piece + ".png"),(SQ_SIZE,SQ_SIZE))
        #giving access to the images
def drawgamestate(screen,gs):
    drawboard(screen)
    drawpieces(screen,gs.board)
def drawboard(screen):
    colors = [p.Color("white"),p.Color("gray")]
    for i in range(DIMENSION):
        for j in range(DIMENSION):
            color=colors[((i+j)%2)]
            p.draw.rect(screen,color,p.Rect(j*SQ_SIZE,i*SQ_SIZE,SQ_SIZE,SQ_SIZE))
def drawpieces(screen,board):
    for i in range(DIMENSION):
        for j in range(DIMENSION):
            piece=board[i][j]
            if piece!="--":
                screen.blit(IMAGES[piece],p.Rect(j*SQ_SIZE,i*SQ_SIZE,SQ_SIZE,SQ_SIZE))

def drawMoveLog(screen, gs, font):
#draws the move log
    move_log_rect = p.Rect(BOARD_WIDTH, 0, MOVE_LOG_PANEL_WIDTH, MOVE_LOG_PANEL_HEIGHT)
    p.draw.rect(screen, p.Color('black'), move_log_rect)
    move_log = gs.movelog
    move_texts = []
    for i in range(0, len(move_log), 2):
        move_string = str(i // 2 + 1) + '. ' + str(move_log[i]) + " "
        if i + 1 < len(move_log):
            move_string += str(move_log[i + 1]) + "  "
        move_texts.append(move_string)

    moves_per_row = 3
    padding = 5
    line_spacing = 2
    text_y = padding
    for i in range(0, len(move_texts), moves_per_row):
        text = ""
        for j in range(moves_per_row):
            if i + j < len(move_texts):
                text += move_texts[i + j]

        text_object = font.render(text, True, p.Color('white'))
        text_location = move_log_rect.move(padding, text_y)
        screen.blit(text_object, text_location)
        text_y += text_object.get_height() + line_spacing

def main():
    p.init()
    screen = p.display.set_mode((BOARD_WIDTH + MOVE_LOG_PANEL_WIDTH,BOARD_HEIGHT))
    clock= p.time.Clock()
    screen.fill(p.Color("white"))
    gs=ChessEngine.gamestate()
    loadimages()
    move_log_font = p.font.SysFont("Arial", 14, False, False)
    square_selected= ()#using a tuple to store location (x,y)
    player_clicks= []#list that stores 2 locations :origin et destination [(x1,y1),(x2,y2)]
    running = True
    while running:
        for event in p.event.get():
            if event.type == p.QUIT:
                p.quit()  #screen exit
                running = False
                sys.exit()
            elif event.type == p.MOUSEBUTTONDOWN:
                    location = p.mouse.get_pos()  # (x, y) location of the mouse
                    col = location[0] // SQ_SIZE
                    row = location[1] // SQ_SIZE
                    if square_selected == (row, col):  # user clicked the same square twice
                        square_selected = ()  # deselect
                        player_clicks = []  # clear clicks
                    else:
                        square_selected = (row, col)
                        player_clicks.append(square_selected)  # append for both 1st and 2nd click
                    if len(player_clicks) == 2:  # after 2nd click
                        move = ChessEngine.Move(player_clicks[0], player_clicks[1], gs.board)
                        gs.makemove(move)
                        square_selected = ()  # reset user clicks
                        player_clicks = []

        clock.tick(MAX_FPS)
        p.display.flip()
        drawgamestate(screen,gs)
        drawMoveLog(screen,gs,move_log_font)
main()










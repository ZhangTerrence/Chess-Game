import pygame

pygame.init()
pygame.display.set_caption("Chess")
WIDTH, HEIGHT = 850, 850
PALETTE = [(227,193,111), (184,139,74)]
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))

CHESS_POS = [[41,21,31,51,61,31,21,41],[11,11,11,11,11,11,11,11],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0],[10,10,10,10,10,10,10,10],[40,20,30,50,60,30,20,40]]
CHESS_DIC = {
    10: "WPawn.png",
    20: "WKnight.png",
    30: "WBishop.png",
    40: "WRook.png",
    50: "WQueen.png",
    60: "WKing.png",
    11: "BPawn.png",
    21: "BKnight.png",
    31: "BBishop.png",
    41: "BRook.png",
    51: "BQueen.png",
    61: "BKing.png",
}

def draw(board):
    switch = 0
    for x in range(8):
        for y in range(8):
            pygame.draw.rect(WINDOW, PALETTE[switch], pygame.Rect(100 * x + 25, 100 * y + 25, 100, 100))
            if board[y][x] in CHESS_DIC:
                WINDOW.blit(pygame.image.load("img/"+CHESS_DIC[board[y][x]]), (100 * x + 42.5, 100 * y + 42.5))
            switch = 1 - switch
        switch = 1 - switch
    pygame.draw.lines(WINDOW, PALETTE[1], True, [(25, 25), (825, 25), (825, 825), (25, 825)])

def game(board):
    running = True
    player = "White"
    while running:
        WINDOW.fill((255,255,255))
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                if 25 < pos[0] < 825 and 25 < pos[1] < 825:
                    x_index, y_index = pos[0]//100, pos[1]//100
                    if board[y_index][x_index] in CHESS_DIC:
                        print(CHESS_DIC[board[y_index][x_index]])
            if event.type == pygame.QUIT:
                running = False
        draw(board)
        pygame.display.update()

if __name__ == '__main__':
    game(CHESS_POS)
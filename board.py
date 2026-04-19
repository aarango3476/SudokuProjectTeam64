import sudoku_generator
from cell import Cell
import pygame
import sys

class Board:
    def __init__(self, WIDTH, HEIGHT, screen, difficulty):
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.screen = screen
        self.difficulty = difficulty
        self.selected=(-1,-1)
        self.board=sudoku_generator.generate_sudoku(9, difficulty)
        self.cells=[
            [Cell(self.board[i][j],i,j,self.screen) for j in range(WIDTH)]
            for i in range(HEIGHT)

        ]

    def draw_board(self):
        #  horizontal liness
        for i in range(1, 3):
            pygame.draw.line(
                screen,
                (245, 152, 66),
                (0, i * 300),
                (900, i * 300),
                15
            )
        for i in range(1, 9):
            pygame.draw.line(
                screen,
                (245, 152, 66),
                (0, i * 100),
                (900, i * 100),
                3)
        #vertical liness
        for i in range(1, 3):
            pygame.draw.line(
                screen,
                (245, 152, 66),
                (i * 300, 0),
                (i * 300, 900),
                15
            )
        for i in range(1, 9):
            pygame.draw.line(
                screen,
                (245, 152, 66),
                (i * 100, 0),
                (i * 100, 900),
                3
            )


        for row in self.cells:
            for cell in row:
                cell.draw()

    def select(self,row,col):
        self.selected=(row,col)


    def sketch(self,value):
        row,col=self.selected
        for r in self.cells:
            for cell in r:
                if cell.row==row and cell.col==col:
                    cell.set_sketched_value(value)

#
# pygame.init()
# screen = pygame.display.set_mode((900, 900))
# pygame.display.set_caption("Sudoku")
# screen.fill((0,0,0))
#
# b=Board(9,9,screen,30)
# b.draw_board()
# # c=Cell(6,0,1,screen)
# # c1=Cell(0,0,2,screen)
# # c.draw()
# # c1.draw()
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit()
#     pygame.display.update()


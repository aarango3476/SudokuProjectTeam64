import sys

import pygame
class Cell:
    def __init__(self, value,row,col,screen):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen
        self.sketched_val=0

    def set_cell_value(self,value):
        self.value = value

    def set_sketched_value(self,value):
        self.sketched_val = value

    def draw(self):
        num_font=pygame.font.Font(None,100)
        num_surf=num_font.render(str(self.value),1,(100,100,100))

        if self.value!=0:
            num_rect=num_surf.get_rect(center=(self.col*100+100/2,self.row*100+100/2))
            self.screen.blit(num_surf,num_rect)

# pygame.init()
# screen = pygame.display.set_mode((900, 900))
# pygame.display.set_caption("Sudoku")
# screen.fill((0,0,0))
#
# c=Cell(6,0,1,screen)
# c1=Cell(0,0,2,screen)
# c.draw()
# c1.draw()
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit()
#     pygame.display.update()
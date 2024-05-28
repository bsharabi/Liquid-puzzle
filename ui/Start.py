from .GuiController import *
from .menu import *
from components.widgets import *
import os

class Start(GuiController):
    
    def __init__(self):
        super().__init__()
        display.set_caption("Liquid Pazzle")
        # Load images
        self.image = pg.image.load(os.path.join('data', 'Images', 'start_background.jpg'))
        self.header = pg.image.load(os.path.join('data', 'Images', 'image.png'))
        
        self.header_size = self.header.get_size()
        
        
    def handleClick(self,event):
        pass

    def handleButtonPress(self, event):
        self.next = True

    def handleWheel(self, event):
        pass

    def shouldAdvance(self):   
        return self.next

    def getNextViewController(self):
        self.next_view=Menu()
        return self.next_view

    def draw_screen(self):

        self.screen.fill(PALETTE["purple"])
        self.screen.blit(self.image,(0,0))  
        header_x = (WIDTH - self.header_size[0]) // 2
        header_y = (HEIGHT - self.header_size[1]) // 2
        self.screen.blit(self.header, (header_x, header_y))
         
        pg.display.update()
        self.clock.tick(REFRASH)

    def __del__(self):
        print("GUI_Panel is distroy")
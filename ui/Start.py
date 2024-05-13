from .GuiController import *
from .menu import *
from components.widgets import *

class Start(GuiController):
    def __init__(self):
        super().__init__()
        display.set_caption("Liquid Pazzle")
        self.image = pg.image.load('./data/images/liquidPazzle.png')
        

    def handleClick(self,event):
        pass

    def handleButtonPress(self, event):
        self.next_view = True

    def handleWheel(self, event):
        pass

    def shouldAdvance(self):   
        return self.next_view

    def getNextViewController(self):
        return Menu()

    def draw_screen(self):

        self.screen.fill(palette["white"])
        self.screen.blit(self.image, (0, 0))  
        pg.display.update()
        self.clock.tick(REFRASH)


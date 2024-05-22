from .GuiController import *
from .options import *
from .Gui import *
from api.IAlgo import *
from components.widgets import *
from ui.Game import Game

class Menu(GuiController):
    def __init__(self):

        super().__init__()    
        display.set_caption("Liquid Pazzle - Menu")
        self.image = pg.image.load('data\Images\menu_background.jpg')
        self.image = pg.transform.scale(self.image, (WIDTH, HEIGHT))
        
        self.startButton = Button(
            Rectangle(((WIDTH-150)//2,((HEIGHT-32)//2)), (150, 32)),
            Label("Start", self.font),
            PALETTE["green"],
            PALETTE["light-green"],
            PALETTE["white"])
        

        self.optionsButton = Button(
            Rectangle(((WIDTH-150)//2,((HEIGHT-32)//2)+50), (150, 32)),
            Label("Options", self.font),
            PALETTE["red"], 
            PALETTE["light-red"], 
            PALETTE["white"])
        
        self.quitButton = Button(
            Rectangle(((WIDTH-150)//2,((HEIGHT-32)//2)+100), (150, 32)),
            Label("Quit", self.font),
            PALETTE["purple"], 
            PALETTE["gray"], 
            PALETTE["white"])
        
        self.start = False
        self.options = False
        self.quit = False

    def handleClick(self,event):
        
        if self.startButton.mouse_hover():
            self.start = True
        elif self.optionsButton.mouse_hover():
            self.options = True
        elif self.quitButton.mouse_hover():
            self.quit = True

    def handleButtonPress(self, event):
        pass

    def handleWheel(self, event):
        pass

    def shouldAdvance(self):   
        if self.start or self.options or self.quit:
            self.sound_effect["click"].play()
            return True
        return False

    def getNextViewController(self):
        if self.start:
             return Game()
        elif self.options:
            return options()
        elif self.quit:
            return None
        

    def draw_screen(self):

        self.screen.fill(PALETTE["white"])
        self.screen.blit(self.image,(0,0))
        self.startButton.draw_button(self.screen, True)
        self.optionsButton.draw_button(self.screen, True)
        self.quitButton.draw_button(self.screen, True)
        pg.display.update()
        self.clock.tick(REFRASH)
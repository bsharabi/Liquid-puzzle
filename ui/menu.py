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
       

        self.startButton = Button(
            Rectangle((200, 100), (100, 32)),
            Label("Start", self.font),
            palette["green"],
            palette["light-green"],
            palette["white"])
        

        self.optionsButton = Button(
            Rectangle((200, 150), (100, 32)),
            Label("Options", self.font),
            palette["red"], 
            palette["light-red"], 
            palette["white"])
        
        self.quitButton = Button(
            Rectangle((200, 200), (100, 32)),
            Label("Quit", self.font),
            palette["purple"], 
            palette["gray"], 
            palette["white"])
        
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
        return self.start or self.options or self.quit

    def getNextViewController(self):
        if self.start:
             return Game()
        elif self.options:
            return options()
        elif self.quit:
            return None
        

    def draw_screen(self):

        self.screen.fill(palette["white"])
        self.startButton.draw_button(self.screen, True)
        self.optionsButton.draw_button(self.screen, True)
        self.quitButton.draw_button(self.screen, True)
        pg.display.update()
        self.clock.tick(REFRASH)
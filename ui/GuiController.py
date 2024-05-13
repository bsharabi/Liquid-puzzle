from api.lib import *
from api.setting import *
from api.IAlgo import IAlgo
from logic.Algo import Algo

class GuiController:

    def __init__(self):
        self.algo:IAlgo = Algo()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT),depth=32)
        self.clock = pg.time.Clock()
        self.font = pg.font.SysFont("Arial", 24, bold=True)
        self.music_on = True  
        self.difficulty_level = 0.5
        self.next_view = False
       

    def shouldAdvance(self):

        # override this
        pass

    def getNextViewController(self):

        # override this
        pass
    
    def getPrevViewController(self):

        # override this
        pass

    def handleClick(self):

        # override this
        pass

    def handleButtonPress(self, event):

        # override this
        pass

    def handleWheel(self, event):

        # override this
        pass

    def draw_screen(self):

        # override this
        pass

    def __del__(self):
        # print("Viewer controller is distroy")
        pass


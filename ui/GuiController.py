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
        self.prev_view =False
        
        self.sounds:dict[str,str]={
            "start":"data\sound\Kevin_MacLeod_-_Canon_in_D_Major(chosic.com)"
            
        }
        self.sound_effect:dict[str,pg.mixer.Sound]={
            "click":pg.mixer.Sound("data\sound\system-notification-199277.mp3"),
            "win":pg.mixer.Sound("data\sound\system-notification-199277.mp3"),
        }
       

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


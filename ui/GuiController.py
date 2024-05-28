from api.lib import *
from api.setting import *
from api.IAlgo import IAlgo
from logic.Algo import Algo
import os

class GuiController:
    
    

    def __init__(self):
        self.algo:IAlgo = Algo()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT),depth=32)
        self.clock = pg.time.Clock()
        self.font = pg.font.SysFont("Arial", 24, bold=True)
        self.music_on = True  
        self.difficulty_level = 0.5
        self.next_view = None
        self.prev_view =None
        self.next=False
        self.prev=False
        self.resume=False
      
 
        
        self.sounds:dict[str,str]={
            "start":os.path.join(r"data\sound\Kevin_MacLeod_-_Canon_in_D_Major(chosic.com)")          
        }
        self.sound_effect:dict[str,pg.mixer.Sound]={
            "click":pg.mixer.Sound(os.path.join(r'data\sound\click.mp3')),
            "win":pg.mixer.Sound(os.path.join(r'data\sound\click.mp3')),
        }
    
    def build_image(self,file_path:str,dim:tuple[int,int]=(None,None)) -> Surface:
        image = pg.image.load(file_path)
        if all(dim): 
            image = pg.transform.scale(image, dim)
        return image
    
    def set_timer(self):
        # override this
        pass

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


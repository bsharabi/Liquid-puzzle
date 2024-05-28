from  .Start import Start
from api.lib import *

class GUI_Panel:
 
    def __init__(self) -> None:
        pg.display.set_caption('Liquid puzzle')
        pg.init()
        pg.font.init()
        pg.mixer.init()
        self.timer_event = pygame.USEREVENT + 1
        pg.time.set_timer(self.timer_event, 1000)
        pg.mixer.music.load(r"data\sound\Kevin_MacLeod_-_Canon_in_D_Major(chosic.com).mp3")
        # pg.mixer.music.play(-1)
        self.GuiController = Start()
    
    def __call__(self):
        running = True
        
        while running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
                elif event.type == pg.KEYDOWN:
                    self.GuiController.handleButtonPress(event)
                elif event.type == pg.MOUSEBUTTONDOWN:
                    if 1 <= event.button <= 2:
                        self.GuiController.handleClick(event)
                elif event.type == pg.MOUSEWHEEL:
                    self.GuiController.handleWheel(event)
                elif event.type == self.timer_event:
                    self.GuiController.set_timer()
            if self.GuiController.shouldAdvance():
                self.GuiController = self.GuiController.getNextViewController()
                if self.GuiController ==None:
                    running=False
                    continue
            self.GuiController.draw_screen()
        return running
       
    def __del__(self):
        print("GUI_Panel is distroy")
    

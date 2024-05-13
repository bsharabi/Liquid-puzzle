from .GuiController import *
from components.widgets import *
from ui.Game import Game
from components.widgets import *
import api.IAlgo as IAlgo 
from ui.Game import Game

class options(GuiController):
    def __init__(self):
        super().__init__()
        pg.display.set_caption("Options")

        
        self.music_button = Button(
            Label("Music On" if self.music_on else "Music Off", self.font), 
            Rectangle((WIDTH // 2 - 50, HEIGHT// 2 - 50), (100, 32)),
            palette["green"],
            palette["light-green"],
            palette["white"])

       
        self.seek_bar = SeekBar(Rectangle((WIDTH // 2 - 100, HEIGHT // 2),
                                          (200, 20)), self.difficulty_level,palette["green"])
        
        
    def handleClick(self, event):
        if self.music_button.mouse_hover():
            self.music_on = not self.music_on
            self.music_button.label.text = "Music On" if self.music_on else "Music Off"
        self.seek_bar.handle_event(event)

    def handleButtonPress(self, event):
        pass

    def handleWheel(self, event):
        pass

    def shouldAdvance(self):
        return self.next_view

    def getNextViewController(self):
        return Game(self.algo)

    def draw_screen(self):
        self.screen.fill(palette["white"])

        # Draw music button
        self.music_button.draw_button(self.screen, True)

        # Draw seek bar
        self.seek_bar.draw_seek_bar(self.screen)

        pg.display.update()
        self.clock.tick(REFRASH)


from logic.parser import Parser
from api.lib import *
from api.IAlgo import IAlgo
from copy import *
from .GuiController import *
from components.widgets import *


class Game(GuiController):
  
    def __init__(self) -> None:
        super().__init__()
        self .parser = Parser("example.csv","example.csv")
        display.set_caption("Liquid Pazzle - Game")
        self.image = pg.image.load('data\Images\game_bakground.jpg')
        self.image = pg.transform.scale(self.image, (WIDTH, HEIGHT))
        self.index_solve=0
        self.empty = 2
        self.full = 8
        self.size = 8
        self.colors = 8
        self.tubes_number=self.size+self.empty
        self.tubes_color,self.diff_color_per_tube =self.algo.generate_tubes(self.full,self.size,self.colors,self.empty)
        self.solve,self.time_taken = self.algo(self.tubes_color)
        self.resualt_dict = self.parser.init_dict(self.tubes_color,self.empty,self.full,self.size,self.colors,self.diff_color_per_tube,len(self.solve),self.solve,self.time_taken)
        self.parser.writer(self.resualt_dict)
        self.deepcopy=deepcopy(self.tubes_color)
        self.select_box=0
        self.win=False
        self.index=0
        self.undo = [deepcopy(self.tubes_color)]
        self.selected = False
       
    def handleClick(self,event):
      
        if not self.selected:
            for item in range(len(self.tube_rects)):
                if self.tube_rects[item].collidepoint(event.pos):
                    self.selected = True
                    self.select_box = item
        else:
            for item in range(len(self.tube_rects)):
                if self.tube_rects[item].collidepoint(event.pos):
                    dest_rect = item
                    self.tubes_color = self.calc_move(self.tubes_color, self.select_box, dest_rect)
                    self.selected = False
                    self.select_box = 100
        print(self.select_box)
        pass
     
    def handleButtonPress(self, event):

        if self.win and event.key==13:
            print("Winn")
            self.tubes_color,self.diff_color_per_tube = self.algo.generate_tubes(self.full,self.size,self.colors,self.empty)
            self.solve,self.time_taken = self.algo(self.tubes_color)
            self.index_solve=0
            self.deepcopy=deepcopy(self.tubes_color)
            self.resualt_dict = self.parser.init_dict(self.tubes_color,self.empty,self.full,self.size,self.colors,self.diff_color_per_tube,len(self.solve),self.solve,self.time_taken)
            self.parser.writer(self.resualt_dict)
            self.win=False
        if event.key == 32 and not self.win:
            self.tubes_color=deepcopy(self.deepcopy)
            self.index_solve=0
        if event.key == 1073741904:
            print("Home")
            self.index = self.index-1 if self.index  >0 else 0
            self.tubes_color=deepcopy(self.undo[self.index])  
        if event.key == 1073741903:
            self.index = self.index+1 if len(self.undo)  < self.index+1 else self.index
            self.tubes_color=deepcopy(self.undo[self.index])     
        
    def handleWheel(self, event):
        pass

    def shouldAdvance(self):   
        pass

    def getNextViewController(self):
    
        return Game(self.algo)
    
    def getNextSolve(self):
        if(self.index_solve>=len(self.solve)):
            return
        v= self.solve[self.index_solve]
        for i in range(int(v[2])):
            item =self.tubes_color[int(v[0])].pop()
            self.tubes_color[int(v[1])].append(item)
        self.select_box = self.solve[self.index_solve][1]
        self.index_solve+=1

    def draw_screen(self):

        self.screen.fill(PALETTE["white"])
        self.screen.blit(self.image,(0,0))
        # self.select_box = 100 if self.index_solve >= len(self.solve) else self.solve[self.index_solve][0]
        self.tube_rects =  self.draw_tubes(self.tubes_color)

        self.win = self.check_victory(self.tubes_color)
       
        if self.win:
            victory_text = self.font.render('You Won! Press Enter for a new board!', True, 'white')
            self.screen.blit(victory_text, (WIDTH//3, HEIGHT -50))
        restart_text = self.font.render('Stuck? Space-Restart, Enter-New Board!', True, 'white')
        self.screen.blit(restart_text, (10, 10))
        
        self.getNextSolve()
        pg.display.update()
        self.clock.tick(REFRASH)
        # time.sleep(1)

    def draw_tubes(self, tube_cols):
        tube_boxes = []
    
        spacing = WIDTH / self.tubes_number
        s = (spacing-65)//2
        y = (HEIGHT - (50*self.size))/2 
        for i in range(self.tubes_number):
            for j in range(len(tube_cols[i])):
                pg.draw.rect(self.screen, COLOR_CHOICES[tube_cols[i][j]], [s+spacing * i, y-50+self.size*50 - (50 * j), 65, 50],0,40 if j==0 else 0,0,0)
            box = pg.draw.rect(self.screen, 'white', [s+spacing * i, y, 65, 50*self.size], 1,40,0,0)
            if self.select_box == i:
                pg.draw.rect(self.screen, 'green', [s+spacing * i, y, 65, 50*self.size],1,40,0,0)
            tube_boxes.append(box)
    
        return tube_boxes

    def calc_move(self,colors, selected_rect, destination):
        color_on_top = 100
        length = 1
        color_to_move = 100
        if len(colors[selected_rect]) > 0:
            color_to_move = colors[selected_rect][-1]
        if self.size > len(colors[destination]):
            if len(colors[destination]) == 0:
                color_on_top = color_to_move
            else:
                color_on_top = colors[destination][-1]
        if color_on_top == color_to_move:
            for i in range(length):
                if len(colors[destination]) < self.size:
                    if len(colors[selected_rect]) > 0:
                        colors[destination].append(color_on_top)
                        colors[selected_rect].pop(-1)
        if colors != self.undo[len(self.undo)-1]:
            self.undo.append(colors)
            self.index+=1
            print(self.undo)
        return colors

    def check_victory(self,colors):
        won = True
        for i in range(len(colors)):
            if len(colors[i]) > 0:
                if len(colors[i]) != self.size:
                    won = False
                else:
                    main_color = colors[i][-1]
                    for j in range(len(colors[i])):
                        if colors[i][j] != main_color:
                            won = False
        return won
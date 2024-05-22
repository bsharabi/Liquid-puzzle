from logic.parser import Parser
from api.lib import *
from api.IAlgo import IAlgo
from copy import *
from .GuiController import *
from components.widgets import *
from math import ceil, sqrt


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
        self.parser.writer( empty=self.empty, full=self.full, size=self.size, colors=self.colors,diffColor=self.diff_color_per_tube, num_step=len(self.solve),time=self.time_taken, init=self.tubes_color, steps=self.solve)
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
            self.parser.writer( empty=self.empty, full=self.full, size=self.size, colors=self.colors,diffColor=self.diff_color_per_tube, num_step=len(self.solve),time=self.time_taken, init=self.tubes_color, steps=self.solve)

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
        pg.draw.rect(self.screen,"white",RECT_CONTAINER,2,10)

        self.win = self.check_victory(self.tubes_color)
       
        if self.win:
            victory_text = self.font.render('You Won! Press Enter for a new board!', True, 'white')
            self.screen.blit(victory_text, (WIDTH//3, HEIGHT -50))
        restart_text = self.font.render('Stuck? Space-Restart, Enter-New Board!', True, 'white')
        self.screen.blit(restart_text, (10, 10))
        
        # self.getNextSolve()
        pg.display.update()
        self.clock.tick(REFRASH)
        # time.sleep(1)

    # def draw_tubes(self, tube_cols):
    #     tube_boxes = []
    
    #     c_row = self.tubes_number//NTPR
    #     height_tube = ((CONTAINER_HEIGHT*0.9)//c_row)*0.95
    #     width_tube = ((CONTAINER_WIDTH*0.9)//NTPR)*0.4
        
        
        
    #     spacing = WIDTH / self.tubes_number
    #     s = (spacing-65)//2
    #     y = (HEIGHT - (50*self.size))/2 
        
    #     for i in range(self.tubes_number):
    #         color = 'green' if self.select_box == i else 'white' 
    #         for j in range(len(tube_cols[i])):
    #             # ball_rect = Rect()
    #             # tube_rect =Rect()
    #             pass
    #             # pg.draw.rect(self.screen, COLOR_CHOICES[tube_cols[i][j]], [s+spacing * i, y-50+self.size*50 - (50 * j), 65, 50],0,40 if j==0 else 0,0,0)
    #         # box = pg.draw.rect(self.screen, color, [s+spacing * i, y, 65, 50*self.size], 1,40,0,0)
    #         box = pg.draw.rect(self.screen, color, [s+spacing * i, y,  width_tube,height_tube], 1,40,0,0)
            
    #         tube_boxes.append(box)
    
    #     return tube_boxes
    
    def draw_tubes(self, tube_cols):
        tube_boxes = []

        # Calculate the height and width of each test tube
        c_row = (self.tubes_number + NTPR - 1) // NTPR  # Number of rows needed
        height_tube = ((CONTAINER_HEIGHT * 0.9) / c_row) * 0.95
        ball_size = height_tube//self.size
        width_tube = ball_size*1.3
        
        # Calculate the vertical and horizontal spacing
        vertical_spacing = (CONTAINER_HEIGHT - (height_tube * c_row)) / (c_row + 1)
        horizontal_spacing = (CONTAINER_WIDTH - (width_tube * NTPR)) / (NTPR + 1)

        for i in range(self.tubes_number):
            row = i // NTPR
            col = i % NTPR

            x = CONTAINER_X + horizontal_spacing * (col + 1) + width_tube * col
            y = CONTAINER_Y + vertical_spacing * (row + 1) + height_tube * row

            color = 'green' if self.select_box == i else 'white'
            box = pg.draw.rect(self.screen, color, [x, y, width_tube, height_tube], 1, 40, 0, 0)
            tube_boxes.append(box)

            # Draw balls in the test tube
            for j in range(len(tube_cols[i])):
                ball_x = x + (width_tube - ball_size) // 2  # Center ball in the test tube
                ball_y = y + height_tube - (ball_size * (j + 1))  # Position balls from bottom to top
                pg.draw.rect(self.screen, COLOR_CHOICES[tube_cols[i][j]], [ball_x, ball_y, ball_size, ball_size], 0, 100)

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
from api.lib import *
from api.IAlgo import IAlgo
from copy import *
from .GuiController import *
from components.widgets import *



class Game(GuiController):
  
    def __init__(self) -> None:
        super().__init__()
        display.set_caption("Liquid Pazzle - Game")
        
        self.image =self.build_image(r'data\Images\game_bakground.jpg',(WIDTH, HEIGHT))  
        
        self.algo.initialize(filePath= "output.csv")
       
        self.select_box:int=0
        self.win:bool=False
        self.selected:bool = False
        self.steps:list[tuple[int]]=[]
        
        self.back_button = Button(
            Rectangle(BACK_BUTTON_POS, (BUTTON_WIDTH, BUTTON_HEIGHT)),
            Label("Back", self.font),
            PALETTE["green"],
            PALETTE["light-green"],
            PALETTE["white"])
        

        self.auto_solve_Button = Button(
            Rectangle(AUTO_BUTTON_POS, (BUTTON_WIDTH, BUTTON_HEIGHT)),
            Label("Auto", self.font),
            PALETTE["red"], 
            PALETTE["light-red"], 
            PALETTE["white"])
        
        self.next_step_Button = Button(
            Rectangle(NEXT_BUTTON_POS, (BUTTON_WIDTH, BUTTON_HEIGHT)),
            Label("Next", self.font),
            PALETTE["purple"], 
            PALETTE["gray"], 
            PALETTE["white"])
        
        self.prev_step_Button = Button(
            Rectangle(PREV_BUTTON_POS, (BUTTON_WIDTH, BUTTON_HEIGHT)),
            Label("Prev", self.font),
            PALETTE["purple"], 
            PALETTE["gray"], 
            PALETTE["white"])
        
        self.time_left = 60 
        self.score=0
        self.steps_number=0
        self.score_lable=RectLabel(Rectangle(SCORE_POS,SCORE_SIZE),
                Label("Score: 0", self.font),  
                PALETTE["gray"], 
                PALETTE["white"] )
        self.step_lable=RectLabel(Rectangle(STEPS_POS,STEPS_SIZE),
                Label("Step: ", self.font),  
                PALETTE["gray"], 
                PALETTE["white"] )
        
        self.auto_solve = False
        self.is_change=False
        
    
       
    def handleClick(self,event):
        
        if self.auto_solve_Button.mouse_hover():
            self.auto_solve = True
        elif self.next_step_Button.mouse_hover():
            self.getNextStep()
        elif self.back_button.mouse_hover():
            self.prev=True
        elif self.prev_step_Button.mouse_hover() and not self.win:
            self.getPrevStep()
        else:
            if not self.selected:
                for item in range(len(self.tube_rects)):
                    if self.tube_rects[item].collidepoint(event.pos):
                        self.selected = True
                        self.select_box = item
            else:
                for item in range(len(self.tube_rects)):
                    if self.tube_rects[item].collidepoint(event.pos):
                        dest_rect = item
                        self.is_change,step =self.algo.calc_move( self.select_box, dest_rect)
                        self.selected = False
                        self.select_box = 100
                        if self.is_change:
                            self.steps_number+=1
                            self.steps.append(step)
                
    
    def __init_new_game(self):
        self.steps.clear()
        self.time_left=60
        self.auto_solve=False
        self.score+=1
        self.steps_number=0
        self.score_lable.label.text=f'Score: {self.score}'
  
                        
    def handleButtonPress(self, event):
        if self.win and event.key==13:
            self.__init_new_game()
            try:
                self.algo.next_grid_df()
            except Exception as e:
                print(e)
                self.algo.initialize(full=8,size=8,colors=8,empty=2)
            self.win=False
        elif event.key == 1073741904:
            self.getPrevStep()
        elif event.key == 1073741903:
            self.getNextStep()   
        elif event.key == 32:
           self.auto_solve = True

        
    def handleWheel(self, event):
        pass

    def shouldAdvance(self):
        return self.prev 

    
    def getNextViewController(self):
        return self.prev_view
        
    
    def getPrevViewController(self):
        pass
    
    def getNextStep(self):
        if self.is_change:
            self.algo.initialize(True)
        if self.algo.hasNext():
            step=(src,dest,amt)= self.algo.next()
            src_stack:list[int] = self.algo.df["init"][src]
            dest_stack:list[int] = self.algo.df["init"][dest]
            for _ in range(amt):
                src_item = src_stack.pop()
                dest_stack.append( src_item)
            self.steps.append(step)
            self.steps_number+=1

        self.is_change=False

    def getPrevStep(self):
        if len(self.steps) != 0:
            step=(dest,src,amt)= self.steps.pop()
            src_stack:list[int] = self.algo.df["init"][src]
            dest_stack:list[int] = self.algo.df["init"][dest]
            for _ in range(amt):
                src_item = src_stack.pop()
                dest_stack.append( src_item)
            self.is_change=True
            self.steps_number+=1

    
    def set_timer(self):
        if self.time_left > 0 and not self.win:
             self.time_left -= 1
        pass     

    def draw_screen(self):

        self.screen.fill(PALETTE["white"])
        self.screen.blit(self.image,(0,0))
        self.tube_rects =  self.draw_tubes()
        pg.draw.rect(self.screen,"white",RECT_CONTAINER,2,10)

        self.win = self.algo.check_victory()
       
        if self.win:
            victory_text = self.font.render('You Won! Press Enter for a new board!', True, 'white')
            self.screen.blit(victory_text, ((WIDTH-150)//3, HEIGHT*0.96))
        
        timer_text = self.font.render(f'Time {self.time_left}', True, "red" if self.time_left < 10 else "white")
        text_rect = timer_text.get_rect(center=TIMER_POS)
        
        self.screen.blit(timer_text, text_rect)
        self.score_lable.draw_rectLabel(self.screen,True,False)
        self.step_lable.draw_rectLabel(self.screen,True,False,self.steps_number)
        self.draw_Button()
        if self.auto_solve:
            self.getNextStep()
        pg.display.update()
        self.clock.tick(REFRASH)

        
    def calculate_ntpr(self,tubes_number):
        if MIN_NTPR <= tubes_number <= MAX_NTPR:
            NTPR = tubes_number
        elif tubes_number > MAX_NTPR:
            # Find the maximum NTPR that is less than or equal to MAX_NTPR and is a divisor of tubes_number
            for i in range(MAX_NTPR, MIN_NTPR-1, -1):
                if tubes_number % i == 0:
                    NTPR = i
                    break
            else:
                # If no exact divisor is found, fall back to max between MIN_NTPR and MAX_NTPR
                NTPR = min(max(MIN_NTPR, tubes_number // ((tubes_number // MAX_NTPR) + 1)), MAX_NTPR)
        else:
            NTPR = MIN_NTPR
    
        return NTPR
    
    def draw_Button(self):
        self.back_button.draw_button(self.screen,True)
        self.auto_solve_Button.draw_button(self.screen,True)
        self.next_step_Button.draw_button(self.screen,True)
        self.prev_step_Button.draw_button(self.screen,True)
         
    def draw_tubes(self):
        
        tube_cols= self.algo.df["init"]
        tube_boxes = []
        full= self.algo.df["full"]
        tubes_number=self.algo.df["tubesNumber"]
        
        NTPR =  self.calculate_ntpr(tubes_number)
         
        c_row = (tubes_number + NTPR - 1) // NTPR  # Number of rows needed
        height_tube = ((CONTAINER_HEIGHT * 0.9) / c_row) * 0.95
        ball_size = (height_tube//full)*0.9
        width_tube = ball_size*1.15
        spacing = (height_tube//full)*0.08
        
        # Calculate the vertical and horizontal spacing
        vertical_spacing = (CONTAINER_HEIGHT - (height_tube * c_row)) / (c_row + 1)
        horizontal_spacing = (CONTAINER_WIDTH - (width_tube * NTPR)) / (NTPR + 1)

        for i in range(tubes_number):
            row = i // NTPR
            col = i % NTPR

            x = CONTAINER_X + horizontal_spacing * (col + 1) + width_tube * col
            y = CONTAINER_Y + vertical_spacing * (row + 1) + height_tube * row

            color = 'green' if self.select_box == i else 'white'
            box = pg.draw.rect(self.screen, color, [x, y, width_tube, height_tube], 2, 100, 0, 0)
            tube_boxes.append(box)

            # Draw balls in the test tube
            for j in range(len(tube_cols[i])):
                ball_x = x + (width_tube - ball_size) // 2  # Center ball in the test tube
                ball_y = (y + height_tube - ((ball_size+spacing) * (j + 1)))  
                # print(tube_cols[i][j])
                pg.draw.rect(self.screen, COLOR_CHOICES[tube_cols[i][j]], [ball_x, ball_y, ball_size, ball_size], 0, 100)

     
        return tube_boxes
     

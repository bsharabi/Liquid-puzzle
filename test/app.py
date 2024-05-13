# import critical modules - random for board generation, copy for being able to restart, pygame for framework
import copy
import random
import pygame

# initialize pygame
pygame.init()

# initialize game variables
WIDTH = 700
HEIGHT = 350
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('Liquid puzzle')
font = pygame.font.Font('freesansbold.ttf', 24)
fps = 60
timer = pygame.time.Clock()
color_choices = ['red', 'blue', 'green','yellow', 'orange', 'light blue', 'dark blue', 'dark green', 'pink', 'purple', 'dark gray',
                 'brown', 'light green']
tube_colors = []
initial_colors = []
# 10 - 14 tubes, always start with two empty
tubes = 10
new_game = True
selected = False
tube_rects = []
select_rect = 100
win = False
# Function to draw text on the screen
def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect()
    text_rect.center = (x, y)
    surface.blit(text_obj, text_rect)

# Function to draw a button
def draw_button(text, font, color, bg_color, surface, x, y, width, height):
    pygame.draw.rect(surface, bg_color, (x, y, width, height))
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(x + width / 2, y + height / 2))
    surface.blit(text_surface, text_rect)


# select a number of tubes and pick random colors upon new game setup
def generate_start(empty_tube:int=1):
    tubes_number = random.randint(2, 8)
    tubes_colors = []
    available_colors = []
    for i in range(tubes_number):
        tubes_colors.append([])
        if i < tubes_number - empty_tube:
            for j in range(4):
                available_colors.append(i)
    for i in range(tubes_number - empty_tube):
        for j in range(4):
            color = random.choice(available_colors)
            tubes_colors[i].append(color)
            available_colors.remove(color)
    print(tubes_colors)
    print(tubes_number)
    return tubes_number, tubes_colors


# draw all tubes and colors on screen, as well as indicating what tube was selected
def draw_tubes(tubes_num, tube_cols):
    tube_boxes = []
 
    spacing = WIDTH / tubes_num
    for i in range(tubes_num):
        for j in range(len(tube_cols[i])):
            pygame.draw.rect(screen, color_choices[tube_cols[i][j]], [5 + spacing * i, 200 - (50 * j), 65, 48], 0, 3)
        box = pygame.draw.rect(screen, 'black', [5 + spacing * i, 50, 65, 200], 5, 5)
        if select_rect == i:
            pygame.draw.rect(screen, 'green', [5 + spacing * i, 50, 65, 200], 3, 5)
        tube_boxes.append(box)
 
    return tube_boxes


# determine the top color of the selected tube and destination tube,
# as well as how long a chain of that color to move
def calc_move(colors, selected_rect, destination):
    chain = True
    color_on_top = 100
    length = 1
    color_to_move = 100
    if len(colors[selected_rect]) > 0:
        color_to_move = colors[selected_rect][-1]
    if 4 > len(colors[destination]):
        if len(colors[destination]) == 0:
            color_on_top = color_to_move
        else:
            color_on_top = colors[destination][-1]
    if color_on_top == color_to_move:
        for i in range(length):
            if len(colors[destination]) < 4:
                if len(colors[selected_rect]) > 0:
                    colors[destination].append(color_on_top)
                    colors[selected_rect].pop(-1)
    print(colors, length)
    return colors


# check if every tube with colors is 4 long and all the same color. That's how we win
def check_victory(colors):
    won = True
    for i in range(len(colors)):
        if len(colors[i]) > 0:
            if len(colors[i]) != 4:
                won = False
            else:
                main_color = colors[i][-1]
                for j in range(len(colors[i])):
                    if colors[i][j] != main_color:
                        won = False
    return won


# main game loop
run = True

while run:
    
    screen.fill('white')
    timer.tick(fps)
    restart_button_width = 150
    restart_button_height = 50
    restart_button_x = 50
    restart_button_y = HEIGHT - 70
    draw_button("Restart", font, (0, 0, 0), (200, 200, 200), screen, restart_button_x, restart_button_y, restart_button_width, restart_button_height)

    # Draw the Shuffle button
    shuffle_button_width = 150
    shuffle_button_height = 50
    shuffle_button_x = WIDTH - 200
    shuffle_button_y = HEIGHT - 70
    draw_button("Shuffle", font, (0, 0, 0), (200, 200, 200), screen, shuffle_button_x, shuffle_button_y, shuffle_button_width, shuffle_button_height)
    # generate game board on new game, make a copy of the colors in case of restart
    if new_game:
        tubes, tube_colors = generate_start()
        # tubes, tube_colors = 5,[[4,1,3,1],[1,4,3,4],[2,2,4,3],[1,2,3,2],[]]
        initial_colors = copy.deepcopy(tube_colors)
        new_game = False
    # draw tubes every cycle
    else:
        tube_rects = draw_tubes(tubes, tube_colors)
    # check for victory every cycle
    win = check_victory(tube_colors)
    # event handling - Quit button exits, clicks select tubes, enter and space for restart and new board
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if restart_button_x <= mouse_pos[0] <= restart_button_x + restart_button_width and restart_button_y <= mouse_pos[1] <= restart_button_y + restart_button_height:
                tube_colors = copy.deepcopy(initial_colors)
                pass
            if shuffle_button_x <= mouse_pos[0] <= shuffle_button_x + shuffle_button_width and shuffle_button_y <= mouse_pos[1] <= shuffle_button_y + shuffle_button_height:
                new_game = True
                pass
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                tube_colors = copy.deepcopy(initial_colors)
            elif event.key == pygame.K_RETURN:
                new_game = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            if not selected:
                for item in range(len(tube_rects)):
                    if tube_rects[item].collidepoint(event.pos):
                        selected = True
                        select_rect = item
            else:
                for item in range(len(tube_rects)):
                    if tube_rects[item].collidepoint(event.pos):
                        dest_rect = item
                        tube_colors = calc_move(tube_colors, select_rect, dest_rect)
                        selected = False
                        select_rect = 100
    # draw 'victory' text when winning in middle, always show restart and new board text at top
    if win:
        victory_text = font.render('You Won! Press Enter for a new board!', True, 'black')
        screen.blit(victory_text, (30, 265))
    restart_text = font.render('Stuck? Space-Restart, Enter-New Board!', True, 'black')
    screen.blit(restart_text, (10, 10))

    # display all drawn items on screen, exit pygame if run == False
    pygame.display.flip()
pygame.quit()
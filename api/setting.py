WIDTH, HEIGHT = (1024, 768)
REFRASH = 60

CONTAINER_HEIGHT = HEIGHT*0.80
CONTAINER_WIDTH = WIDTH*0.9
CONTAINER_X=WIDTH*0.05
CONTAINER_Y=HEIGHT*0.08


MARGIN_CONTAINER=(WIDTH*0.05,HEIGHT*0.08,WIDTH*0.05,HEIGHT*0.12)
RECT_CONTAINER = (CONTAINER_X,CONTAINER_Y,CONTAINER_WIDTH,CONTAINER_HEIGHT)

MIN_NTPR = 2
MAX_NTPR = 25

BUTTON_WIDTH,BUTTON_HEIGHT=BUTTON_SIZE=(150,50)

TIMER_X,TIMER_Y = TIMER_POS=(WIDTH//2, HEIGHT*0.05)

AUTO_BUTTON_X, AUTO_BUTTON_Y = AUTO_BUTTON_POS = ((WIDTH-BUTTON_WIDTH)*0.1, (HEIGHT-BUTTON_HEIGHT)*0.95)

NEXT_BUTTON_X, NEXT_BUTTON_Y =NEXT_BUTTON_POS= ((WIDTH-BUTTON_WIDTH)*0.9, (HEIGHT-BUTTON_HEIGHT)*0.95)

PREV_BUTTON_X, PREV_BUTTON_Y = PREV_BUTTON_POS = ((WIDTH-(BUTTON_WIDTH*2.1))*0.9, (HEIGHT-BUTTON_HEIGHT)*0.95)

BACK_BUTTON_X, BACK_BUTTON_Y = BACK_BUTTON_POS =  ((WIDTH-BUTTON_WIDTH)*0.06, (HEIGHT-BUTTON_HEIGHT)*0.01)

SCORE_WIDTH,SCORE_HEIGHT = SCORE_SIZE=(150,50)
SCORE_X,SCORE_Y = SCORE_POS = ((WIDTH-BUTTON_WIDTH)*0.94, (HEIGHT-BUTTON_HEIGHT)*0.01)

STEPS_WIDTH,STEPS_HEIGHT = STEPS_SIZE=(150,50)
STEPS_X,SCORE_Y = STEPS_POS = ((WIDTH-BUTTON_WIDTH*2)*0.94, (HEIGHT-BUTTON_HEIGHT)*0.01)


# COLOR_CHOICES = ['red', 'blue', 'green','yellow', 'orange', 'light blue', 'dark blue','pink', 'dark green',  'purple', 'dark gray',
#                  'brown', 'light green']
COLOR_CHOICES=['oldlace', 'purple',  'indianred', 'chocolate', 'peachpuff', 'aqua', 'red', 'blue', 'green','yellow', 'orange', 'light blue', 'dark blue','pink', 'dark green',  'purple', 'dark gray','brown', 'light green','dark blue','brown','cyan', 'dark green', 'slategray', 'darkred', 'turquoise', 'darkslategray', 'navy', 'darkcyan', 
 'aliceblue','antiquewhite','midnightblue', 'darkgoldenrod', 'lightskyblue', 'fuchsia', 'dark_goldenrod', 'powderblue', 'sienna', 'gray', 'plum',
 'forestgreen', 'medium_violet_red', 'darkgreen', 'gold', 'palevioletred', 'seagreen', 'lime', 'mediumspringgreen', 
 'cadetblue', 'dark_gray' 'beige', 'mediumturquoise', 'sandy_brown', 'light_yellow', 'firebrick', 'lightslategray', 'khaki',
 'magenta', 'medium_sea_green', 'papayawhip', 'lavender', 'darkviolet', 'yellowgreen', 'dark_salmon', 'paleturquoise',
 'dark_cyan', 'indigo', 'wheat', 'powder_blue', 'bisque', 'dark_blue', 'darkmagenta', 'orange', 'darkorange', 'salmon',
 'darkorchid', 'lightgoldenrodyellow', 'seashell', 'dark_orange', 'lawn_green',  'spring_green', 'light_goldenrod_yellow', 'lightyellow',
 'light_salmon', 'light_cyan', 'orchid', 'blueviolet', 'forest_green', 'darkturquoise', 'cornflowerblue', 'pale_goldenrod', 
 'cadet_blue', 'mediumorchid', 'darkgray', 'orangered', 'blanchedalmond', 'crimson', 'mintcream', 'peru', 'royalblue','burlywood', 'mediumblue', 'linen', 'green', 'mediumseagreen', 'navajowhite',
 'dark_khaki', 'mediumaquamarine', 'papaya_whip', 'mistyrose', 'medium_spring_green', 'deep_pink', 'greenyellow', 'lavenderblush', 
 'lightcoral', 'ghostwhite', 'lightgray', 'white', 'thistle', 'springgreen', 'light green', 'light_blue', 'lightseagreen',  'lemonchiffon', 'royal_blue', 'blue', 'chartreuse', 'pink', 'lightpink', 'light blue', 
 'palegoldenrod', 'hot_pink', 'azure', 'rosybrown', 'tomato', 'honeydew', 'rosy_brown', 'red', 'sandybrown', 'maroon', 'lightcyan',
 'lightsalmon', 'deeppink', 'dark_red', 'mediumpurple', 'goldenrod', 'darkblue', 'olivedrab', 'dark gray', 'mediumvioletred', 'slateblue',
 'saddle_brown', 'medium_orchid', 'whitesmoke', 'teal', 'violet', 'sea_green', 'tan', 'palegreen', 'aquamarine', 'pale_turquoise', 
 'dimgray', 'steelblue', 'lightblue', 'sky_blue', 'lawngreen', 'lemon_chiffon', 'mediumslateblue', 'lightsteelblue', 'dark_green',
 'gainsboro', 'darkkhaki', 'light_pink', 'deepskyblue', 'skyblue', 'darksalmon', 'hotpink', 'black', 'pale_green', 'dodgerblue', 
 'light_green', 'medium_purple', 'light_gray', 'olive', 'yellow', 'lightgreen', 'cornsilk', 'floralwhite', 'limegreen', 'snow', 
 'indian_red', 'darkslateblue', 'moccasin', 'steel_blue', 'dark_orchid', 'blanched_almond']
# color_names = [
#     "black", "white", "red", "green", "blue", "yellow", "cyan", "magenta", 
#     "orange", "purple", "pink", "brown", "gray", "light_gray", "dark_gray", 
#     "olive", "lime", "teal", "navy", "maroon", "silver", "gold", "indigo", 
#     "violet", "turquoise", "aquamarine", "sky_blue", "royal_blue", "light_blue", 
#     "steel_blue", "dark_blue", "medium_blue", "cadet_blue", "powder_blue", 
#     "pale_turquoise", "dark_cyan", "light_cyan", "medium_cyan", "dark_green", 
#     "forest_green", "sea_green", "medium_sea_green", "dark_sea_green", "light_green", 
#     "pale_green", "spring_green", "medium_spring_green", "lawn_green", "chartreuse", 
#     "light_yellow", "lemon_chiffon", "light_goldenrod_yellow", "papaya_whip", 
#     "moccasin", "peach_puff", "pale_goldenrod", "khaki", "dark_khaki", "cornsilk", 
#     "blanched_almond", "bisque", "navajo_white", "wheat", "burlywood", "tan", 
#     "rosy_brown", "sandy_brown", "goldenrod", "dark_goldenrod", "peru", "chocolate", 
#     "saddle_brown", "sienna", "brown", "maroon", "dark_red", "firebrick", "indian_red", 
#     "light_coral", "salmon", "dark_salmon", "light_salmon", "orange_red", "tomato", 
#     "dark_orange", "coral", "dark_orchid", "medium_orchid", "orchid", "violet", "plum", 
#     "thistle", "lavender", "medium_purple", "medium_violet_red", "crimson", "deep_pink", 
#     "hot_pink", "light_pink"
# ]
# pygame_colors = [
#     "aliceblue", "antiquewhite", "aqua", "aquamarine", "azure", "beige", "bisque",
#     "black", "blanchedalmond", "blue", "blueviolet", "brown", "burlywood", "cadetblue",
#     "chartreuse", "chocolate", "coral", "cornflowerblue", "cornsilk", "crimson", "cyan",
#     "darkblue", "darkcyan", "darkgoldenrod", "darkgray", "darkgreen", "darkkhaki",
#     "darkmagenta", "darkolivegreen", "darkorange", "darkorchid", "darkred", "darksalmon",
#     "darkseagreen", "darkslateblue", "darkslategray", "darkturquoise", "darkviolet",
#     "deeppink", "deepskyblue", "dimgray", "dodgerblue", "firebrick", "floralwhite",
#     "forestgreen", "fuchsia", "gainsboro", "ghostwhite", "gold", "goldenrod", "gray",
#     "green", "greenyellow", "honeydew", "hotpink", "indianred", "indigo", "ivory",
#     "khaki", "lavender", "lavenderblush", "lawngreen", "lemonchiffon", "lightblue",
#     "lightcoral", "lightcyan", "lightgoldenrodyellow", "lightgray", "lightgreen",
#     "lightpink", "lightsalmon", "lightseagreen", "lightskyblue", "lightslategray",
#     "lightsteelblue", "lightyellow", "lime", "limegreen", "linen", "magenta", "maroon",
#     "mediumaquamarine", "mediumblue", "mediumorchid", "mediumpurple", "mediumseagreen",
#     "mediumslateblue", "mediumspringgreen", "mediumturquoise", "mediumvioletred",
#     "midnightblue", "mintcream", "mistyrose", "moccasin", "navajowhite", "navy",
#     "oldlace", "olive", "olivedrab", "orange", "orangered", "orchid", "palegoldenrod",
#     "palegreen", "paleturquoise", "palevioletred", "papayawhip", "peachpuff", "peru",
#     "pink", "plum", "powderblue", "purple", "red", "rosybrown", "royalblue", "saddlebrown",
#     "salmon", "sandybrown", "seagreen", "seashell", "sienna", "silver", "skyblue",
#     "slateblue", "slategray", "snow", "springgreen", "steelblue", "tan", "teal",
#     "thistle", "tomato", "turquoise", "violet", "wheat", "white", "whitesmoke",
#     "yellow", "yellowgreen"
# ]
PALETTE = {
            "gray": (192, 192, 192),
            "white": (255, 255, 255),
            "light-green": (64, 213, 47),
            "green": (175, 237, 169),
            "red": (255, 0, 0),
            "purple": (70, 50, 111),
            "light-red": (252, 87, 87),
            "black": (0, 0, 0)
        }





WIDTH, HEIGHT = (1024, 768)
REFRASH = 60

CONTAINER_HEIGHT = HEIGHT*0.80
CONTAINER_WIDTH = WIDTH*0.9
CONTAINER_X=WIDTH*0.05
CONTAINER_Y=HEIGHT*0.08


MARGIN_CONTAINER=(WIDTH*0.05,HEIGHT*0.08,WIDTH*0.05,HEIGHT*0.12)
RECT_CONTAINER = (CONTAINER_X,CONTAINER_Y,CONTAINER_WIDTH,CONTAINER_HEIGHT)

NTPR = 6
""" Number tube per row on screen"""
SPT = WIDTH / NTPR

COLOR_CHOICES = ['red', 'blue', 'green','yellow', 'orange', 'light blue', 'dark blue','pink', 'dark green',  'purple', 'dark gray',
                 'brown', 'light green']
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




FIELD_WIDTH, FIELD_HEIGHT = (590, 175)
MSG_WIDTH, MSG_HEIGHT = (590, 355)
CLIENT_LIST_WIDTH, CLIENT_LIST_HEIGHT = (180, 540)
FILE_LIST_WIDTH, FILE_LIST_HEIGHT = (180, 540)

SEND_BUTTON_WIDTH, SEND_BUTTON_HEIGHT = (70, 30)
LOADING_BAR_WIDTH, LOADING_BAR_HEIGHT = (500, 30)
GET_FILE_BUTTON_WIDTH, GET_FILE_BUTTON_HEIGHT = (100, 30)
STOP_BUTTON_WIDTH, STOP_BUTTON_HEIGHT = (70, 30)

BACK_BUTTON_WIDTH, BACK_BUTTON_HEIGHT = (150, 30)


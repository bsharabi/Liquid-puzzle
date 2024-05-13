from api.lib import *   
     
class Label:
    
    def __init__(self, text_field: str = '', text_font: font = None) -> None:
        self.text = text_field
        self.font = text_font
        self.active = True

    def draw_label(self, surface: Surface, pos: tuple[float, float], color: Color = Color(70, 50, 111), center_text: bool = False) -> None:
        if self.active:
            if center_text:
                title_srf = self.font.render(
                    self.text, True, color)
                title_rect = title_srf.get_rect(center=pos)
                surface.blit(title_srf, title_rect)
            else:
                surface.blit(self.font.render(self.text, True, color), pos)   

class Rectangle:

    def __init__(self, position: tuple[int, int], size_box: tuple[int, int]) -> None:
        self.rect: Rect = Rect(position, size_box)
        self.position = position

    '''Checks if the mouse is in the field '''

    def has_mouse(self):
        mouse_pos = pg.mouse.get_pos()
        return self.rect.collidepoint(mouse_pos)

    def gradientRect(self, window, left_colour, right_colour, target_rect):
        """ Draw a horizontal-gradient filled rectangle covering <target_rect> """
        colour_rect = pg.Surface(
            (2, 2))                              
        pg.draw.line(colour_rect, left_colour,  (0, 0),
                     (0, 1))            
        pg.draw.line(colour_rect, right_colour, (1, 0),
                     (1, 1))           
        colour_rect = pg.transform.smoothscale(
            colour_rect, (target_rect.width, target_rect.height))  # stretch!
        # paint it
        window.blit(colour_rect, target_rect)

    '''Draws the rectangle on Surface'''

    def draw_rect(self, surface: Surface, color: Color) -> None:
        pg.draw.rect(surface, color, self.rect, border_radius=4)


class RectLabel:
    def __init__(self, rect_label: Rectangle, lable: Label, color: Color = (204, 204, 204), text_color: Color = (0, 0, 0)) -> None:
        self.color = color
        self.label = lable
        self.rect = rect_label
        self.text_color = text_color

    def draw_rectLabel(self, surface):
        self.rect.draw_rect(surface, self.color)
        self.rect.rect.topleft = self.rect.position
        self.label.draw_label(
            surface, self.rect.rect.topleft, self.text_color, False)
        pass


class Button:

    def __init__(self, rect_button: Rectangle, text_button: Label, hover_color: Color = (0, 0, 255), text_color: Color = (0, 255, 0), rect_color: Color = (255, 0, 0,0)):
        self.rect_button = rect_button
        self.text_button = text_button
        self.hover_color = hover_color
        self.text_color = text_color
        self.rect_color = rect_color
        self.active = False

    '''Check if the mouse hovers over the Rectangle Button'''

    def mouse_hover(self) -> bool:
        mouse_pos = pg.mouse.get_pos()
        return self.rect_button.rect.collidepoint(mouse_pos)

    '''Check if the mouse cliked on the Rectangle Button'''

    '''Draws the rectangle button on the Surface'''

    def draw_button(self, surface, center: bool = False):
        button_color = self.rect_color
        if self.mouse_hover():
            button_color = self.hover_color
        if self.active:
            button_color = (146, 181, 233)
        self.color_now = button_color
        self.rect_button.draw_rect(surface, button_color)
        self.rect_button.rect.topleft = self.rect_button.position
        self.text_button.draw_label(
            surface, self.rect_button.rect.center, self.text_color, center)

class RectangleList:

    def __init__(self, rect_list_Button: list[Button], rect: Rectangle) -> None:
        self.rectListButton = rect_list_Button
        self.rect = rect
        self.y = 0
        self.p = 10

    def scroll(self, y):
        self.y += y

    def has_mouse(self):
        return self.rect.has_mouse()

    def draw_scerrn(self, surf: Surface):
        self.rect.draw_rect(surf, (255, 255, 255))
        for client in self.rectListButton:
            client.draw_button(surf, True)
            self.p += 55
            pass
        
class SeekBar:
    def __init__(self, panel, initial_value, color):
        self.panel = panel
        self.value = initial_value
        self.color = color

    def draw_seekbar(self, screen):
        # Draw seek bar background
        pg.draw.rect(screen, (200, 200, 200), self.panel.rect)

        # Calculate position of the slider based on current value
        slider_x = self.panel.rect.left + int(self.value * self.panel.rect.width)

        # Draw slider
        slider_width = 10
        slider_height = self.panel.rect.height
        slider_rect = pg.Rect(slider_x - slider_width // 2, self.panel.rect.top, slider_width, slider_height)
        pg.draw.rect(screen, self.color, slider_rect)


    def handle_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            if self.panel.rect.collidepoint(event.pos):
                # Calculate new value based on mouse position
                relative_pos = event.pos[0] - self.panel.rect.left
                self.value = max(0.0, min(1.0, relative_pos / self.panel.rect.width))
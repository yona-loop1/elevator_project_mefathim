from CONFIG import *

class Floor:

    def __init__(self, i):
        """
        creating variables that needed to drawing the elevators as detailed below
        accepts i to counting the numbers of the elevators
        return None
        """
        self.num_floor = i
        # shape and position (in axis y) of the floors
        self.shape_floor = pygame.image.load(BUILDING_BACKGROUND)
        self.shape_floor = pygame.transform.scale(self.shape_floor, (FLOOR_WIDTH, FLOOR_HEIGHT))
        self.y = SCREEN_HEIGHT - ((self.num_floor+1) * FLOOR_HEIGHT)
        # shape and color of the button and floor's numbers
        self.shape_button = pygame.Rect(BUTTON_POSITION_X , self.y + BUTTON_POSITION_Y, BUTTON_WIDTH, BUTTON_HEIGHT)
        self.font_button = pygame.font.Font(TEXT_FONT, SIZE_TEXT_BUTTON)
        self.text_button = self.font_button.render(str(self.num_floor), True, BUTTONS_TEXT_COLOR, None)
        self.text_react_button = self.text_button.get_rect()
        self.text_react_button.center = (TEXT_BUTTON_POSITION_X, self.y + TEXT_BUTTON_POSITION_Y)
        self.color = BUTTON_COLOR
        # shape of timer of the elevator arrival
        self.background_timer = pygame.Rect(TIMER_POSITION_X, self.y + TIMER_POSITION_Y, TIMER_WIDTH, TIMER_HEIGHT)
        self.font_timer = pygame.font.Font(TEXT_FONT, SIZE_TEXT_TIMER)
        self.show_timer = 0
        self.show_text_timer = str()

        self.arrivel_time = 0          
        self.start = 0
        

    def draw_full_floor(self, screen):
        """
        draws the floors on the screen
        accepts variable 'screen' created in main file
        return None
        """
        self.draw_floor(screen)
        self.draw_button(screen)
        self.draw_timer(screen)


    def draw_floor(self, screen):
        """
        draws only the floors on the screen
        accepts variable 'screen' created in main file
        return None
        """
        screen.blit(self.shape_floor, (BUILDING_POSITION_WIDTH, self.y))
        if self.num_floor != NUMBER_FLOORS - 1:
            pygame.draw.line(screen, LINE_COLOR, (BUILDING_POSITION_WIDTH, self.y + LINE_POSITION), (BUILDING_POSITION_WIDTH + FLOOR_WIDTH-1 ,self.y + LINE_POSITION) ,LINE_SPACE)
        else:
            pygame.draw.line(screen, SCREEN_BACKGROUND, (BUILDING_POSITION_WIDTH, self.y + LINE_POSITION), (BUILDING_POSITION_WIDTH + FLOOR_WIDTH-1 ,self.y + LINE_POSITION) ,LINE_SPACE)
        

    def draw_button(self, screen):
        """
        draws only the buttons on the screen
        accepts variable 'screen' created in main file
        return None
        """
        pygame.draw.rect(screen, (self.color), self.shape_button, 0, 4)
        screen.blit(self.text_button, self.text_react_button)


    def draw_timer(self, screen):
        """
        draws only the timers on the screen
        accepts variable 'screen' created in main file
        return None
        """
        if self.show_timer: # this condition is because i don't want show timer only if the floor orders a elevator
            pygame.draw.rect(screen, TIMER_COLOR, self.background_timer, 1, 5)
            self.shape_text_timer()
            text = self.font_timer.render(self.show_text_timer, True, TIMER_COLOR, None)
            text_react = text.get_rect()
            text_react.center = (TEXT_TIMER_POSITION_X, self.y + TEXT_TIMER_POSITION_Y)
            screen.blit(text, text_react)
        

    def elevator_arrive(self, arrivel_time):
        """
        accepts the elevator arrival time to the floor, and update it in the data of the floor
        return None
        """
        self.start = time.time()
        self.arrivel_time, self.show_timer = arrivel_time, arrivel_time
        self.color = GREEN


    def update_floor(self): 
        """
        updates the timer of elevator arrivel because the time changes as time passes by
        accepts None
        return None
        """
        if self.show_timer:
            counting = time.time()
            if self.start + self.arrivel_time > counting:
                self.show_timer = self.start + self.arrivel_time - counting
            else:
                self.show_timer, self.arrivel_time = 0, 0
                self.color = BUTTON_COLOR


    def shape_text_timer(self): 
        """
        this function improve the shape of the timer for the purpose draw it better on the screen
        accepts None
        return None
        """ 
        text = str(self.show_timer)
        text = text.replace('.', ':')
        zero = '0'
        if text[2] == ':':
            self.show_text_timer = text[:4] + zero
        else:
            self.show_text_timer = zero + text[:3] + zero

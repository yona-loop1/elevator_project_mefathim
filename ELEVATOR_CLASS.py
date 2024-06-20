from FLOOR_CLASS import *

class Elevator:



    def __init__(self, i):
        """
        creating variables that needed to activition of the elevators as detailed below
        accepts i to counting the numbers of the elevators
        return None
        """
        self.num_elv = i
        self.order_array = [] # In this array, all orders made for the elevator are saved, this includes the floor and the time of the travel to it
        # data of the elevator situation
        self.current_floor = 0
        self.previous_floor = 0
        self.mode_elv = 'stoping'
        self.diraction_elv = 0
        self.distance = 0
        self.travel = 0
        # shape (image) and position (in axis x and y) of the elevators
        self.img = pygame.image.load(ELEVATOR_IMAGE)
        self.img = pygame.transform.scale(self.img, (ELEVATOR_W, ELEVATOR_H))
        self.y = SCREEN_HEIGHT- (self.current_floor+1) * FLOOR_HEIGHT + LINE_SPACE
        self.x = BUILDING_POSITION_WIDTH + FLOOR_WIDTH + self.num_elv * ELEVATOR_W
        # when and where will be the elevator available
        self.availability_floor = 0
        self.availability_timer = 0
        self.availability_time = 0
        self.start_available_timer = 0
        # timers to counting the time of travelation
        self.timer = 0
        self.start_timer = 0


    def draw_elevator(self, screen):
        """ 
        draws the elevators
        accepts variable 'screen' created in main file
        return None
        """
        screen.blit(self.img, (self.x, self.y))
        

    def update_elv(self):
        """
        updates the elevators situations 
        accepts None
        return None
        as can see that is axisting three situations for the elevator:
        1. "movement", when the elevator travel to eny floor.
        2. "waiting", when the elevator is coming to the floor.
        3. "stoping", when the elevator finished the travel.
        in any situation, the function calls to other function in accordance to the situation.
        """
        if self.order_array and self.mode_elv == 'stoping':
            self.start_timer = self.order_elv(time.time())
        if self.mode_elv == 'movement':
            self.travelation()
        if self.mode_elv == 'waiting':
            self.waitation()
        self.calculate_availability()


    def order_elv(self, time):
        """
        Commands the elevator to make the next order in line, by extract the order saved in the "order_array"
        accepts function time.time to counting the time passes
        return the time when it was called to itself
        """
        self.previous_floor = self.current_floor
        self.current_floor, self.travel = self.order_array.pop(0)
        self.diraction()
        self.mode_elv = 'movement'
        return time


    def travelation(self): 
        """
        calculation the position for the elevator
        by it, the draw function drawing the elevator on the true position
        accepts None
        return None
        """
        if self.timer < self.travel:
            timer = time.time()
            self.timer = timer - self.start_timer
            self.distance = self.diraction_elv * self.timer
            self.y = SCREEN_HEIGHT - (self.previous_floor+1) * FLOOR_HEIGHT + self.distance + LINE_SPACE
        else:
            self.y = SCREEN_HEIGHT- (self.current_floor+1) * FLOOR_HEIGHT + LINE_SPACE
            pygame.mixer.Sound(ARRIVAL_SOUND).play()
            self.start_timer = time.time()
            self.distance, self.timer = 0, 0
            self.mode_elv = 'waiting'


    def waitation(self): 
        """
        calculation when ends two seconds to waiting in the floor [because the rul is to waiting two secounds in every floor]
        accepts None
        return None
        """
        if self.timer < TIME_STOP_FLOOR:
            timer = time.time()
            self.timer = timer - self.start_timer
        else:
            self.timer = 0
            self.mode_elv = 'stoping'


    def receiving_order(self, floor, arrivel_time, time_travel):
        """
        recived order from the mian function, that it the function "order_elevator" in the BUILDING_CLASS
        accepts floor ordered, when will it availability to next order, the elvator arrival time to the floor wich orders.
        return None
        """
        self.order_array.append((floor, time_travel))
        self.start_available_timer = time.time()
        self.availability_time, self.availability_timer = arrivel_time + TIME_STOP_FLOOR, arrivel_time + TIME_STOP_FLOOR
        self.availability_floor = floor


    def diraction(self): 
        """
        determines if the elevator goes up or down
        accepts None
        return None
        """
        if self.previous_floor > self.current_floor:
            self.diraction_elv = FLOOR_HEIGHT/TIME_PASS_FLOOR
        else:
            self.diraction_elv = -FLOOR_HEIGHT/TIME_PASS_FLOOR


    def calculate_availability(self):
        """
        calculation the availability time, because the time changes as time passes by
        accepts None
        return None
        """
        if self.availability_timer > 0:
            timer = time.time()
            self.availability_timer = self.start_available_timer + self.availability_time - timer
        else:
            self.availability_time = 0


    def availability(self): 
        """
        accepts None
        return the time and the floor when and where will be the elevator available to make another reservation, 
        """
        return self.availability_timer, self.availability_floor

from FLOOR_CLASS import *

class Elevator:

    def __init__(self, i):
        self.num_elv = i
        self.order_array = [] # In this array, all orders made for the elevator are saved, this includes the floor and the time of the travel to it
        # data of the elevator situation
        self.current_floor = 0
        self.previous_floor = 0
        self.mode_elv = 'stoping'
        self.diraction_elv = 0
        self.distance = 0
        self.travel = 0
        # shape and position (in axis x and y) of the elevators
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
        screen.blit(self.img, (self.x, self.y))
        

    def update_elv(self):
        """as can see that is axisting three situations for the elevator:
        1. movement, when the elevator travel to eny floor.
        2. waiting, when the elevator is coming to the floor.
        3. stoping, when the elevator finished the travel."""
        if self.order_array and self.mode_elv == 'stoping':
            self.start_timer = self.order_elv(time.time())
        if self.mode_elv == 'movement':
            self.travelation()
        if self.mode_elv == 'waiting':
            self.waitation()
        self.calculate_availability()


    def order_elv(self, time):
        self.previous_floor = self.current_floor
        self.current_floor, self.travel = self.order_array.pop(0)
        self.diraction()
        self.mode_elv = 'movement'
        return time


    def travelation(self): # calculation the position for the elevator
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


    def waitation(self): # calculation when ends two seconds to waiting in the floor
        if self.timer < TIME_STOP_FLOOR:
            timer = time.time()
            self.timer = timer - self.start_timer
        else:
            self.timer = 0
            self.mode_elv = 'stoping'


    def receiving_order(self, floor, arrivel_time, time_travel):
        self.order_array.append((floor, time_travel))
        self.start_available_timer = time.time()
        self.availability_time, self.availability_timer = arrivel_time + TIME_STOP_FLOOR, arrivel_time + TIME_STOP_FLOOR
        self.availability_floor = floor


    def diraction(self): # if the elevator goes up or down
        if self.previous_floor > self.current_floor:
            self.diraction_elv = FLOOR_HEIGHT/TIME_PASS_FLOOR
        else:
            self.diraction_elv = -FLOOR_HEIGHT/TIME_PASS_FLOOR


    def calculate_availability(self):
        if self.availability_timer > 0:
            timer = time.time()
            self.availability_timer = self.start_available_timer + self.availability_time - timer
        else:
            self.availability_time = 0


    def availability(self): # the goal of the function is to given data the building function ("ordering_elevator") that it calculate who is the first available elevator
        return self.availability_timer, self.availability_floor

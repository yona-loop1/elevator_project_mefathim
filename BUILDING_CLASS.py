from ELEVATOR_CLASS import *

class Building:

    def __init__(self):
        self.floors = [Floor(i) for i in range(NUMBER_FLOORS)]
        self.elevators = [Elevator(i) for i in range(NUMBER_ELEVATORS)]


    def draw_building(self, screen):
        for floor in self.floors:
            floor.draw_full_floor(screen)
        for elevator in self.elevators:
            elevator.draw_elevator(screen)
        

    def ordering_elevator(self, x, y): # calculate which the elevator available first
        if BUTTON_POSITION_X < x < BUTTON_POSITION_X + BUTTON_WIDTH: # this is the position (in axis x) of the elevator order button 
            order_floor = self.button_pressed(y)
            best_time = float('inf')
            object_elevator = None
            travel_time = 0
            order = True
            for e in self.elevators:
                time, floor = e.availability()
                travel = abs(floor - order_floor) * TIME_PASS_FLOOR
                if floor == order_floor: # this condition for cancel the order if there is an elevator on the floor
                    order = False
                if travel + time < best_time:
                    best_time = travel + time
                    travel_time = travel
                    object_elevator = e
            if order:
                object_elevator.receiving_order(order_floor, best_time, travel_time)
                self.floors[order_floor].elevator_arrive(best_time)


    def button_pressed(self, y): # calculate and return which floor ordered the elevator
        return (SCREEN_HEIGHT - y)//FLOOR_HEIGHT


    def update_building(self):
        # i made twice the update of elevators, for punctual in the times 
        for elevator in self.elevators:
            elevator.update_elv()
        for elevator in self.elevators:
            elevator.update_elv()
        for floor in self.floors:
            floor.update_floor()

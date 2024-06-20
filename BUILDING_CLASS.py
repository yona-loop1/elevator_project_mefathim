from ELEVATOR_CLASS import *

class Building:

    def __init__(self):
        """ 
        creating building by create floors and elevators objects 
        """
        self.floors = [Floor(i) for i in range(NUMBER_FLOORS)]
        self.elevators = [Elevator(i) for i in range(NUMBER_ELEVATORS)]


    def draw_building(self, screen):
        """ 
        draws the building by calling to the drew's functions of the floors and elevators
        accepts variable 'screen' created in main file
        return None
        """
        for floor in self.floors:
            floor.draw_full_floor(screen)
        for elevator in self.elevators:
            elevator.draw_elevator(screen)
        

    def order_elevator(self, x, y):
        """ 
        orders a elevator according to the calculate which the elevator available first
        and sends the number floor to the selected elevator plus the travel time
        and sends the travel time that it the elvator arrival time - to the floor. 
        accepts X-axis and Y-axis positions on the game's screen
        return None
        """
        if BUTTON_POSITION_X < x < BUTTON_POSITION_X + BUTTON_WIDTH: # this is the position (in axis x) of the elevator order button 
            order_floor = self.button_pressed(y)
            best_time = float('inf')
            object_elevator = None
            travel_time = 0
            order = True
            for e in self.elevators:
                time, floor = e.availability()
                travel = abs(floor - order_floor) * TIME_PASS_FLOOR
                if floor == order_floor: # this condition is cancels the order if there is an elevator on the floor
                    order = False
                if travel + time < best_time:
                    best_time = travel + time
                    travel_time = travel
                    object_elevator = e
            if order:
                object_elevator.receiving_order(order_floor, best_time, travel_time)
                self.floors[order_floor].elevator_arrive(best_time)


    def button_pressed(self, y):
        """
        accepts Y-axis positions on the game's screen
        return which floor ordered the elevator
        """
        return (SCREEN_HEIGHT - y)//FLOOR_HEIGHT


    def update_building(self):
        """ 
        updates the situations of the elevators and floors
        accepts None
        return None
        """
        for elevator in self.elevators:
            elevator.update_elv()
        for elevator in self.elevators: # i called twice the update_elv to punctual in the times of the elevators arrival
            elevator.update_elv()
        for floor in self.floors:
            floor.update_floor()

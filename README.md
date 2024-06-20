# Elevator Control System

## Overview
This project implements a simple elevator control system using Python. The main functionality is encapsulated within the BUILDING_CLASS.py file, which represents the core logic of managing elevators within a building.
the logic is, that each floor that orders for a elevator, the elevators management order the elevator that is available first for all elevators, that is, because the elevator cno't reseiv thr order only after it finished the previuos order, therefore any elevator avilable in an other time. 

## Features
•	Elevator Management: Controls the movement and operation of elevators within a simulated building environment.
•	Request Handling: Processes requests from different floors to order elevators.
•	Simulation: Simulates elevator behavior and movement based on the provided logic.

## Installation
1.	Clone the repository:
bash
Copy code
git clone https://github.com/yona-loop1/elevator_project_mefathim.git
2.	Navigate to the project directory.

## Tu Use
To use the elevator control system in your own projects, follow these steps:
1.	Import the BUILDING_CLASS module:
python
Copy code
from BUILDING_CLASS import Building (the Building is a class)
2.	Initialize a Building object:
python
Copy code
(variable)building = Building(num_elevators, num_floors)
o	num_elevators: Number of elevators in the building.
o	num_floors: Number of floors the building has.
3.	Interact with the elevators using the following method:
order_elevator (floor): Requests an elevator to a specific floor, chooses the best elevator, sender\updater the number of the floor what performed the order plus the time of the travel of the elevator to him - to the selected elevator, and sender the time of elevator arrival to the floor.
4.	Simulate the elevator system as per your requirements, by two functions:
o	draw_building (screen): draws the image of the floors and the elevators on the screen.
o	update_building: updater the situation of any elevator Relative to the floor that ordered it, and the time of any floor when will a elevator comming to him. [Basically, the draw function draws the building by the updates that the update function given it]
5.	Run the main loop ('while') in the file MAIN here called to the update function, and draw function. and also called to order_elevator function to order any elevator.

## Example
Here's a simple example demonstrating the usage of the elevator control system:
python
Copy code
from BUILDING_CLASS import Building

• Initialize a building with 3 elevators and 10 floors
building = Building(3, 10)

• Request an elevator to floor 5
building.order_elevator(5): chooces elevator 2, sending floor 5 plus sume secounds of travel time 
- to elevator 2, and sending sume secounds of travel time to floor 5.
building.update_building: updating an object elevator number 2 that it travelation to floor 5, and updating an floor 5 with the time ov elevator arraival to him.

## Contributing
Contributions to this project are welcome. If you find any issues or have suggestions for improvements, please feel free to open an issue or a pull request on GitHub.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.

## Contact
For questions or further information, please contact the project maintainer(s):
•	GitHub


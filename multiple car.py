from mesa import Model, Agent
from mesa.time import RandomActivation
from mesa.space import MultiGrid
import random


class Car(Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)

    def step(self):
        """Defines the movement of the car"""
        x, y = self.pos
        new_x = min(x + 1, self.model.grid.width - 1)  
        self.model.grid.move_agent(self, (new_x, y))


class TrafficModel(Model):
    def __init__(self, width, height, num_cars):
        self.grid = MultiGrid(width, height, torus=False)  
        self.schedule = RandomActivation(self)

        
        for i in range(num_cars):
            car = Car(i, self)
            self.schedule.add(car)
            
            
            x, y = 0, random.randint(0, height - 1)
            self.grid.place_agent(car, (x, y))

    def step(self):
        """Advance the simulation by one step."""
        self.schedule.step()


if __name__ == "__main__":
    width, height, num_cars = 10, 5, 3  
    model = TrafficModel(width, height, num_cars)

    for _ in range(10): 
        model.step()

import math
import random
import statistics as st
import matplotlib.pyplot as plt
import numpy as np


class Simulation:
    def __init__(self):
        self.ticks = 0
        self.road = Road()

    # def __str__(self):
    #     return '
    #
    # def __repr__(self):
    #     return self.__str__()


    def tick(self):
        self.road.change_speed()
        self.road.drive()
        self.road.move_location()
        return((sum(self.road.test())/len(self.road.test())), np.array(self.road.graph))


    def sim(self, time = 60):
        data = []
        avg_speed = []
        self.road.add_cars()
        for tick in range(time):
            data.append(self.tick()[1])
            avg_speed.append(self.tick()[0])
            self.ticks += 1
        avg_speed = sum(avg_speed)/len(avg_speed)
        return(np.array(data), avg_speed)



class Car:
    def __init__(self, speed = 0, max_speed = 15, location = 0):
        self.max_speed = max_speed
        self.speed = speed
        self.location = location


    def car(self):
        self.location += self.speed
        if self.location > 1000:
            self.location = self.location % 1000
        return self.location



class Road:
    def __init__(self):
        self.cars = [Car() for x in range(30)]
        self.graph = np.array([0 for _ in range(1100)]) #


    def drive(self):
        return [car.car() for car in self.cars]


    def test(self):
        return [car.speed for car in self.cars]


    def add_cars(self):
        x = 0
        for car in self.cars:
            car.location = x
            x += 33


    def move_location(self):
        self.graph = np.array([0 for _ in range(1100)]) #
        for car in self.cars:
            for x in range(5):
                self.graph[car.location+x] = 1


    def change_speed(self):
        for car in self.cars:
            distance = []
            for x in self.graph[(car.location+5):(car.location+5)+car.speed]:
                distance.append(x)
            if random.random() < .1:
                car.speed -= 2
            elif sum(distance) == 0 and car.speed >= car.max_speed:
                car.speed == car.max_speed
            elif sum(distance) == 0 and car.speed <= car.max_speed:
                car.speed += 2
            elif sum(distance) > 5:
                if car.speed > 0:
                    car.speed = 0

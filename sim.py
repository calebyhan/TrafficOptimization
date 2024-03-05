import random
import numpy as np


class Sim:
    """
        0: 2 lanes straight (a, b)
        1: 2 lanes left, 2 lanes right (a, b)
        2: 1 lane all (a, b, c, d)
    """

    POSSIBLE_ACTIONS = ["0a", "0b", "1a", "1b", "2a", "2b", "2c", "2d"]

    def __init__(self, t):
        self.roads = []
        self.action = None
        self.t = t

    def fill_roads(self):
        for i in range(4):
            self.roads.append(Road(self.t))


class Road:
    def __init__(self, t):
        self.cars = []
        self.t = t
        self.x = self.create_events()

    @staticmethod
    def create_events():
        x = np.linspace(0, 200, 1000)

        frequency = 0.1
        amplitude = 1
        sin_wave = amplitude * np.sin(2 * np.pi * frequency * x)

        noise_amplitude = random.random()
        noise = noise_amplitude * np.random.randn(len(x))
        noisy_sin_wave = sin_wave + noise

        return noisy_sin_wave

    def run(self):
        if random.random() < self.x[self.t]:
            self.add_car()

        for car in self.cars:
            car.move()

    def add_car(self):
        self.cars.append(Car())


class Car:
    MAX_ACCELERATION = 1
    MAX_SPEED = 2

    def __init__(self):
        self.speed = 0
        self.acceleration = 0
        self.position = 0
        self.idle = False
        self.road = None

    def move(self):
        pass

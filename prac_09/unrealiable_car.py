from car import Car
import random

class UnreliableCar(Car):
    """An unreliable car that only drives based on its reliability."""
    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        if random.uniform(0, 100) < self.reliability:
            return super().drive(distance)
        return 0



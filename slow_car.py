from base_car import BaseCar


class SlowCar(BaseCar):
    """
    A class used to represent the slow car
    """
    def __init__(self):
        super().__init__()
        self.max_speed *= 0.75
        self.acceleration *= 0.75
        self.brake_efficiency *= 2

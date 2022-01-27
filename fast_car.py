from base_car import BaseCar


class FastCar(BaseCar):
    """
    A class used to represent the fast car
    """
    def __init__(self):
        super().__init__()
        self.max_speed *= 3
        self.max_acceleration *= 2
        self.brake_efficiency *= 1

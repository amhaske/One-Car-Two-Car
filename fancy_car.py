from base_car import BaseCar


class FancyCar(BaseCar):
    """
    A class used to represent the fancy car

    Methods
    -------
    horn()
        honks a beep beep horn
    gear(gear)
        Changes the gear of the car
    """

    def __init__(self):
        super().__init__()
        self.max_speed *= 2
        self.max_acceleration *= 1
        self.brake_efficiency *= 1

    def horn(self):
        """Honks the car horn.
        """
        if self.engine:
            print("beep beep")
        else:
            print("engine is off can't beep")

    def gear(self, gear):
        """Drives the car in its current direction.

        Parameters
        ----------
        gear : string
            The gear state the car must switch to

        Raises
        ------
        NotImplementedError
            If no gear value is passed in as a parameter.
        """
        if not(isinstance(gear, str)):
            raise TypeError("Please give the gear as a string value: ex reverse")

        if gear is None:
            raise NotImplementedError("Please provide a gear value to move to")

        if gear == "reverse":
            if self.current_speed == 0:
                self.direction = "reverse"
                self.current_gear = "reverse"
            else:
                return "Cannot change the gear as speed is greater than zero."

        elif gear == "drive":
            if self.current_speed == 0:
                self.direction = "forward"
                self.current_gear = "drive"
            else:
                return "Cannot change the gear as speed is greater than zero."

        else:
            "Cannot change the gear to {}".format(gear)

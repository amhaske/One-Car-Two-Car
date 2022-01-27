class BaseCar:
    """
    A class used to represent the average car

    ...

    Attributes
    ----------
    engine : bool
        the state of the engine
    headlights : bool
        the state of the headlights
    current_gear : str
        the gear in which the car is currently  in
    direction : str
        the direction in which the car is moving
    trip_distance : int
        the total trip distance the car has covered
    distance_from_home : int
        the relative distance the car has covered from home
    max_speed : int
        the maximum speed the car can travel in
    max_acceleration : int
        the custom acceleration speed for each car
    brake_efficiency : int
        the braking efficiency of each car
    current_speed : int
        the current speed of the car
    acceleration : int
        the acceleration of the car

    Methods
    -------
    on()
        Starts the engine of the car
    off()
        Stops the engine of the car
    gas(time)
        adds gas to the engine, accelerates the car
    drive(time)
        drives the car in a direction
    brake(time)
        slows down the vehicle
    lights(time)
        turns the headlights on or off
    stats(time)
        prints the dashboard statistics of the car
    """

    def __init__(self):

        self.engine = False
        self.headlights = False
        self.current_gear = "park"
        self.direction = "forward"

        self.trip_distance = 0
        self.distance_from_home = 0

        self.max_speed = 50
        self.max_acceleration = 5
        self.brake_efficiency = 10

        self.current_speed = 0
        self.acceleration = 0

    def on(self):
        """Turns on the engine of the vehicle.
        """
        self.engine = True
        self.trip_distance = 0
        self.distance_from_home = 0

    def off(self):
        """Turns on the engine of the vehicle.
        """
        if self.current_speed > 0:
            return "Cannot turn the engine off as speed is greater than zero, apply brakes."
        self.engine = False

    def gas(self, time):
        """Adds gas to the engine.

        Parameters
        ----------
        time : int, float
            The time for which the gas is added

        Raises
        ------
        NotImplementedError
            If no time value is passed in as a parameter.
        """
        if not(isinstance(time, (int, float))):
            raise TypeError("Please give the time as an integer or a float value.")

        if time is None:
            raise NotImplementedError("Please provide a time value for how long the gas is filled")

        if self.engine:
            self.acceleration = self.max_acceleration * time
            self.current_speed += self.acceleration
            if self.current_speed > self.max_speed:
                self.current_speed = self.max_speed

    def drive(self, time):
        """Drives the car in its current direction.

        Parameters
        ----------
        time : int, float
            The time for which the car is driven

        Raises
        ------
        NotImplementedError
            If no time value is passed in as a parameter.
        """
        if not(isinstance(time, (int, float))):
            raise TypeError("Please give the time as an integer or a float value.")

        if time is None:
            raise NotImplementedError("Please provide a time value for how long the car is driven")

        if self.engine:

            self.trip_distance += self.current_speed * time

            if self.direction == "forward":
                self.distance_from_home += self.current_speed * time

            elif self.direction == "reverse":
                self.distance_from_home -= self.current_speed * time
                self.distance_from_home = abs(self.distance_from_home)

            if self.current_speed > 0 and self.direction == "forward":
                self.current_gear = "drive"

            self.current_speed = self.current_speed if self.current_speed <= self.max_speed else self.max_speed

    def brake(self, time):
        """Slows down the vehicle.

        Parameters
        ----------
        time : int, float
            The time for which the brake pedal is pressed

        Raises
        ------
        NotImplementedError
            If no time value is passed in as a parameter.
        """
        if not(isinstance(time, (int, float))):
            raise TypeError("Please give the time as an integer or a float value.")

        if time is None:
            raise NotImplementedError("Please provide a time value for how long the brakes are applied")

        if self.engine:
            self.current_speed -= time * self.brake_efficiency
            self.current_speed = max(self.current_speed, 0)

            if self.current_speed == 0:
                self.current_gear = "park"

    def lights(self):
        """Toggles the headlight between on and off
        """

        if self.headlights:
            self.headlights = False
        else:
            self.headlights = True

    def stats(self):
        """Prints the dashboard statistics of the car
        """

        engine = "On" if self.engine else "Off"
        light = "On" if self.headlights else "Off"
        print(
            f"\nengine: {engine}\n"
            f"light: {light}\n"
            f"speed: {self.current_speed} m/s\n"
            f"odometer: {self.trip_distance} m\n"
            f"home: {self.distance_from_home} m\n"
            f"gear: {self.current_gear.title()} \n"
            f"direction: {self.direction.title()}"
        )

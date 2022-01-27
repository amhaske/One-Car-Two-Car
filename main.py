from fast_car import FastCar
from fancy_car import FancyCar
from slow_car import SlowCar

if __name__ == '__main__':
    """Runs the problem statement.
    """
    fast_car = FastCar()
    fancy_car = FancyCar()
    slow_car = SlowCar()

    print("\nEngine started for all the three cars.")
    fast_car.on()
    fancy_car.on()
    slow_car.on()

    print("\nLights turned on for Fancy and Fast cars.")
    fancy_car.lights()
    fast_car.lights()

    print("\nAll three cars gas for 11 seconds.")
    fast_car.gas(11)
    fancy_car.gas(11)
    slow_car.gas(11)

    print("\nAll three cars drive for 30 seconds.")
    fast_car.drive(30)
    fancy_car.drive(30)
    slow_car.drive(30)

    print("\nFancy car stops for 5 seconds.")
    fancy_car.brake(5)
    print("\nFancy car drives for 3 seconds.")
    fancy_car.drive(3)

    print("\nSlow car brakes for 6 seconds.")
    slow_car.brake(6)

    print("\nFancy car comes to a full stop.")
    _time = 1
    while fancy_car.current_speed > 0:
        fancy_car.brake(_time)
        _time += 1

    print("\nFancy car changes to reverse.")
    fancy_car.gear('reverse')
    print("\nFancy car gases for 20 seconds.")
    fancy_car.gas(20)
    print("\nFancy car drives for 30 seconds.")
    fancy_car.drive(30)
    print("\nFancy car turns off their lights.")
    fancy_car.lights()

    print("\nFast car drives for 30 seconds.")
    fast_car.drive(30)
    print("\nFancy car gases for 20 seconds.")
    fast_car.gas(20)
    print("\nFancy car drives for additional 60 seconds.")
    fast_car.drive(60)

    print("\nSlow car comes to a full stop.")
    _time = 1
    while slow_car.current_speed > 0:
        slow_car.brake(_time)
        _time += 1

    print("\nSlow car turns off their engine.")
    slow_car.off()

    print("\nAll three cars check their dashboards.")
    print("\nFancy Car")
    fancy_car.stats()
    print("\nFast Car")
    fast_car.stats()
    print("\nSlow Car")
    slow_car.stats()

    print("\nFancy car honks its horn twice.")
    fancy_car.horn()
    fancy_car.horn()

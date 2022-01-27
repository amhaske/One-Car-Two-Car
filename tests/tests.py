import pytest


def test_engine(slow_car, fast_car, fancy_car):
    """Checks engine status.

    Parameters
    ----------
    slow_car : SlowCar instance
    fast_car : FastCar instance
    fancy_car : Fancy instance

    """
    # tests if the engine is off
    assert (not slow_car.engine)
    assert (not fast_car.engine)
    assert (not fancy_car.engine)

    slow_car.on()
    fast_car.on()
    fancy_car.on()

    # tests if the engine is on
    assert slow_car.engine
    assert fast_car.engine
    assert fancy_car.engine


def test_speed_on_engine_status(slow_car, fast_car, fancy_car):
    """Checks if the speed changes on the engine status.

    Parameters
    ----------
    slow_car : SlowCar instance
    fast_car : FastCar instance
    fancy_car : Fancy instance

    """

    slow_car.gas(2)
    slow_car.drive(2)
    assert not slow_car.engine and slow_car.current_speed == 0

    fast_car.gas(2)
    fast_car.drive(2)
    assert not fast_car.engine and fast_car.current_speed == 0

    fancy_car.gas(2)
    fancy_car.drive(2)
    assert not fancy_car.engine and fancy_car.current_speed == 0

    slow_car.on()
    slow_car.gas(2)
    slow_car.drive(2)
    assert slow_car.engine and slow_car.current_speed > 0

    fast_car.on()
    fast_car.gas(2)
    fast_car.drive(2)
    assert fast_car.engine and fast_car.current_speed > 0

    fancy_car.on()
    fancy_car.gas(2)
    fancy_car.drive(2)
    assert fancy_car.engine and fancy_car.current_speed > 0


def test_headlights(slow_car, fast_car, fancy_car):
    """Tests for checking if headlights toggle correctly despite the engine status.

    Parameters
    ----------
    slow_car : SlowCar instance
    fast_car : FastCar instance
    fancy_car : Fancy instance

    """
    slow_car.lights = True
    assert not slow_car.engine and slow_car.lights
    slow_car.on()
    slow_car.lights = False
    assert slow_car.engine and not slow_car.lights

    fast_car.lights = True
    assert not fast_car.engine and fast_car.lights
    fast_car.on()
    fast_car.lights = False
    assert fast_car.engine and not fast_car.lights

    fancy_car.lights = True
    assert not fancy_car.engine and fancy_car.lights
    fancy_car.on()
    fancy_car.lights = False
    assert fancy_car.engine and not fancy_car.lights


def test_engine_can_be_turned_off(slow_car, fast_car, fancy_car):
    """Tests if engine can be turned off based on the current speed.

    Parameters
    ----------
    slow_car : SlowCar instance
    fast_car : FastCar instance
    fancy_car : Fancy instance

    """
    slow_car.on()
    fast_car.on()
    fancy_car.on()

    slow_car.gas(2)
    slow_car.drive(2)
    fast_car.gas(2)
    fast_car.drive(2)
    fancy_car.gas(2)
    fancy_car.drive(2)

    assert slow_car.off() == "Cannot turn the engine off as speed is greater than zero, apply brakes."
    assert fast_car.off() == "Cannot turn the engine off as speed is greater than zero, apply brakes."
    assert fancy_car.off() == "Cannot turn the engine off as speed is greater than zero, apply brakes."


def test_gear_for_speed(slow_car, fast_car, fancy_car):
    """Tests if the gear is in a proper state based on the current speed.

    Parameters
    ----------
    slow_car : SlowCar instance
    fast_car : FastCar instance
    fancy_car : Fancy instance

    """
    assert slow_car.current_speed == 0 and slow_car.current_gear == "park"
    assert fast_car.current_speed == 0 and fast_car.current_gear == "park"
    assert fancy_car.current_speed == 0 and fancy_car.current_gear == "park"

    slow_car.on()
    slow_car.gas(2)
    slow_car.drive(2)
    fast_car.on()
    fast_car.gas(2)
    fast_car.drive(2)
    fancy_car.on()
    fancy_car.gas(2)
    fancy_car.drive(2)

    assert slow_car.current_speed > 0 and slow_car.current_gear == "drive"
    assert fast_car.current_speed > 0 and fast_car.current_gear == "drive"
    assert fancy_car.current_speed > 0 and fancy_car.current_gear == "drive"


def test_gear_change(slow_car, fast_car, fancy_car):
    """Tests if the gear and the direction change correctly on gear change.

    Parameters
    ----------
    slow_car : SlowCar instance
    fast_car : FastCar instance
    fancy_car : Fancy instance

    """
    fancy_car.on()
    fancy_car.gear("reverse")
    assert fancy_car.direction == "reverse"

    slow_car.on()
    with pytest.raises(AttributeError):
        assert slow_car.gear("reverse")

    fast_car.on()
    with pytest.raises(AttributeError):
        assert fast_car.gear("reverse")


def test_gas_effect(slow_car, fast_car, fancy_car):
    """Tests the gas function effects on speed and distance.

    Parameters
    ----------
    slow_car : SlowCar instance
    fast_car : FastCar instance
    fancy_car : Fancy instance

    """
    _slow_car_speed = slow_car.current_speed
    _slow_car_trip_distance = slow_car.trip_distance
    slow_car.on()
    slow_car.gas(2)
    assert slow_car.current_speed != _slow_car_speed
    assert slow_car.trip_distance == _slow_car_trip_distance

    _fast_car_speed = fast_car.current_speed
    _fast_car_trip_distance = fast_car.trip_distance
    fast_car.on()
    fast_car.gas(2)
    assert fast_car.current_speed != _fast_car_speed
    assert fast_car.trip_distance == _fast_car_trip_distance

    _fancy_car_speed = fancy_car.current_speed
    _fancy_car_trip_distance = fancy_car.trip_distance
    fancy_car.on()
    fancy_car.gas(2)
    assert fancy_car.current_speed != _fancy_car_speed
    assert fancy_car.trip_distance == _fancy_car_trip_distance


def test_drive_effect(slow_car, fast_car, fancy_car):
    """Tests the drive function effects on acceleration and distance .

    Parameters
    ----------
    slow_car : SlowCar instance
    fast_car : FastCar instance
    fancy_car : Fancy instance

    """
    slow_car.on()
    slow_car.gas(2)
    _slow_car_acceleration = slow_car.acceleration
    _slow_car_trip_distance = slow_car.trip_distance
    slow_car.drive(2)
    assert slow_car.trip_distance != _slow_car_trip_distance
    assert slow_car.acceleration == _slow_car_acceleration

    fast_car.on()
    fast_car.gas(2)
    _fast_car_acceleration = fast_car.acceleration
    _fast_car_trip_distance = fast_car.trip_distance
    fast_car.drive(2)
    assert fast_car.acceleration == _fast_car_acceleration
    assert fast_car.trip_distance != _fast_car_trip_distance

    fancy_car.on()
    fancy_car.gas(2)
    _fancy_car_acceleration = fancy_car.acceleration
    _fancy_car_trip_distance = fancy_car.trip_distance
    fancy_car.drive(2)
    assert fancy_car.acceleration == _fancy_car_acceleration
    assert fancy_car.trip_distance != _fancy_car_trip_distance


def test_brake_effect(slow_car, fast_car, fancy_car):
    """Tests the brake effects on speed and distance.

    Parameters
    ----------
    slow_car : SlowCar instance
    fast_car : FastCar instance
    fancy_car : Fancy instance

    """
    slow_car.on()
    slow_car.gas(2)
    slow_car.drive(2)
    _slow_car_speed = slow_car.current_speed
    _slow_car_distance = slow_car.trip_distance

    slow_car.brake(2)
    assert _slow_car_speed != slow_car.current_speed
    assert _slow_car_distance == slow_car.trip_distance

    fast_car.on()
    fast_car.gas(2)
    fast_car.drive(2)
    _fast_car_speed = fast_car.current_speed
    _fast_car_distance = fast_car.trip_distance

    fast_car.brake(2)
    assert _fast_car_speed != fast_car.current_speed
    assert _fast_car_distance == fast_car.trip_distance

    fancy_car.on()
    fancy_car.gas(2)
    fancy_car.drive(2)
    _fancy_car_speed = fancy_car.current_speed
    _fancy_car_distance = fancy_car.trip_distance

    fancy_car.brake(2)
    assert _fancy_car_speed != fancy_car.current_speed
    assert _fancy_car_distance == fancy_car.trip_distance


def test_max_speed_exceeds(slow_car, fast_car, fancy_car):
    """Tests the maximum speed limit values for each car.

    Parameters
    ----------
    slow_car : SlowCar instance
    fast_car : FastCar instance
    fancy_car : Fancy instance

    """
    slow_car.on()
    fast_car.on()
    fancy_car.on()

    _slow_car_max_speed = slow_car.max_speed
    slow_car.gas(10000)
    assert slow_car.current_speed == _slow_car_max_speed

    _fast_car_max_speed = fast_car.max_speed
    fast_car.gas(10000)
    assert fast_car.current_speed == _fast_car_max_speed

    _fancy_car_max_speed = fancy_car.max_speed
    fancy_car.gas(10000)
    assert fancy_car.current_speed == _fancy_car_max_speed


def test_can_change_gear(slow_car, fast_car, fancy_car):
    """Tests if the gear can be changed in the fancy car.

    Parameters
    ----------
    slow_car : SlowCar instance
    fast_car : FastCar instance
    fancy_car : Fancy instance

    """
    fancy_car.on()
    assert fancy_car.current_speed == 0 and fancy_car.current_gear == "park"
    fancy_car.gas(2)
    assert fancy_car.gear("reverse") == "Cannot change the gear as speed is greater than zero."


def test_distance_difference_on_reverse(slow_car, fast_car, fancy_car):
    """Tests for trip distance increase and home_distance decrease in reverse gear.

    Parameters
    ----------
    slow_car : SlowCar instance
    fast_car : FastCar instance
    fancy_car : Fancy instance

    """
    # tests if the distance increase when the car is driving in reverse gear
    fancy_car.on()
    _fancy_car_distance = fancy_car.trip_distance
    fancy_car.gear("reverse")
    fancy_car.gas(2)
    fancy_car.drive(2)
    assert _fancy_car_distance < fancy_car.trip_distance

    # tests if the distance from home decreases when the car is driving in reverse gear
    fancy_car.brake(10)
    fancy_car.gear("drive")
    fancy_car.gas(2)
    fancy_car.drive(10)
    _fancy_car_distance_from_home = fancy_car.distance_from_home
    fancy_car.brake(10)
    fancy_car.gear("reverse")
    fancy_car.gas(2)
    fancy_car.drive(2)
    assert _fancy_car_distance_from_home > fancy_car.distance_from_home


def test_gear_speed_relation(slow_car, fast_car, fancy_car):
    """Tests the speed and gear relations for each car type.

    Parameters
    ----------
    slow_car : SlowCar instance
    fast_car : FastCar instance
    fancy_car : Fancy instance

    """
    slow_car.on()
    fast_car.on()
    fancy_car.on()

    assert slow_car.current_speed == 0 and slow_car.current_gear == "park"
    assert fast_car.current_speed == 0 and fast_car.current_gear == "park"
    assert fancy_car.current_speed == 0 and fancy_car.current_gear == "park"

    slow_car.gas(2)
    slow_car.drive(2)
    fast_car.gas(2)
    fast_car.drive(2)
    fancy_car.gas(2)
    fancy_car.drive(2)

    assert slow_car.current_speed > 0 and slow_car.current_gear == "drive"
    assert fast_car.current_speed > 0 and fast_car.current_gear == "drive"
    assert fancy_car.current_speed > 0 and fancy_car.current_gear == "drive"

    fancy_car.brake(100)
    fancy_car.gear("reverse")
    fancy_car.gas(2)
    fancy_car.drive(2)
    assert fancy_car.current_speed > 0 and fancy_car.current_gear == "reverse"


def test_individual_attributes(slow_car, fast_car, fancy_car):
    """Tests for custom attributes for each car based on the given base car values.

    Parameters
    ----------
    slow_car : SlowCar instance
    fast_car : FastCar instance
    fancy_car : Fancy instance

    """
    assert slow_car.max_speed == 37.5
    assert slow_car.brake_efficiency == 20

    assert fast_car.max_speed == 150
    assert fast_car.brake_efficiency == 10

    assert fancy_car.max_speed == 100
    assert fancy_car.brake_efficiency == 10

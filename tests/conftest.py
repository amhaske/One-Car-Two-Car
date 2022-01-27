import pytest
from fast_car import FastCar
from fancy_car import FancyCar
from slow_car import SlowCar


@pytest.fixture(autouse=True)
def slow_car():
    slow_car = SlowCar()
    return slow_car


@pytest.fixture(autouse=True)
def fast_car():
    fast_car = FastCar()
    return fast_car


@pytest.fixture(autouse=True)
def fancy_car():
    fancy_car = FancyCar()
    return fancy_car

from abc import ABCMeta, abstractmethod

class Vehicle(metaclass=ABCMeta):
    def __init__(self, company: str,
                 model: str,
                 year: int,
                 num_wheels: int,
                 speed: int):
        self._company = company
        self._model = model
        self._year = year
        self._num_wheels = num_wheels
        self._speed = speed

    @abstractmethod
    def test_drive(self) -> None:
        pass

    @abstractmethod
    def park(self) -> None:
        pass

    @property
    def company(self):
        return self._company

    @property
    def model(self):
        return self._model

    @property
    def year_release(self):
        return self._year

    @property
    def num_wheels(self):
        return self._num_wheels

    @property
    def speed(self):
        return self._speed


class Motorcycle(Vehicle):
    def __init__(self, company: str, model: str, year: int):
        super().__init__(company, model, year, num_wheels=2, speed=0)

    def test_drive(self) -> None:
        self._speed = 75

    def park(self) -> None:
        self._speed = 0


class Car(Vehicle):
    def __init__(self, company: str, model: str, year: int):
        super().__init__(company, model, year, num_wheels=4, speed=0)

    def test_drive(self) -> None:
        self._speed = 60

    def park(self) -> None:
        self._speed = 0


from abc import ABC, abstractmethod
from math import pi


class Figura(ABC):

    def __init__(self, color: str):
        self.color = color

    @abstractmethod
    def obwod(self) -> float:
        pass

    @abstractmethod
    def pole(self) -> float:
        pass

    def show_color(self):
        print(self.color)


class Prostokat(Figura):
    def __init__(self, color: str, a: float, b: float):
        super().__init__(color)
        self.a = a
        self.b = b

    def obwod(self) -> float:
        return 2 * (self.a + self.b)

    def pole(self) -> float:
        return self.a * self.b


class Kolo(Figura):
    def __init__(self, color: str, r: float):
        super().__init__(color)
        self.r = r

    def obwod(self) -> float:
        return 2 * self.r * pi

    def pole(self) -> float:
        return pi * self.r ** 2


class Kwadrat(Figura):
    def __init__(self, color: str, a: float):
        super().__init__(color)
        self.a = a

    def obwod(self) -> float:
        return 4 * self.a

    def pole(self) -> float:
        return self.a * self.a


if __name__ == '__main__':
    prostokat = Prostokat('Pink', 3, 5)
    kolo = Kolo('Red', 12)
    print(prostokat.obwod())
    print(kolo.obwod())
    kwadrat = Kwadrat('Blue', 5)
    print(kwadrat.obwod())
    print(kwadrat.pole())
    kwadrat.show_color()

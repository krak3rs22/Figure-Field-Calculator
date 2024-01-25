from figura import *


class Prostokat(Figura):
    def __init__(self, a, b):
        super().__init__()
        self.a = a
        self.b = b
        self.pole = self.oblicz_pole()

    def oblicz_pole(self):
        return self.a * self.b


class Kwadrat(Prostokat):
    def __init__(self, a):
        super().__init__(a, a)

    def oblicz_pole(self):
        return self.a ** 2
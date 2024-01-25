from figura import *


class Trojkat(Figura):
    def __init__(self, a, b, c):
        super().__init__()
        self.a = a
        self.b = b
        self.c = c
        self.pole = self.oblicz_pole()


class TrojkatRownoramienny(Trojkat):
    def __init__(self, a, b, c):
        super().__init__(a, b, c)

    def oblicz_pole(self):
        p = (self.a + self.b + self.c) / 2
        return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5


class TrojkatRownoboczny(Trojkat):
    def __init__(self, a, b, c):
        super().__init__(a, b, c)

    def oblicz_pole(self):
        return (math.sqrt(3) / 4) * self.a ** 2


class TrojkatRoznoboczny(Trojkat):
    def __init__(self, a, b, c):
        super().__init__(a, b, c)

    def oblicz_pole(self):
        s = 0.5 * (self.a + self.b + self.c)
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

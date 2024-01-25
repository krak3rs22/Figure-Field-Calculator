from abc import ABC, abstractmethod
import math


class Figura(ABC):
    def __init__(self):
        self.pole = None

    def __repr__(self):
        return f"{self.__class__.__name__}({', '.join(f'{k}={v}' for k, v in vars(self).items())})"

    @abstractmethod
    def oblicz_pole(self):
        pass

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return vars(self) == vars(other)
        return False

    def __lt__(self, other):
        return self.pole < other.pole

    def __le__(self, other):
        return self.pole <= other.pole

    def __gt__(self, other):
        return self.pole > other.pole

    def __ge__(self, other):
        return self.pole >= other.pole



















































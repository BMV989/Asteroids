from abc import ABC, abstractmethod


class MovableObject(ABC):
    def __init__(self, x, y, v, a):  # v = v_x, v_y
        self.point_X = x
        self.point_Y = y
        self.speed = v
        self.a = a

    @abstractmethod
    def move(self, a):
        pass


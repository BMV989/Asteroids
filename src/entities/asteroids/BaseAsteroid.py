from abc import ABC, abstractmethod

from src.entities.MovableObject import MovableObject


class BaseAsteroid(MovableObject, ABC):
    def
from __future__ import annotations

from dataclasses import dataclass, field, replace
from typing import Generic, TypeVar


class Probability:
    """assure class attribute is within range of 0 and 1"""

    def __set_name__(self, _, name):
        self.public_name = name
        self.private_name = '_' + name

    def __get__(self, obj, _=None):
        value = getattr(obj, self.private_name)
        return value

    def __set__(self, obj, value):
        if not 0 <= value <= 1:
            raise ValueError("Probability must be between 0 and 1")
        setattr(obj, self.private_name, value)


T = TypeVar('T')


@dataclass
class ProbabilityRecord(Generic[T]):
    """record holding data with associated probability"""
    data: T
    probability: Probability = field(default=Probability())

    def replace(self, **changes) -> ProbabilityRecord:
        """return new instance replacing some are all attributes"""
        return replace(self, **changes)

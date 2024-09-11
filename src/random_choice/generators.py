from __future__ import annotations

from itertools import cycle
from random import choices
from typing import Final, Generic, Protocol, Sequence, TypeVar

T = TypeVar('T')


class ProbabilityRecord(Protocol[T]):
    data: T
    probability: float


class RandomGen(Generic[T]):
    _PROBABILITY_TOL: Final = 1e-6

    def __init__(self, probability_records: Sequence[ProbabilityRecord]):
        if abs(sum(r.probability for r in probability_records) - 1) > self._PROBABILITY_TOL:
            raise ValueError(
                f"Probability weights should add up to unity with tollerance of {self._PROBABILITY_TOL}")

        self._gen = cycle(
            choices([r.data for r in probability_records],
                    weights=[r.probability for r in probability_records],
                    k=10*len(probability_records))
        )

    def next_data(self) -> T:
        return next(self._gen)

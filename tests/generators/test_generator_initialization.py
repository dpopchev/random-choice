from typing import NamedTuple

import pytest

from random_choice.generators import RandomGen


class ProbabilityRecord(NamedTuple):
    data: float
    probability: float


@pytest.fixture
def general_records():
    return [
        ProbabilityRecord(1, 0.2),
        ProbabilityRecord(1, 0.5)
    ]


def test_generator_raises_exception_when_initializing_with_not_normalized_records(general_records):
    with pytest.raises(ValueError):
        RandomGen(general_records)

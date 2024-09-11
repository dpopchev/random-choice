from collections import Counter
from typing import Final, NamedTuple

import pytest

from random_choice.generators import RandomGen

SAMPLE_SiZE: Final[int] = 100


class ProbabilityRecord(NamedTuple):
    data: float
    probability: float


@pytest.fixture
def three_records():
    return [
        ProbabilityRecord(-1, 0.15),
        ProbabilityRecord(0, 0.70),
        ProbabilityRecord(1, 0.15)
    ]


@pytest.fixture
def generator(three_records):
    return RandomGen(three_records)


@pytest.fixture
def sample(generator):
    c = Counter()
    for _ in range(SAMPLE_SiZE):
        c.update([generator.next_data()])

    return c


def test_only_sample_size_data_present(sample):
    assert sample.keys() == set([-1, 0, 1])

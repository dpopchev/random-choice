from collections import Counter
from typing import Final, NamedTuple

import pytest

from random_choice.generators import RandomGen

SAMPLE_SiZE: Final[int] = 100


class ProbabilityRecord(NamedTuple):
    data: float
    probability: float


@pytest.fixture
def records():
    return [
        ProbabilityRecord(-1, 0.01),
        ProbabilityRecord(0, 0.3),
        ProbabilityRecord(1, 0.58),
        ProbabilityRecord(2, 0.1),
        ProbabilityRecord(3, 0.01),
    ]


@pytest.fixture
def generator(records):
    return RandomGen(records)


@pytest.fixture
def sample(generator):
    c = Counter()
    for _ in range(SAMPLE_SiZE):
        c.update([generator.next_data()])
    return c


def test_generated_highest_probabilities(sample):
    assert [s[0] for s in sample.most_common(3)] == [1, 0, 2]


@pytest.mark.xfail(reason="Equal probability for elements")
def test_generated_equal_probabilities(sample):
    assert set([s[0] for s in sample.most_common()[-2:]]) == set([-1, 3])

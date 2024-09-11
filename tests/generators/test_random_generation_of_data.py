from typing import NamedTuple

import pytest


class ProbabilityRecord(NamedTuple):
    data: float
    probability: float


@pytest.fixture
def equal_probability_records():
    return [
        ProbabilityRecord(-1, 0.5),
        ProbabilityRecord(1, 0.5)
    ]


@pytest.fixture
def equal_probabilities_gene


@pytest.fixture
def equal_probabilities_sample(equal_probability_records):
    pass

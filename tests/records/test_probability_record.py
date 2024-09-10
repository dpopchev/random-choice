from typing import Final

import pytest

from random_choice.records import ProbabilityRecord

RECORD_DATA: Final = 10
RECORD_PROBABILITY: Final = 0.2


@pytest.fixture
def record():
    return ProbabilityRecord(RECORD_DATA, RECORD_PROBABILITY)


def test_replace_record_data(record: ProbabilityRecord):
    new_data: int = RECORD_DATA + 10
    assert record.replace(data=new_data).data == new_data


def test_replace_record_probability(record: ProbabilityRecord):
    new_probability: float = RECORD_PROBABILITY / 10
    assert record.replace(
        probability=new_probability).probability == new_probability

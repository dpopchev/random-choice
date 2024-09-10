from typing import Union

import pytest

from random_choice.records import Probability


@pytest.fixture
def make_probability_holding_class():
    class ProbabilityClass:
        probability = Probability()

        def __init__(self, probability):
            self.probability = probability

    return ProbabilityClass


@pytest.mark.parametrize("value", [-10, 10])
def test_existance_of_invalid_probabilities_is_prevented(make_probability_holding_class, value):
    with pytest.raises(ValueError):
        _ = make_probability_holding_class(value)

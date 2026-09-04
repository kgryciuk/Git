import pytest

from flight_calculator import calculate_flight_time, flight_time_table


@pytest.mark.parametrize(
    ("weight_grams", "expected_minutes"),
    [(0, 180), (500, 130), (123.5, 167.65)],
)
def test_calculate_flight_time_uses_weight_formula(
    weight_grams, expected_minutes
):
    assert calculate_flight_time(weight_grams) == pytest.approx(expected_minutes)


def test_calculate_flight_time_rejects_negative_weight():
    with pytest.raises(ValueError, match="Weight cannot be negative"):
        calculate_flight_time(-1)


def test_flight_time_table_returns_weight_and_time_pairs():
    assert flight_time_table(100, 50) == [
        (0, 180),
        (50, 175.0),
        (100, 170.0),
    ]


@pytest.mark.parametrize(
    ("max_weight_grams", "step_grams"),
    [(-1, 10), (100, 0), (100, -10)],
)
def test_flight_time_table_rejects_invalid_arguments(
    max_weight_grams, step_grams
):
    with pytest.raises(
        ValueError,
        match="Max weight must be non-negative and step must be positive",
    ):
        flight_time_table(max_weight_grams, step_grams)

import pytest
from src.processing import filter_by_state_and_date, sort_by_date


@pytest.fixture
def sample_data():
    return [
        {"id": 1, "state": "EXECUTED", "date": "2024-04-25T08:21:33.419441"},
        {"id": 2, "state": "PENDING", "date": "2024-04-25T10:15:42.123456"},
    ]


@pytest.mark.parametrize("id, state, date, expected_result", [
    (1, "EXECUTED", "2024-04-25T08:21:33.419441",
     [{"id": 1, "state": "EXECUTED", "date": "2024-04-25T08:21:33.419441"}]),
    (3, "PENDING", None, [{"id": 2, "state": "PENDING", "date": "2024-04-25T10:15:42.123456"}]),
])
def test_filter_by_state_and_date(sample_data, id, state, date, expected_result):
    assert filter_by_state_and_date(sample_data, state=state, date=date) == expected_result


def test_sort_by_date():
    data = [
        {"id": 1, "state": "EXECUTED", "date": "2024-04-25T08:21:33.419441"},
        {"id": 2, "state": "PENDING", "date": "2024-04-25T10:15:42.123456"},
        {"id": 3, "state": "PROCESSING", "date": "2024-04-23T12:00:00.000000"},
        {"id": 4, "state": "CANCELLED", "date": "2024-04-25T12:00:00.000000"},
    ]

    assert sort_by_date(data) == [
        {"id": 4, "state": "CANCELLED", "date": "2024-04-25T12:00:00.000000"},
        {"id": 2, "state": "PENDING", "date": "2024-04-25T10:15:42.123456"},
        {"id": 1, "state": "EXECUTED", "date": "2024-04-25T08:21:33.419441"},
        {"id": 3, "state": "PROCESSING", "date": "2024-04-23T12:00:00.000000"},
    ]
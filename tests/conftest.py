import pytest

@pytest.fixture
def fizzy_numbers():
    return [3, 6]


@pytest.fixture
def buzzy_numbers():
    return [5, 10]


@pytest.fixture
def fizzbuzzy_numbers():
    return [15, 30]


@pytest.fixture
def quiet_numbers():
    return [1, 2, 4, 7, 8]

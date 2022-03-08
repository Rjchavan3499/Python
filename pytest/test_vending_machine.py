import pytest
@pytest.fixture()
def no_notes():
    a = 880
    Q = [500, 200, 100, 50, 20, 10]

    for i in range(6):
        q = Q[i]
        x += int(a / q)
        a = int(a % q)
    if a > 0:
        x = -1
    return x

def test_note(x):
    assert x == 6

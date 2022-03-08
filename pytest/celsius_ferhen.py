import pytest

@pytest.fixture()
def cel():
   fe = 113
   cel = (fe - 32) / 1.8
   return cel

def test_cel(cel):
   assert cel == 45.00

@pytest.fixture()
def fer():
   cel = 34.00
   fer = (cel * 1.8) + 32
   return fer

def test_ferehen(fer):
   assert  fer == 93.20


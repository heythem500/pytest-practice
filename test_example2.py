import pytest


@pytest.fixture #/before each
def setupFirst():
    print("load the server First")
    print("load the database Second")
    yield #/after each do x
    print("{1.} stop the server...")
    print("{2.} stop the database, end of seassion")


def test_caseE1(setupFirst):
    print("Hello 1")

def test_caseE2(setupFirst):
    print("Hello 2")

def test_caseE3(setupFirst):
    print("Hello 3")

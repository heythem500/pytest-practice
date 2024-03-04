import pytest
from h1 import checkNameHas

@pytest.mark.sanityTest #// use @pytest annotaion import it too, mark it as sanity test or name it
def test_Case1():
    actual_result = checkNameHas("hythemflowers")
    assert actual_result == "hythemflowers" #assert will compare 2 results

@pytest.mark.regression
def test_Case2():
    actual_result = checkNameHas("hythemflowers")
    assert actual_result == "hythemflowers222"

@pytest.mark.sanityTest
def test_Case3():
    actual_result = checkNameHas("hattem@")
    assert actual_result == "member used @ sign" #if we remove even a word case will fail for comparison

@pytest.mark.heythem
def test_case4():
    print("1. hello people, are u ready?")
    print("2. ok, watch this movie")



#example2 from pytest.com
def myvalueIs(numberX):
    return numberX + 1
@pytest.mark.regression #must be above the test_case direcly
def test_Case0():
    assert myvalueIs(4) == 5
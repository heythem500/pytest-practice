import pytest

#if we wanna apply it universal on all project cases without a need to call it else where
@pytest.fixture
def setupSecond():
    print("load the server copy")
    print("load the database copy")
    yield  # /after each do x
    print("{1.} stop the server copy...")
    print("{2.} stop the database copy, end of seassion")


# @pytest.fixture(autouse=True, scope="session") #univeral but once only before/after
@pytest.fixture(autouse=True, scope="function") #univeral before/after every method/test as well
# @pytest.fixture(autouse=True) #univeral before/after every method
def setupThird():
    print("my name is")
    print("but your name is?")
    yield
    print("(((ok got it)))")

#parmaters array, every each test will be done twice since we use 2 params
@pytest.fixture(autouse=True, scope="session", params=["chrome", "firefox"])
def setupFour(request):
    print("open your computer")
    print("open " + request.param + " browser") #no autocomplete u muse write it right "request.param"
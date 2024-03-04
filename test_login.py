import pytest

#assuةe that will test a Login form
#each data sent will be tested on all these tase cases [watch " and ()]
@pytest.mark.parametrize("email, password, result", [("hyttt@gmail.com", "455451", "Yes login worked"), ("mageda@yahoo.com", "9999222", "No login failed visit app later")])
def test_case21(email, password, result): #paras like email will be suggested here
    print('test case 21')
    print("fill the following email " + email)
    print("fill the following password " + password)
    print("have u been able to login?? " + result)

def test_case22():
    print('test case 22')

def test_case22():
    print('test case 23')

#note: when I tried console in this sitituation to do the test it didn't view anything useful don't know why!
"donig good in tha wolrd"

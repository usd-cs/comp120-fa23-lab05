import pytest

from exceptional import foo

def test_foo():
    # test the non-exceptional case
    x = foo(20)
    assert x == 5

    # test the exceptional case
    with pytest.raises(ZeroDivisionError):
        y = foo(0)

# TODO: write a test case for the get_max function, testing it on the
# "meow.txt" and "bad_meow.txt" files



# DO NOT modify anything below this line
if __name__ == "__main__":
    pytest.main(['test_exceptions.py'])

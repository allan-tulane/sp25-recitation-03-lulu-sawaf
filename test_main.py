from main import *



## Feel free to add your own tests here.
def test_multiply():
    assert quadratic_multiply(BinaryNumber(3), BinaryNumber(3)) == 3*3
    assert quadratic_multiply(BinaryNumber(18), BinaryNumber(18)) == 18*18
    assert quadratic_multiply(BinaryNumber(7), BinaryNumber(7)) == 7*7

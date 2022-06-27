from validate_docbr.utils import digitsAreRepeated
from pytest import raises


def test_should_return_true_if_digits_are_repeated():
    assert digitsAreRepeated('11111') == True
    assert digitsAreRepeated(' 11111 ') == True


def test_should_return_true_if_digits_len_are_equal_one():
    assert digitsAreRepeated('1') == True


def test_should_return_false_if_digit_are_empty():
    assert digitsAreRepeated('') == False
    assert digitsAreRepeated(' ') == False


def test_should_return_false_if_digits_are_not_repeated():
    assert digitsAreRepeated('1234') == False


def test_should_raises_TypeError_if_digits_are_None():
    with raises(TypeError):
        digitsAreRepeated(None)

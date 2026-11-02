import code.palindrome_number


def test_palindrome_number():
    assert code.palindrome_number.palindrome_number(121) == True


def test_non_palindrome_number():
    assert code.palindrome_number.palindrome_number(123) == False


def test_single_digit():
    assert code.palindrome_number.palindrome_number(7) == True


def test_palindrome_with_zero():
    assert code.palindrome_number.palindrome_number(12021) == True


def test_zero():
    assert code.palindrome_number.palindrome_number(0) == True
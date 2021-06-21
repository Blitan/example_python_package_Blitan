from example_python_package_Blitan import minus


def test_minus_with_small_numbers():

    answer = minus(7, 3)

    assert answer == 4


def test_minus_with_big_numbers():

    answer = minus(88, 23)

    assert answer == 65
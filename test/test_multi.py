from example_python_package_Blitan import multi


def test_multi_with_small_numbers():

    answer = multi(2, 6)

    assert answer == 12


def test_multi_with_big_numbers():

    answer = multi(15, 12)

    assert answer == 180
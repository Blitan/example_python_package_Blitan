from example_python_package_Blitan import div


def test_div_with_small_numbers():

    answer = div(8, 2)

    assert answer == 4


def test_div_with_big_numbers():

    answer = div(100, 25)

    assert answer == 4
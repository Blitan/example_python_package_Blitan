from example_python_package_Blitan import add

def test_add_with_small_number():

    answer = add(5,2)
    assert answer == 7

def test_add_with_big_number():

    answer = add(73,285)
    assert answer == 358
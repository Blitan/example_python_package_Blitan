
from example_python_package_Blitan import my_name

def test_long_name():

    answer = my_name('averylongname')

    assert answer == "my name is averylongname"

def test_short_name():

    answer = my_name('name')

    assert answer == "my name is name"
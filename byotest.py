def test_are_equal(actual, expected):
    assert expected == actual, "Expected {0}, got {1}".format(expected, actual)
    
def test_not_equal(a, b):
    assert a != b, "Did not expect {0}, but got {1}".format(a, b)
    
def test_is_in(collection, item):
    assert item in collection, "{0} does not contain {1}".format(collection, item)
    
def test_not_in(collection, item):
    assert item not in collection, "{0} does contain {1}".format(collection, item)
    
def test_between(upper_limit, lower_limit, actual):
    assert lower_limit <= actual <= upper_limit, "{2} is not between {0} & {1}".format(upper_limit, lower_limit, actual)

test_are_equal(32, 32)

test_not_equal(32, 34)

test_is_in([1, 8, 5, 3, 3, 7, 4, 3], 5)

test_not_in([1, 8, 5, 3, 3, 7, 4, 3], 6)

test_between(8, 2, 5)
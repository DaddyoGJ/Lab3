import price_info as price

def test_total_cost_shopping():
    expected = 46.75
    result = price.total_cost_shopping()

    assert (expected == result)

def test_cost_of_fruit():
    expected = 14.0
    result = price.cost_of_fruits('orange', 10)

    assert (expected == result)
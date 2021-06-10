from math_series.series import fibonacci, lucas

# fibonacci series
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55.....
def test_one():
  actual = fibonacci(11)
  expected = 55
  assert actual == expected

def test_two():
  actual = fibonacci(9)
  expected = 21
  assert actual == expected

# Lucas Numbers
# 2, 1, 3, 4, 7, 11, 18, 29, 47
def test_three():
  actual = lucas(10)
  expected = 47
  assert actual == expected

def test_four():
  actual = lucas(4)
  expected = 7
  assert actual == expected

# # sum_series

# def test_five():
#   actual = lucas(0)
#   expected = 0
#   assert actual == expected

# def test_six():
#   actual = lucas(2, 2, 1)
#   expected = 3
#   assert actual == expected
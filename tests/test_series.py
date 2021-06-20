from math_series.series import fibonacci, lucas, sum_series

# Fibonacci Tests
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144

def test_one():
  actual = fibonacci(11)
  expected = 55
  assert actual == expected

def test_two():
  actual = fibonacci(6)
  expected = 5
  assert actual == expected

# Lucas Tests
# 2, 1, 3, 4, 7, 11, 18, 29, 47, 76, 123

def test_three():
  actual = lucas(8)
  expected = 47
  assert actual == expected

def test_four():
  actual = lucas(4)
  expected = 7
  assert actual == expected

# Sum Series Tests

def test_five():
  actual = sum_series(0)
  expected = 0
  assert actual == expected

def test_six():
  actual = sum_series(2, 2, 1)
  expected = 3
  assert actual == expected
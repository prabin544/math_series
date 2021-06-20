def fibonacci(n):
  """
  Return the nth value in the fibonacci series.
  """
  if n <= 1:
    return 0
  elif n == 2:
    return 1
  else:
    return fibonacci(n-1) + fibonacci(n-2)

def lucas(n):
  """
  Returns the nth value in the lucas numbers
  """
  if n <= 0:
      return 2
  if n == 1: 
      return 1
  return lucas(n-1) + lucas(n-2)

def sum_series(n, x=0, y=1):
  """
  Calling this function with no optional parameters will produce numbers from the fibonacci series. Calling it with the optional arguments 2 and 1 will produce values from the lucas numbers.
  """
  if n == 0:
    return x
  if n == 1:
    return y
  return sum_series(n-1, x, y) + sum_series(n-2, x, y)
import math

def hypotenuse(x,y):
    return math.sqrt(x**2 + y**2)

def fare(distance):
    return (4 + round(distance/140,0) * 0.25)

def shipping_cost(items):
    return 10.95 + 2.95 * items - 1

def median_3(x,y,z):
    average = (x + y + z) / 3
    return average

def ordinal(number):
    if number == 1:
        return "first"
    elif number == 2:
        return "second"
    elif number == 3:
        return "third"
    elif number == 4:
        return "fourth"
    elif number == 5:
        return "fifth"
    elif number == 6:
        return "sixth"
    elif number == 7:
        return "seventh"
    elif number == 8:
        return "eighth"
    elif number == 9:
        return "ninth"
    elif number == 10:
        return "tenth"
    elif number == 11:
        return "eleventh"
    elif number == 12:
        return "twelveth"
    else:
        return "error unidentified value"
        
# tests

from main import hypotenuse
from main import fare
from main import shipping_cost
from main import median_3
from main import ordinal

def test_hypotenuse():
  assert hypotenuse(10,5) == 11.180339887498949
  assert hypotenuse(8,7) == 10.63014581273465
  assert hypotenuse(3,4) == 5
  print("All tests passed.")

def test_fare():
  assert fare(547) == 5
  assert fare (280) == 4.5
  assert fare (420) == 4.75
  print("All tests passed.")

def test_shipping_cost():
  assert shipping_cost(3) == 18.8
  assert shipping_cost(5) == 24.7
  assert shipping_cost(42) == 133.85
  print("All tests passed.")

def test_median_3():
  assert median_3(10,5,12) == 9
  assert median_3(52,5,12) == 23
  assert median_3(52,23,12) == 29
  print("All tests passed.")

def test_ordinal():
  assert ordinal(1) == "first"
  assert ordinal(3) == "third"
  assert ordinal(12) == "twelveth"
  print("All tests passed.")

def parrot_trouble(talking, hour):
  return (talking and (hour < 7 or hour > 20))

def diff21(n):
  if n > 21:
    return abs(n - 21) * 2
  else: 
   return abs(n - 21)
   
def makes10(a, b):
  if a == 10 or b == 10:
    return True
  elif a + b == 10:
    return True
  else:
    return False
    
def monkey_trouble(a_smile, b_smile):
  if a_smile and b_smile:
   return True
  if not a_smile and not b_smile:
   return True
  if a_smile or b_smile:
   return False
   
def sleep_in(weekday, vacation):
  if not weekday or vacation:
   return True
  else:
   return False
   
# test

from diff21 import diff21

def test_diff21():
    assert diff21(19) == 2
    assert diff21(10) == 11
    assert diff21(21) == 0
    assert diff21(22) == 2
    assert diff21(25) == 8
    assert diff21(30) == 18
    assert diff21(0) == 21
    assert diff21(1) == 20
    assert diff21(2) == 19
    assert diff21(-1) == 22
    assert diff21(-2) == 23
    assert diff21(50) == 58
    print("All tests passed.")
    
from main import parrot_trouble

def test_parrot_trouble():
    assert parrot_trouble(True,6) == True
    assert parrot_trouble(True,7) == False
    assert parrot_trouble(False,6) == False
    assert parrot_trouble(True,21) == True
    assert parrot_trouble(False,21) == False
    assert parrot_trouble(True,23) == True
    assert parrot_trouble(False,23) == False
    assert parrot_trouble(True,20) == False
    assert parrot_trouble(False,12) == False
    print("All tests passed.")
    
from makes10 import makes10

def test_makes10():
  assert makes10(9, 10) == True
  assert makes10(9,9) == False
  assert makes10(1,9) == True
  assert makes10(10,1) == True
  assert makes10(10,10) == True
  assert makes10(8,2) == True
  assert makes10(8,3) == False
  assert makes10(10,42) == True
  assert makes10(12,-2) == True
  
from monkey_trouble import monkey_trouble

def test_monkey_trouble():
    assert monkey_trouble(True, True) == True
    assert monkey_trouble(False, False) == True
    assert monkey_trouble(True, False) == False
    assert monkey_trouble(False, True) == False
    print("All tests passed.")

from sleep_in import sleep_in

def test_sleep_in():
    assert sleep_in(False, False) == True
    assert sleep_in(True, False) == False
    assert sleep_in(False, True) == True
    assert sleep_in(True, True) == True
    print("All tests passed.")
    

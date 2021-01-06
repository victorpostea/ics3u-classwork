#functions
def test_sleep_in():
    assert sleep_in(False, False) == True
    assert sleep_in(True, False) == False
    assert sleep_in(False, True) == True
    assert sleep_in(True, True) == True
    print("All tests passed.")

def test_monkey_trouble():
    assert monkey_trouble(True, True) == True
    assert monkey_trouble(False, False) == True
    assert monkey_trouble(True, False) == False
    assert monkey_trouble(False, True) == False
    print("All tests passed.")

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

# tests
def sleep_in(weekday, vacation):
  if not weekday or vacation:
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

def diff21(n):
  if n > 21:
    return abs(n - 21) * 2
  else: 
   return abs(n - 21)


test_sleep_in()

test_monkey_trouble()

test_diff21()

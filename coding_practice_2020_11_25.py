# 1
def double_char(str):
    return ''.join(char * 2 for char in str)
    
# 2    
def count_code(str):
  times = 0
  for i in range(0,len(str)):
    if str[i:i + 2] == 'co':
      if str[i + 3: i + 4] == 'e':
        times = times + 1
  return times
  
# 3  
def count_code(str):
times = 0
for i in range(0,len(str)):
  if str[i:i + 2] == 'co':
    if str[i + 3: i + 4] == 'e':
      times = times + 1
return times

# 4
def end_other(a, b):
    a = a.lower()
    b = b.lower()
        
    return a.endswith(b) or b.endswith(a)
    
# 5 
def cat_dog(str):
  countcat = 0
  for i in range(0,len(str) - 1):
    if str[i:i + 3] == 'cat':
      countcat = countcat + 1
  countdog = 0
  for i in range(0,len(str) - 1):
    if str[i:i + 3] == 'dog':
      countdog = countdog + 1
  
  if countdog == countcat:
    return True
  else:
    return False
    
# 6    
def xyz_there(str):
  for i in range(len(str)):
    if str[i] != '.' and str[i+1:i+4] == 'xyz':
      return True
  if str[0:3] == 'xyz':
    return True
  return False
  
# 7  
def count_evens(nums):
  count = 0
  for i in range(0,len(nums)):
    if nums[i] % 2 == 0:
      count += 1 

  return count

# 8
def has22(nums):
  for i in range(0, len(nums) - 1):
    if nums[i] == 2 and nums[i + 1] == 2:
      return True
  return False
  
# 9  
def centered_average(nums):
  items = len(nums)
  total = 0
  high = max(nums)
  low = min(nums)
  for num in nums:
    total += num
  aveg = (total -high-low) / (items-2)
  return aveg
  
# 10  
def big_diff(nums):
  a = min(nums)
  b = max(nums)
  return b - a


# Q1 from python workbook

print("Victor Postea")
print("100 Swampshore Rd, ON")

# Q2 from python workbook

name = input("What is your name?:")
print(f"Hi {name}!")

# Q3 from python workbook

length = float(input("What is the length?:"))
width = float(input("What is the width?:"))
area = length * width
print(f"The area is {area}")

# Q4 from python workbook

length = float(input("What is the length in feet?:"))
width = float(input("What is the width in feet?:"))
area = length * width
acre_area = area // 43560.0
print(f"The area is {acre_area}")

# Q5 from python workbook

moneyback = 0

while True:

    print("Enter ""1"" if you want to submit a(nother) bottle")
    print("Enter ""2"" to end")
    choice = int(input("Choice:"))

    if choice == 1:
        size = float(input("How big is your waterbottle in liters?:"))
        if size <= 1:
            moneyback += 0.1
        else:
            moneyback += 0.25
    elif choice == 2:
        print(f"You get back ${moneyback}.")
        break
    else:
        print("error try again")


# Q6 python workbook

cost = int(input("How much did your meal cost?: "))
tax = 0.13 * cost
tip = 0.18 * cost
grand_total = round(tax + tip + cost,2)
print(f"Your grand total is ${grand_total}")


# Q7 python workbook

number = int(input("Choose a number: "))
sum = (number * (number + 1)) // 2
print(f"The sum of all numbers from 1 to {number} is {sum}")


# Q8 python workbook

widgets = int(input("How many widgets are you buying?: "))
gizmos = int(input("How many gizmos are you buying?: "))

weight = widgets * 75 + gizmos * 112

print(f"The total weight of your order is {weight}g")


# Q9 from python workbook

starting_cash = int(input("How much money did you put in your savings account?: "))

cash_1 = round(starting_cash * 1.04,2)

cash_2 = round(cash_1 * 1.04,2)

cash_3 = round(cash_2 * 1.04,2)

print(f"After 1 year you will have ${cash_1}, after 2 you will have ${cash_2} and after 3 you will have ${cash_3}.")


# Q10 from python workbook

import math

a = int(input("What is a?: "))
b = int(input("What is b?: "))

added = a + b
difference = a - b
product = a * b
quotient = a // b
remainder = a % b
log = math.log10(a)
exponent = a ** b

print(f"The sum, difference, product, quotient, remainder, log and exponent in that order of a and b are as follows (seperated by a comma): {added}, {difference}, {product}, {quotient}, {remainder}, {log}, {exponent}")


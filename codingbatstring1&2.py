def first_last6(nums):
  if nums[0] == 6:
    return True
  elif nums[len(nums) - 1] == 6:
    return True
  else:
    return False
    
def common_end(a, b):
  if a[0] == b[0]:
    return True
  elif a[len(a) - 1] == b[len(b) - 1]:
    return True
  else:
    return False
    
def reverse3(nums):
  a = nums[0]
  b = nums[1]
  c = nums[2]
  newList = [c,b,a]
  return newList
  
def middle_way(a, b):
  mid1 = a[1]
  mid2 = b[1]
  newList = [mid1,mid2]
  return newList
  
def same_first_last(nums):
  if len(nums) >= 1:
    if nums[0] == nums[len(nums) - 1]:
      return True
    else:
      return False
  else:
    return False

def sum3(nums):
  a = nums[0]
  b = nums[1]
  c = nums[2]
  return a + b + c
  
def max_end3(nums):
  a = nums[0]
  b = nums[2]
  c = max(a,b)
  newList = [c,c,c]
  return newList
  
def make_ends(nums):
  a = nums[0]
  b = nums[len(nums) - 1]
  newList = [a,b]
  return newList
  
def make_pi():
  return [3,1,4]
  
def rotate_left3(nums):
  a = nums[0]
  b = nums[1]
  c = nums[2]
  newlist = [b,c,a]
  return newlist

def count_evens(nums):
  count = 0
  for i in range(0,len(nums)):
    if nums[i] % 2 == 0:
      count += 1 

  return count
  
def big_diff(nums):
  a = min(nums)
  b = max(nums)
  return b - a
  
def centered_average(nums):
  items = len(nums)
  total = 0
  high = max(nums)
  low = min(nums)
  for num in nums:
    total += num
  aveg = (total -high-low) / (items-2)
  return aveg

def sum13(nums):
  elem_sum = 0
  index = 0

  while index < len(nums):
    if nums[index] != 13:
      elem_sum += nums[index]
    else:
      index += 1 #nums[i] is 13, so skip the next element'
    index += 1

  return elem_sum
  
def sum67(nums):
    total = 0
    found6 = False
      
    for i in range(len(nums)):
        if nums[i] == 6:
            found6 = True
        if not found6:
            total += nums[i]
        if nums[i] == 7 and found6:
            found6 = False
            
    return total
    
def has22(nums):
  for i in range(0, len(nums) - 1):
    if nums[i] == 2 and nums[i + 1] == 2:
      return True
  return False
  
  # there was only 6 string_2 questions for python so I just did all of those

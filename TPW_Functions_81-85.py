import math

# 81 

def hypotenuse(x,y):
    return math.sqrt(x**2 + y**2)

def main():
    x = int(input("What is the first side length?: "))
    y = int(input("What is the second side length?: "))
    print(hypotenuse(x,y))


# 82

def fare(distance):
    return (f"${4 + round(distance/140,0) * 0.25}")

def main():
    distance = int(input("What is the total distance travelled?: "))
    print(fare(distance))

# 83

def shipping_cost(items):
    return 10.95 + 2.95 * items - 1

def main():
    items = int(input("How many items are you shipping?: "))
    print(shipping_cost(items))
    
# 84

def median_3():
    x = int(input("What is the first number length?: "))
    y = int(input("What is the second number length?: "))
    z = int(input("What is the third number length?: "))
    average = (x + y + z) / 3
    return average

# 85

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

def main():
    number = int(input("What number do you want to convert?: "))
    print(ordinal(number))

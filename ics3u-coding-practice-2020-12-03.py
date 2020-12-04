def add3(x,y,z):
    return x + y + z

def name_age(name,age):
    return name + age

def average(x,y):
    return (x+y)/2

def largest(x,y,z):
    if x > z:
        if x > y:
            return x
        else:
            return y
    elif y > z:
        return y
    else:
        return z

def first_two(str):
    return str[:2]

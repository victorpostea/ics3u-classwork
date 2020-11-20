# Q1

favcolor = input("What's your favorite color?:")
favcolorcaps = favcolor.capitalize()
print(f"{favcolorcaps}? ME TOO! I really love {favcolor} infact a wall in my room is painted {favcolor}.")


# Q2

cans_per_pack = int(input("How many cans are there in a pack?:"))
packs = int(input("How many packs are there?:"))
totalcans = packs * cans_per_pack
print(f"There is a total of {totalcans} cans.")


#3

width = int(input("What is the width?:"))
length = int(input("What is the length?:"))
height = int(input("What is the height?:"))
volume = height * length * width

print(f"The volume is {volume} units^3.")


#4

choice = input("If you join this google meet will you mute the teacher?:")
choicelower = choice.lower()
if choicelower == "no":
    print("Ok good.")
elif choicelower == "yes":
    print("That's probably not a great idea.")
else:
    print("error")
    
    

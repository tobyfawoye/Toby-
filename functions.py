def calculate_velocity():
    d = float(input("Enter Distance"))
    t = float(input("Enter Time"))
    velocity = d/t
    print*(velocity)


def calculate_area():
    pi = 22/7
    radius = float(input("Enter Radius"))
    area = pi * radius * radius
    print(area)

# choice = input("Enter v for velocity or a for area")
# if choice == "v":
#     calculate_velocity()
# elif choice == "a":
#     calculate_area
# else:
#     print("Choose a valid input")




#  *============== Arguments =================*

def calculate_velocity(d, t):
    velocity = d/t
    print(velocity)

calculate_velocity(100, 56)

def calculate_area(radius):
    pi = 22/7
    area = pi * radius * radius
    print(area)

# choice = input("Enter v for velocity or a for area: ")
# if choice == "v":
#     a = float(input("Enter Distance: "))
#     b = float(input("Enter Time: "))
#     calculate_velocity(a, b)
# elif choice == "a":
#     c = float(input("Enter Radius: "))
#     calculate_area(c)
# else:
#     print("Choose a valid input")
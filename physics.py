# formulas = [
#     "Newton's second law: F = m × a",
#     "Kinetic energy: KE = ½ × m × v²",
#     "Gravitational potential energy: PE = m × g × h",
#     "Wave speed: v = f × λ",
#     "Ohm's law: V = I × R",
# ]

# for formula in formulas:
#     print(formula)

def Newton():
    m = float(input("Enter Mass: "))
    a = float(input("Enter Acceleration: "))
    Force = m * a
    print(Force, "N")


def kinetic_energy():
    m = float(input("Enter Mass: "))
    v = float(input("Enter Velocity: "))
    kinetic_energy = 1 / 2 * m * v * v
    print(kinetic_energy, "J")


def Gravitational():
    m = float(input("Enter Mass: "))
    h = float(input("Enter Height: "))
    gravitational_potential_energy = m * 10 * h
    print(gravitational_potential_energy, "J")


def Wave():
    F = float(input("Enter Frequency: "))
    n = float(input("Enter Number Of Wavelengths: "))
    Wave_Speed = F * n
    print(Wave_Speed, "m/s")


def ohm():
    i = float(input("Enter Current: "))
    r = float(input("Enter Resistance: "))
    Potential_Difference = i * r
    print(Potential_Difference, "V")


def Formula():
    print(
        "1. Newton's Second Law \n"
        "2. Kinetic Energy \n"
        "3. Gravitational Potential Energy \n"
        "4. Wave Speed \n"
        "5. Ohm's Law"
    )
    option = input(" Pick A Number: ")

    if option == "1":
        Newton()

    elif option == "2":
        kinetic_energy()

    elif option == "3":
        Gravitational()

    elif option == "4":
        Wave()

    elif option == "5":
        ohm()

    else:
        print("Invalid Option")
        Formula()
a = 1
while a == 1:
    Formula()

    while True:
        text = input("Would You Like To Continue? (yes/no): ")
        choice = text.lower()

        if choice == "yes":
            break
        elif choice == "no":
            print("Session Ended!")
            a = 0
            break
        else:
            print("Invalid Input")
        

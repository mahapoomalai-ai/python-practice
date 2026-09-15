print("===== CivicAssist - DAY 8 =====")

try:
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))

    print("\nCitizen Details")
    print("Name:", name)
    print("Age:", age)

    if age >= 18:
        print("Status: Adult Citizen")
    else:
        print("Status: Minor Citizen")

except ValueError:
    print("\nInvalid input!")
    print("Please enter your age as a number.")

print("\nThank you for using CivicAssist!")

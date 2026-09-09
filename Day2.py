print("================================")
print("       CIVICASSIST - DAY 2")
print("================================")

name = input("Enter your name: ")
age = int(input("Enter your age: "))
city = input("Enter your city: ")

print("\n--- Citizen Details ---")
print("Name:", name)
print("Age:", age)
print("City:", city)

if age >= 18:
    print("Status: Eligible for adult services")
else:
    print("Status: Minor")

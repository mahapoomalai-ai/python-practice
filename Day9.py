print("===== CivicAssist - DAY 9 =====")


class Citizen:

    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def display_details(self):
        print("\n--- Citizen Details ---")
        print("Name:", self.name)
        print("Age:", self.age)
        print("City:", self.city)

    def check_eligibility(self):
        if self.age >= 18:
            print("Status: Eligible for adult services")
        else:
            print("Status: Minor Citizen")


name = input("Enter your name: ")
age = int(input("Enter your age: "))
city = input("Enter your city: ")

citizen1 = Citizen(name, age, city)

citizen1.display_details()
citizen1.check_eligibility()

print("\nThank you for using CivicAssist!")

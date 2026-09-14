print("===== CivicAssist - Government Service Assistant =====")


def show_services():
    print("\nAvailable Services:")
    print("1. Aadhaar Service")
    print("2. Driving Licence")
    print("3. Voter ID")
    print("4. Passport")


def check_service(choice, age):
    if choice == "1":
        print("\nAadhaar Service selected.")
        print("Required: Identity Proof")

    elif choice == "2":
        if age >= 18:
            print("\nYou are eligible for Driving Licence.")
            print("Required: Age Proof and Identity Proof")
        else:
            print("\nYou are not eligible for Driving Licence.")

    elif choice == "3":
        if age >= 18:
            print("\nYou are eligible for Voter ID.")
            print("Required: Identity and Address Proof")
        else:
            print("\nYou are not eligible for Voter ID.")

    elif choice == "4":
        print("\nPassport Service selected.")
        print("Required: Identity and Address Proof")

    else:
        print("\nInvalid choice.")


name = input("Enter your name: ")
age = int(input("Enter your age: "))

print("\nWelcome,", name)

show_services()

choice = input("\nEnter your choice (1-4): ")

check_service(choice, age)

print("\nThank you for using CivicAssist!")

print("===== CivicAssist - Eligibility Checker =====")

age = int(input("Enter your age: "))

print("\nSelect a service:")
print("1. Aadhaar Service")
print("2. Driving Licence")
print("3. Voter ID")
print("4. Passport")

choice = input("Enter your choice (1-4): ")

if choice == "1":
    print("Aadhaar Service selected.")
    print("Please provide your identity proof.")

elif choice == "2":
    if age >= 18:
        print("You are eligible to apply for a Driving Licence.")
        print("Please provide your age and identity proof.")
    else:
        print("You are not eligible. You must be 18 or above.")

elif choice == "3":
    if age >= 18:
        print("You are eligible for Voter ID.")
        print("Please provide your identity and address proof.")
    else:
        print("You are not eligible for Voter ID.")

elif choice == "4":
    print("Passport Service selected.")
    print("Please provide your identity and address proof.")

else:
    print("Invalid choice. Please select 1-4.")

print("\nThank you for using CivicAssist!")

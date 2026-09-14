# CivicAssist - Day 6
# Loops and Menu System

print("===== CivicAssist - DAY 6 =====")

services = [
    "Aadhaar Service",
    "Driving Licence",
    "Voter ID",
    "Passport",
    "Birth Certificate"
]

while True:

    print("\n--- Government Services ---")

    for i, service in enumerate(services, start=1):
        print(i, ".", service)

    print("6 . Exit")

    choice = int(input("\nEnter your choice (1-6): "))

    if choice == 6:
        print("\nThank you for using CivicAssist!")
        break

    elif 1 <= choice <= 5:
        selected_service = services[choice - 1]

        print("\nYou selected:", selected_service)
        print("Please check the required documents.")

    else:
        print("\nInvalid choice. Please select 1-6.")

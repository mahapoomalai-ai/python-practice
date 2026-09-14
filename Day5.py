# CivicAssist - Day 5
# Lists and Dictionaries

print("===== CivicAssist - DAY 5 =====")

services = [
    "Aadhaar Service",
    "Driving Licence",
    "Voter ID",
    "Passport",
    "Birth Certificate"
]

print("\nAvailable Government Services:")

for i, service in enumerate(services, start=1):
    print(i, ".", service)


service_details = {
    "Aadhaar Service": "Identity and Address Proof",
    "Driving Licence": "Age Proof and Identity Proof",
    "Voter ID": "Identity and Address Proof",
    "Passport": "Identity and Address Proof",
    "Birth Certificate": "Hospital Record and ID Proof"
}

choice = int(input("\nEnter your choice (1-5): "))

if 1 <= choice <= 5:
    selected_service = services[choice - 1]

    print("\nSelected Service:", selected_service)
    print("Required Documents:", service_details[selected_service])

else:
    print("\nInvalid choice. Please select 1-5.")

print("\nThank you for using CivicAssist!")

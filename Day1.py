print("===========================")
print("CIVICASSIST")
print("Smart Government service Finder")
print("===========================")
print("\n Available Services:")
print("1.Birth Certificate")
print("2.Aadhaar service")
print("3.Passport Service")
print("4.Driving Licence")
print("5.Voter ID")
choice=input("\nEnter you choice(1-5):")
if choice == "1":
  print("\nService:Birth Certificate")
  print("Department:Local Government")
  print("Documents:ID Proof,Hospital Record")
  
  elif choice == "2":
    print("\nService: Aadhaar Service")
    print("Department: UIDAI")
    print("Documents: Identity and Address Proof")

elif choice == "3":
    print("\nService: Passport Service")
    print("Department: Passport Seva")
    print("Documents: ID Proof, Address Proof")

elif choice == "4":
    print("\nService: Driving Licence")
    print("Department: Transport Department")
    print("Documents: ID Proof, Age Proof")

elif choice == "5":
    print("\nService: Voter ID")
    print("Department: Election Commission")
    print("Documents: ID Proof, Address Proof")

else:
    print("\nInvalid choice. Please select 1-5.")

print("\nThank you for using CivicAssist!")

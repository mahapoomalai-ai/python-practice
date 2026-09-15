print("=====CivicAssist-DAY 7=====")
name=input("Enter your name:")
age=input("Enter your age:")
city=input("Enter your city:")

Service=input("Enter the government service you need:")

with open("citizen_data.txt","a")as file:
  file.write("Name:"+name+"\n")
  file.write("Age:"+age+"\n")
  file.write("City:"+city+"\n")
  file.write("Service:"+service+"\n")

file.write("------------------------\n")
print("\nCitizen details saved successfully!")
print("Thank you for using CivicAssist")

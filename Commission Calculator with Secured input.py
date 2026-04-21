"""Commission Calculator with Secured Input"""

print("Enter Your Full Name")
fullName = input()

while len(fullName) < 1:  # Just so if you made an error entering it doesn't kick you out! While Loop!
        print("Error: No Data Entered!")
        fullName = input("Enter Full Name: ")

    #All of this under while loop For the script to work!
print(f"Thank you, {fullName}. Let's Calculate those sales.")

print("Enter Your Company Name")
companyName = input()
print("Enter Total Amount of Sales")
totalAmount = float(input())
while totalAmount < 0:
    print("Error: Non Applicable Data!") # double while loops (Make sure to keep intendtation within the while for the while loop) the rest are in line.
    totalAmount = float(input("Enter Total Amount: "))

commission = totalAmount * 0.10

print(f"Rep: {fullName} ({companyName})")
print(f"Sales Amount: ${totalAmount:,.2f}") # Added a comma for thousands!
print(f"Commission of (10%): ${commission:,.2f}") #.2f means having a decimal be in 2 places so "$20000.00
print("Have a nice day!")
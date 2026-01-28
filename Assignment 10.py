'''
Challenge: Implement error handling to ensure that the user enters a positive integer for the age.

==================================
Input: Prompt the user to enter their age.
Processing: Classify the age into different categories:
Under 18: Minor
18-65: Adult
Above 65: Senior citizen
Output: Display the category based on the entered age.
'''
# Ask the user to enter their age
age_input = int(input("Enter your age: "))
# Check if the input is a number and not an empty string
if age_input.isdigit():
    age = int(age_input)

    if age_input > 0:

        if age < 18:
             print("Minor")

        elif  18 <= age <= 65:
            print("Adult")


        else:
            print("Senior Citizen")

    else:
        print("Error: Age must be positive integer")

else:
    print("Error: Invalid input! Please enter a positive integer")



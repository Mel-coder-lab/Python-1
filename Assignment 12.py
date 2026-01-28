"""Challenge: Use nested loop structures to print the pattern efficiently and neatly. Allow the user to specify the character used for the pattern.

=========================================
Description: Develop a program that prompts the user to enter the number of rows for a pattern and then prints a pattern of asterisks (*) in the form of a right triangle.
"""

# asking the user for a number of rows
rows = int(input("Enter number of rows: "))
ch = input("Enter a character to use: ")

for i in range(1, rows + 1):
    print(ch * i)
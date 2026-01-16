'''
Challenge: Provide feedback to the user based on their BMI category (e.g., underweight, normal weight, overweight, obese).

===============================
Input: Prompt the user to enter their weight in kilograms and height in meters.
Processing: Calculate the BMI using the formula: BMI = Weight / (Height^2).
Output: Display the calculated BMI.

'''

# The input section is being solved below
# We are creating 2 inputs to solve this assignment
# all variables must be written as is

weight = float (input('Enter your weight in kilograms: '))
height = float (input('Enter your height in meters: '))

#  The processing section and calculations are being addressed below

Bmi = weight / (height ** 2)

# This is the output below

print ('Your BMI is:', Bmi)
"""
=============================

Input: Prompt the user to enter the principal amount, interest rate (in percentage), and the time period (in years).

Processing: Calculate the simple interest using the formula: Simple Interest = (Principal * Rate * Time) / 100.

Output: Display the calculated simple interest.
"""
# Input section is solved below

Principal = 'Principal_Amount'
Principal_Amount = float (input(' enter Principal_Amount: ' ))
Interest_Rate = float (input('Enter Interest Rate: '))
Interest_rate = float (input('enter Interest Rate: ' ))
Time = float (input('enter Time:' ))

#  Processing is solved below
Simple_Interest = (Principal_Amount * Interest_rate) / 100

# The output is addressed below
print ('Simple Interest: ', Simple_Interest )

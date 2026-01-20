'''
Challenge: Allow the user to choose from multiple currency pairs and implement appropriate error handling for invalid currency inputs.

==============================================
Input: Ask the user to enter an amount in one currency (e.g., USD).
Processing: Convert the amount to another currency (e.g., EUR) using a fixed exchange rate.
Output: Display the converted amount in the target currency.
'''

# Below the customer is asked to enter the amount in usd, line 12 is the fixed exchanged rate defining USD_to_EUR = 0.92
USD = float (input ('Enter amount in USD: '))
USD_to_EUR = 0.92

#Processing exchange rate conversion
eur = USD * USD_to_EUR

# Output the result of eur since eur 'displays as another currency used in fixed rate from usd to eur'
print (eur)






"""Challenge: Use a loop structure to compare characters from both ends of the string to determine whether it is a palindrome.

===================================
Description: Write a program that prompts the user to enter a string and then checks whether it is a palindrome. A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward."""

# User enters string

text = input('Enter a string: ')
left = 0
right = len(text) - 1
is_palindrome = True
while left < right:
    if text[left] != text[right]:
        is_palindrome = False
        break
    left += 1
    right -= 1
if is_palindrome:
    print("Yes, that is a palindrome")
else:
    print("No, that is not a palindrome")

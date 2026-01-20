'''
Challenge: Implement error handling to ensure that the user enters a non-negative number for the time duration.

=======================================================
Input: Prompt the user to enter a time duration in hours.
Processing: Convert the time duration to minutes and seconds.
Output: Display the converted time duration in minutes and seconds.
'''

# Input implemented below

time = float(input('Enter a time duration in hours: '))

# Processing

minutes = float(input('Enter a number of minutes: '))
seconds = float(input('Enter a number of seconds: '))
duration = time * 60 + minutes * 60 + seconds
time_duration = duration / 60
# Output

print (time_duration)
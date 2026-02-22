try:
     num = int(input("Enter a number: "))
     result = 10 / num
except ValueError:
    print("Invalid Input")
except ZeroDivisionError:
    print("Division by zero")

else:
    print("Results are: ", result)

finally:
    print("Execution Completed")

# nothing is divided by zero so this is just an example of using exception components!
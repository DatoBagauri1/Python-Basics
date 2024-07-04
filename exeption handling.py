#exeption
try:
    numerator=int(input("Enter a numberto divide: "))
    denominator=int(input("Enter a number to divide by: "))
    result=numerator/denominator

except ZeroDivisionError as e:
    print(e)
    print("You can't divide by zero"  )
except ValueError as e:
    print(e)
    print("enter only numbers")
except Exception as e:
    print(e)
    print("something went wrong:(")
else:
    print(result)
finally:
    print("this will always execute")


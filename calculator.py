x=int(input("Enter first number: "))
y=int(input("Enter second number: "))
print("1: Add \n \
       2: Subtract \n \
       3: Multiply \n \
       4: Divide \n")
choice = int(input("Enter your choice: "))
if choice == 1:
    print("Result: ", x+y)
elif choice == 2:
    print("Result: ", x-y)
elif choice == 3:
    print("Result: ", x*y)
elif choice == 4:
    print("Result: ", x/y)
else:
    print("Invalid choice")
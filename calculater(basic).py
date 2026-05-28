num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))
print("What do u want to do with these numbers?")
print("Enter +(add),-(subtract),*(multiply),/(divide))")
op=input("Enter the operator: ")
if op=='+':
    print(f"The sum of both the entered numbers is {num1+num2}.")
elif op=='-':
    print(f"The difference of both the entered numbers is {num1-num2}.")
elif op=='*':
    print(f"The product of both the entered numbers is {num1*num2}.")
elif op=='/':
    print(f"The division of first number by second number gives the result {num1/num2}.")
else:
    print("Invalid Option.")
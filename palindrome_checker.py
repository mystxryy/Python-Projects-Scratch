str1=input("Enter a string for palindrome check: ")
if str1==str1[::-1]:
    print(f"The string {str1} is a palindrome.")
else:
    print(f"The string {str1} is not a palindrome.")
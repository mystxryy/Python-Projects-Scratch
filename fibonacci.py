print()
print("=" * 50)
print("      Nth TERM IN FIBONACCI SERIES")
print("=" * 50)
print()
def fibonacci(num):
    p = 0
    q = 1
    
    if num < 0:
        print("Incorrect input")
        
    elif num == 0:
        return 0
      
    elif num == 1:
        return q
    else:
        for i in range(1, num):
            r = p + q
            p = q
            q = r
        return q

num=int(input("Enter the N: "))
print(fibonacci(num))

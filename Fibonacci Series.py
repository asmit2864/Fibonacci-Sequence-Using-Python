def fibonacci(n):
    if n<=1:
        return n
    else:
        return (fibonacci(n-1)+fibonacci(n-2))
terms=int(input("Enter the number of terms of fibonacci series: "))
if terms<=0:
    print("Ivalid input")
else:
    print("FIBONACCI SERIES IS:")
for i in range(terms):
    print(fibonacci(i))

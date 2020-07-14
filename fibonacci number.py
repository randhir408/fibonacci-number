def fibonacci(n1,n2,n):
    if n==0:
        return
    result=n1+n2
    print(result,end=",")
    fibonacci(n2,result,n-1)
a=1
b=2
n=int(input("Entered how many number are to be printed="))
print(a,end=",")
print(b,end=",")
fibonacci(a,b,n-2)
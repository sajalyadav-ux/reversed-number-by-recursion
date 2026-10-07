def reversed(n,rev=0):
    if n==0:
        return rev
    digit=n%10
    rev=rev*10+digit
    return reversed(n//10,rev)
num=int(input("enter the number :"))
result=reversed(num)
if result==num:
    print("This is palindrom :",result)
else:
    print("This is not palindrome:",result)

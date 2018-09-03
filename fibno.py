nterms = int(input('Enter the number of fibonacci Numbers you want to print -->  '))
n1 = 0
n2 = 1
count = 0
L1 = []


if (nterms <= 0):
    print("Please enter a positive integer")
elif nterms == 1:
    print("Fibonacci sequence upto",nterms,":")
    print(n1)
else:
    print("Fibonacci sequence upto",nterms,":")
    while count < nterms:
        L1.append(n1)
        print(' ',n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1
L2=[]

t = max(L1)
for i in range (1,t + 1):
    if i not in L1:
        L2.append(i)
        i = i + 1

print(L2)
print(len(L2))


def fib(a):
    if ( a == 1 or a ==2 ):
        return 1
    else:
        return((fib(a-1) + fib(a-2)))
    
    
print(fib(9))
        
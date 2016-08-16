
def dupli(A):
    temp=[]
    for i in range(len(A)-1):
        if(A[i]!=A[i+1]):
            temp.append(A[i])
    temp.append(A[len(A)-1])    
            
    return temp

#print(dupli([5,5,5,5,6,10,7,5]) )           
            
def prime(n):
    l=[]
    for i in range(2,n+1):
        for num in range(2,i):
            if i % num==0:
                break
                
            l.append(num)
            
    return l
            
#print(prime(5))  
def fib1(n):
    l=[0,1]
    i=1
    num = l[i]
    while True:
        if num>=n:
            return l
        else:
            l.append(l[i]+l[i-1])
            i+=1
            num=l[i]
    
#print(fib1(50))

def fib(n): 
    myList=[]
    a, b = 0, 1
    while a < n:
        myList.append(a)
        a, b = b, a+b
    return myList
    
#print(fib(2000))

def primeGenerator(k):
    myList=[]
    for n in range(2, k+1):
        for x in range(2, n):
            if n % x == 0:
                break
        else:
            myList.append(n)

    return myList
print(primeGenerator(23))


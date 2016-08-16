
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
    
print(fib1(50))

def fib(n):    # write Fibonacci series up to n
     """Print a Fibonacci series up to n."""
     a, b = 0, 1
     while a < n:
         print(a, end=' ')
        a, b = b, a+b
    print()
    
    fib(2000)

        

'''
def find_missing(list1,list2):
    if not list1 and not list2: return 0
    if(list1==list2): return 0
    if(len(list1)>len(list2)):
        setdiff=set(list1)-set(list2)
    elif (len(list2)>len(list1)):
        setdiff=set(list2)-set(list1)
    else:
        return 0
        
    return list(setdiff)[0]

'''
class PrimeChecker(object):
    
    def __init__(self, number=''):
        self.number=number
    def is_prime(self):
        if not self.number:
            return False
        else:
            self.number=int(self.number)
            if self.number < 2:
                return False
            elif self.number==2 or self.number==3:
                return True
            else:
                for i in range(2,self.number//2):
                    if self.number%i==0:
                        return False
                return True
            

class test(object):
    pass
#kata data type lap python
def data_type(arg):
    if isinstance(arg,str): 
        return len(arg)
    elif arg is None:
        return 'no value'
    elif isinstance(arg,bool): 
        return arg 
    elif isinstance(arg,int):
        if arg<100:
            return 'less than 100'
        elif arg==100: 
            return 'equal to 100'
        else: 
            return 'more than 100'
    elif isinstance(arg,list):
        if len(arg)>=3:
            return arg[2]
        return None
#fizz buzz   
def fizz_buzz(num):
    if num%15==0:
        return "FizzBuzz"
    elif num%5==0:
        return "Buzz"
    elif num%3==0:
        return "Fizz"
    else:
        return num

    
#reverse string
def reverse_string(string):
    if not string:
        return None
    reversed_string=string[::-1]
    if reversed_string==string:
        return True
    return reversed_string


#factorial lab
def factorial(number):
    product=1
    for num in range(1,number+1):
        product*=num
    return product
        
    
print(factorial(5))
print(factorial(10))


    


    
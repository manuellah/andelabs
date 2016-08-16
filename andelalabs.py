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
class PrimeChecker:
    
    def __init__(self,number):
        self.number=int(number)
    def is_prime(self):
        for i in range(2,self.number+1):
            print('loop 1')
            for num in range(2,i):
                print('loop 2')
                if i % num==0:
                    print(i,m)
                    return False
            else:
                return True
'''           
obj=PrimeChecker('34')
print(obj.is_prime())
'''  
def string_length(*my_args)
    print(args)
    
string_length(['Adam', 'Frankel'])


                

            
 
        


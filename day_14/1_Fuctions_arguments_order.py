#functions arguments  has a certain order in python.Following is the order of arguments :

#1.Positional
#2.Default / Keyword
#3.*args
#4.**kwargs

def addition (a,b,c=1,d=2,*args,**kwargs): # order of arguments  in functions definition
    print(a)
    print(b)
    print(c)
    print(d)
    print(args)
    print(kwargs)
    return a+b+c+d+sum(args)+sum(kwargs.values())





result=addition(1,2,3,4,5,6,7,8,p=9,q=10)
print("The sum of all is:",result)



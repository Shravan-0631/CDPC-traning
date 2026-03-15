# def add():
#     a=int(input('Enter number:'))
#     b=int(input('Enter number:'))
#     res=a+b
#     print(res)
# if __name__=='__main__':
#     add()

#output
# Enter number:66
# Enter number:77
# 143






# def add(x,y):
    
#     res=x+y
#     print(res)
# if __name__=='__main__':
#     a=int(input('Enter number:'))
#     b=int(input('Enter number:'))
#     add(a,b)
    
#     #output
#     # Enter number:22
# Enter number:22
# 44




# def add(x,y):
#     res=x+y
#     return res
   
# if __name__=='__main__':
#     a=int(input('Enter number:'))
#     b=int(input('Enter number:'))
#     res=add(a,b)
#     print(res)
    
    #     #output
#     # Enter number:22
# Enter number:22
# 44



def add(x,y):
    res1=x+y
    res2=x+y
    res3=x+y
    return res1,res2,res3
   
if __name__=='__main__':
    a=int(input('Enter number:'))
    b=int(input('Enter number:'))
    r1,r2,r3=add(a,b)
    print(r1,r2,r3)
    


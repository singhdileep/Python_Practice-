
""" # Reverse String 

s="My name is Vivek"
l=s.split()
l1=[]
i=len(l)-1
while i>=0:
    l1.append(l[i])
    i=i-1
output=' '.join(l1)
print(output)   """

""" #input: Durga Software Solutions
#output:agruD erawtfoS snoituloS

s=input("Enter the string :")
l=s.split()
l1=[]
i=0
while i<len(l):
    l1.append(l[i][::-1])
    i=i+1
output=' '.join(l1)
print(output)
"""

"""  Program to merge characters of 2 strings into a single string by taking characters
alternatively.
s1="ravi"
s2="reja"
output: rtaevjia
 

s1="dileep"
s2="singh"
i,j=0,0
output=''
while i<len(s1) or j<len(s2):
    if i<len(s1):
        output=output+s1[i]
        i=i+1
    if j<len(s2):
        output=output+s2[j]
        j=j+1
print(output)           
"""

""" Write a program to sort the characters of the string and first alphabet symbols
followed by numeric values
input: B4A1D3
Output: ABD134

 

s=input("Enter the String :")
s1=s2=output=''
for i in  s:
    if i.isalpha():
        s1=s1+i
    else:
        s2=s2+i 
for i in sorted(s1):
    output=output+i
for i in sorted(s2):
    output=output+i
print(output)                   

"""






""" s=input("Enter the string ")
l=len(s)-1
rev=''
for i in range(l,-1,-1):
    rev=rev+s[i]
print(rev)
 """













""" n=80
l=[]
for i in range(1,n+1):
    if n%i==0:
        l.append(i)
print(l)

l.remove(1) """

""" # Find the sum of prime factor of any number

n=99
l1=[]
l2=[]
sum=0
for k in range(1,n+1):
    if n%k==0:
        l1.append(k)
for i in l1:
    if i>=1:
        for j in range(2,i):
            if (i%j)==0:
                 break
        else:
            l2.append(i)
l2.remove(1)
for a in range(0,len(l2)):
    sum=sum+l2[a]
print(sum)    """


""" l=[1,3,4,5,6]
sum=0
for i in range(0,len(l)):
    sum=sum+l[i]
print(sum)
 """




"""# lCM of two number
a=2
b=4
if a>b:
    max=a
    min=b
else:
    max=b
    min=a
for i in range(1,min+1):
    x=max*i
    if x%min==0:
        lcm=x
        break 
print(lcm)       
 """




""" def gcd(a,b):
    Compute the greatest common divisor of a and b
    while b > 0:
        a, b = b, a % b
    return a
    
def lcm(a, b)
    Compute the lowest common multiple of a and b
    return a * b / gcd(a, b)
a=8
b=4
print(lcm(a,b)) """




""" from math import gcd
a = [2,4,]   #will work for an int array of any length
lcm = a[0]
for i in a[1:]:
  lcm = int(lcm*i/gcd(lcm, i))
print(lcm)
 """


#  Remove repeated alphabet
""" s=input("Enter the string: ")
l=[]
for i in s:
    if i not in l:
        l.append(i)
    a=''.join(l)
print(a) """       
 


""" s1="my name is dileep"
s2="my name is raj"
l1=s1.split()
l2=s2.split()
l=[]
result=[i for i in l1 if i not in l2]+\
    [i for i in l2 if i not in l1]


print(', '.join(result))    
 """





""" s1="My name is dileep"
s2="My name is raj"
    string = "big black bug bit a big black dog on his big black nose";  
       
    #Converts the string into lowercase  
    string = string.lower();  
       
    #Split the string into words using built-in function  
    words = string.split(" ");  
       
    print("Duplicate words in a given string : ");  
    for i in range(0, len(words)):  
        count = 1;  
        for j in range(i+1, len(words)):  
            if(words[i] == (words[j])):  
                count = count + 1;  
                #Set words[j] to 0 to avoid printing visited word  
                words[j] = "0";  
                  
        #Displays the duplicate word if count is greater than 1  
        if(count > 1 and words[i] != "0"):  
            print(words[i]);  





 """



""" Write a program for the following requirement
input: a4b3c2
output: aaaabbbcc
 

s=input("Enter the string :")
output=''
for x in s:
    if x.isalpha():
        output=output+x
        previous=x
    else:
        output=output+previous*(int(x)-1)
print(output)  
""" 

""" s=input("enter the string :")
output=''
for x in s:
    if x.isalpha():
        output=output+x
        previous=x
    else:
        output=output+chr(ord(previous)+int(x))
print(output)      
     """

"""

s=input("Enterthe string :")
d={}
for x in s:
    if x in d.keys():
        d[x]=d[x]+1
    else:
        d[x]=1
for k,v in d.items():
    print("{}={}".format(k,v))            

"""

""" s=input("Enter the string :")
l=[]
for i in s:
    l.append(i)
d={x:l.count(x) for x in l}
print(d) """

""" s=input("Enter the string :")
rev=''
l=len(s)-1
for i in range(l,-1,-1):
    rev=rev+s[i]
print(rev) """

""" s=input("enter the string :")
print(s[::-1])
 """

""" l=[1,2,3,4,5,7,8,910,45]
l.sort()
print(l[::-1]) """




""" string = input('Type your numbers, separated by a space')
numbers = [int(i) for i in string.strip().split(' ')]
numbers.sort()     #an optional reverse argument possible
print(numbers) """

""" l=[1,2,3,4,5]
l.sort()
a=[]
b=[]
c=[]
x=l[len(l)//2]
l.remove(l[len(l)//2])
for i in range(len(l)//2):
    a.append(l[i])
    b.append(l[len(l)-i-1])
for i in range(len(b)):
    c.append(b[i])
    c.append(a[i]) 
c.append(x)   
print(c) """







""" a=[1,2,3,4,6,5,7]
a.sort()
n=len(a)
largest=a[n-1]+1
min=0
max=n-1
for i in range(n):
    if i%2==0:
        a[i]=(a[max]%largest)*largest+a[i]
        max=max-1
    else:
        a[i]=(a[min]%largest)*largest+a[i]
        min=min+1
for i in range(n):
    a[i]=a[i]//largest
print(a)                 
 """


""" s="My name is dileep."
l1=[]
l=s.split()
for i in range(len(l)):
    l1.append(l[i][::-1])
output=' '.join(l1)    
print(output)    
print(l[::-1])
print(type(l)) """


# l=[[1,2,3,4,5,6],[3,4,5,6,78,9],[0,5,6,7,8,9]]
# for i in range(len(l)):
#     for j in range(len(l[i])):
#         print(l[i][j],end=' ')
#     print() 


""" s=[x*x for x in range(1,11)]
m=[x for x in s if x%2==0]
print(m)    
 """



# s=[10,20,30,40,40,40,60]
# l=[]
# for i in s:
#     if i not in l:
#         l.append(i)
# print(l) 




""" s=input("Enter the string :")
l=set(s)
v={'a','e','i','o','u'}
d=l.intersection(v)
for i in d:
    l.remove(i)
print(''.join(l))
print(d)
 """


""" i=int(input("Enter ur number :"))
l=[]
if i!=0:
    l.append(i)
else:
    print(l)     """


""" #print("inut the cal")
count=0
sum=0
n=1
while n!=0:
    n=int(input("Enter the no :"))
    sum=sum+n
    count=count+1
if count==0:
    print("enter some no:")
else:
    print("sum of the no :",sum) """




    #   function


""" def wish(name):
    print("hello",name,"Good morning")
wish("dileep")
wish("raj")
wish("1")
print(wish("dileep"))
         """
""" import random
l=[1,3,4,5,6,7,8]
random.shuffle(l)
print(l) """


""" import os
os.chdir("C:\\Users\\singhdileep\\Desktop\\python")
f=open('test.txt')
f
type(f)
print(f.read())
print(ord('a'))
print(chr(65))
l=[5,7,8]
s=sum(l)
print(s) """



# Functions

""" def sqt(n):
    print("The square of the",n,"is :",n*n)
sqt(4)
 """

""" def add(x,y):
    return x+y
print(add(2,4))
     """

""" def f1():
    print("hello")
f1()
print(f1())          """

""" def even_odd():
    n=int(input("Enter the no :"))
    if n%2==0:
        print(n," : is even")
    else:
        print(n,": is odd")
even_odd()            
 """


""" def fact():
    f=1
    n=int(input("Enter theno :"))
    for i in range(1,n+1):
        f=f*i
    print(f)
fact()        """ 


""" def sum_sub():
    a=int(input())
    b=int(input())
    sum=a+b
    sub=a-b
    return sum,sub
print(sum_sub())     """

""" def cal(a,b):
    sum=a+b
    sub=a-b
    mul=a*b
    div=a/b
    return sum,sub,mul,div
t=cal(100,5)
    print(t) """


""" a=111
def f1():
    a=10
    print(a)
    print(globals()['a'])

def f2():
    print(a)
f1()
f2() """

""" def fact(n):
    if n==0:
        result=1
    else:
        result=n*fact(n-1)
    return result
print(fact(4))
    """

""" def sqt(x):
    return 2*x
l=list(map(sqt,[1,2,3,4,5]))    
print(l)    
 """


""" a=[1,2,3,4,5]
b=[2,9,5,6,6]
l=list(map(lambda x,y:x*y*2,a,b))
print(l) """ 

""" from functools import *
a=[10,30,3]
l=reduce(lambda x,y:x/y,a)
print(l)

 """

""" def f1(name):
    print("My name is dileep singh ",name)
dileep=f1
print(id(f1))
print(id(dileep))    
f1("dileep singh")
dileep("dileep singh")
del dileep
dileep("sonu")
 """


""" t=[1,2,3,4,5]
t1=[2,4,5,6,8]
t.update(t1)
print(t) """



""" def sumArray(arr, n): 
  
    i, temp = 0, 0
    Sum = [0 for i in range(n)] 
    for i in range(n): 
        Sum[i] = temp 
        temp= temp+arr[i] 
    temp = 0
    for i in range(n - 1, -1, -1): 
        Sum[i]=Sum[i]+ temp 
        temp =temp+arr[i] 
      
    for i in range(n): 
        print(Sum[i], end = " ") 
arr = [ 3, 6, 4, 8, 9 ] 
n = len(arr) 
sumArray(arr, n) 
   """




""" arr = [1,2,3,4,5,6 ]
n=len(arr)
i, temp = 0, 0
Sum = [i for i in range(n)] 
for i in range(n): 
    Sum[i] = temp 
    temp= temp+arr[i] 
temp = 0
for i in range(n - 1, -1, -1): 
    Sum[i]=Sum[i]+ temp 
    temp =temp+arr[i] 
for i in range(n): 
    print(Sum[i], end = ' ') 
  """

""" s1 = "my name is raj"
s2 = "my name is dileep"
r=[]
l1=s1.split()
l2=s2.split()
print(l1)
for i in range(0,len(l1)):
    for j in range(0,len(l2)):
        if l1[i]!=l2[j]:
            r=l1[i]+l2[j]
        print(r)     """

# l=[1,2,3,4,5]
# sum=0
# l1=[]
# for i in range(0,len(l)):
#     sum=sum+l[i]
# for i in range(0,len(l)):
#     l[i]=sum-l[i]
#     l1.append(l[i])    
# print(l1)   
  

# What is the difference between the sum of the squares and the square of the sums.
# n=5
# sum=0
# for i in range(0,n+1):
#     s=i*i
#     sum=sum+i
#     p=sum*sum

# print(s)
# print(sum)
# print(p)
# print(p-s) 





# l= [1,3,4,5,67,8]
# m=0
# for i in l:
#     if i>m:
#         m=i
# print(m)    



# d={1:[1234],"a":"abc","c":12345}
# d[1].append(333)
# print(d)


# s="Dileep kumar Singh"
# print(s[-1:-5:-3])

# a=10+5j
# b=10+3j
# print(a is b)

# d={(1,2):[1,2,33],'A':'BCC'}
# for i in d.keys():
#     if i==1:
#         d[i].append(20202)
# print(d[(1,2)])        

# d=chr(97)
# print(d)
# print(ord('a'))



# def reverse(self, x):
#     x = str(x)
#     if x[0] == '-':
#         a = int('-' + x[-1:0:-1])
#         if a >= -2147483648 and a<= 2147483647:
#             return 
#          else:
#             return 0
#          else:
#             a = int(x[::-1])
#             if a >= -2147483648 and a<= 2147483647:
#                return a
#             else:
#                return 0
# print(ob1.reverse(-425))


# a=-120
# s=str(-a)
# print(-int(s[::-1]))


# a="dileep"
# b=-3
# print(a*b)

''' find the max of the given 2 and three number */ '''

# n1=int(input("Enter the first number :"))
# n2=int(input("Enter the second number :"))
# n3=int(input("Enter the Third number :"))
# max=n1 if n1>n2 and n1>n3 else n2 if n2>n3 else n3
# print("The max of Number is :",max)


# def max_Number(a,b,c):
#     max=a if a>b and a>c else b if b>c else c
#     return max
# print(max_Number(20,10,5))
   
''' Write a program to read 3 int numbers from the keyboard with , seperator and print'''

# a,b,c=[int(x) for x in input("Enter the number :").split()]
# print("The sum of the given number :",a+b+c)

# x=eval(input("Enter the number "))
# print(sum(x))




'''Program to display command line Argumnet'''

# from sys import argv
# print("The number of Argumnets:",len(argv))
# print("The list of command line Argumnets:",argv)
# print("The command line argunment one by one :")
# for i in argv:
#     print(i)

'''Program to print the multiplication of the given command argunment'''

# from sys import argv
# mul=1
# argvs=argv[1:]
# for x in argvs:
#     n=int(x)
#     mul=mul*n
# print(mul)


'''Q. Write a program to find smallest of given 2 numbers'''

# a=int(input("Enter first number: "))
# b=int(input("Enter second number: "))
# min=a if a<b else b
# print(min)

'''Q. Write a program to check whether the given number is even or odd'''


# n=int(input("Enter any number :"))
# if n%2==0:
#     print("It is even Number ")
# else:    
#     print("It is odd Number ")


'''Q. Write a program to check whether the given number is in between 1 and 100?'''

# n=int(input("Enter any Number :"))
# if n>=1 and n<=100:
#     print("The Number",n,"is between 1- 100")
# else:
#     print("The number",n,"is not in between 1 to 100")   


'''Q. Write a program to print the string with index '''

# s=input("Enter any string :")
# i=0
# for x in s:
#     print("The character present at ",i,"index is :",x)
#     i=i+1

'''print pyrimid '''

# n=input("Enter any Number:")
# for i in range(1,int(n)+1):
#     print(" " * (int(n)-i),end="")
#     print("* "*i)







# '''''''''''''''''''''''''''''''''''''


# number=[10,33,0,40,0,50,9,0]
# for n in number:
#     if n==0:
#         print("Hey how we can divide with zero..just skipping")
#         continue
#     print("100/{} = {}".format(n,100/n))




# cart=[20,330,400,600,40,50]
# for item in cart:
#     if item>500:
#         print("Item to be placed")
#         break
#     print(item)



# name=""
# while name!="dileep":
#     name=input("Enter Name:")
# print("Thanks for confirmation")    








# n=int(input("Enter the number :"))
# i=1
# sum=0
# while i<=10:
#     sum=sum+i
#     i=i+1
# print("Sum is :",sum)    



''''''

# print("The Sum:",int(input("Enter First Number:"))+int(input("Enter Second Number:")))  



s="Dileep"
print(s)
s=None
print(s)
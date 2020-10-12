'''To print prime number '''

# for num in range(1,100):
#     if num>1:
#         for i in range(2,num):
#             if num%i==0:
#                 break
#         else:
#                 print(num)


# for i in range(101):
#     for j in range(2,i-1):
#         if i%j==0: break
#     else:
#         print (i)



# n=int(input("Enter any Number :"))
# if n>1:
#     for i in range(2,n):
#         if n%i==0:
#             print(n,"is Not a prime Number")
#             break
#     else:
#         print(n,"is a prime Number")
# else:
#     print(n,"is not aprime number")        

'''Check the give number is prime or not '''


# n=int(input("Enter any Number :"))
# count=0
# for i in range(1,n+1):
#     if n%i==0:
#         count=count+1
# if count==2:
#     print("It is prime Number")
# else:
#     print("It is not a Prime Number")    

'''Print prime till the range '''


# count=0
# for i in range(1,100):
#     count=0
#     for j in range(1,i+1):
#         if i%j==0:
#             count=count+1
#     if count==2:
#         print(i)                


# for i in range(101):
#     for j in range(2,i-1):
#         if i%j==0: break
#     else:
#         print (i)




'''Factorial program using recursion '''


# def fact(n):
#     if n==0:
#         return 1
#     else:
#         return n*fact(n-1)
# n=int(input("Enter any Number to for factorial :"))
# result=fact(n)
# print(result)  

# def fact(n):
#     return 1 if (n==0 or n==1) else n*fact(n-1)
# print(fact(5))              


'''Fibonacci Series '''

# n=int(input("Enter the Number of series :"))
# f=0
# l=1
# print(f)
# print(l)
# for i in range(2,n):
#     fab=f+l
#     print(fab)
#     f=l
#     l=fab


'''To check leap year or not '''


# year=int(input("Enter the Year :"))
# if(year%4==0 and year%100!=0 or year%400==0):
#     print("It is a leap Year")
# else:
#     print("It is not a leap year")   


# year = int(input("Please Enter the Year: "))
# if(year%4 == 0):
#     if(year%100 == 0):
#         if(year%400 == 0):
#             print("%d is a Leap Year" %year)
#         else:
#             print("%d is Not the Leap Year" %year)
#     else:
#         print("%d is a Leap Year" %year)
# else:
#     print("%d is Not the Leap Year" %year)

  


'''Check any Number is plaindrome or Not'''

# n=int(input("Enter any Number "))
# palin=0
# t=n
# while n>0:
#     r=n%10
#     palin=palin*10+r
#     n=n//10
# if t==palin:
#     print("It is palindrome Number")
# else:
#     print("It is not palindrome Number")   


'''check the given Number is armstrong '''

# n=int(input("Enter any Number :"))
# d=len(str(n))
# temp=n
# arm=0
# while n>0:
#     r=n%10
#     arm=arm+r**d
#     n=n//10
# if temp==arm:
#     print("It is Armstrong Number ")
# else:
#     print("It is not a Armstrong Number")  


'''Code to print armstrong of a give range'''

# for i in range(1,1000000):
#     d=len(str(i))
#     temp=i
#     arm=0
#     while i>0:
#         r=i%10
#         arm=arm+r**d
#         i=i//10
#     if temp==arm:
#         print(arm)    


'''Digital sum and digital Multiplication'''

# n=int(input("Enter any Number: "))
# temp=n
# sum=0
# while n>0:
#     r=n%10
#     n=n//10
#     sum=sum+r
# print(sum)
    

''' String plaindrome '''

# s="abCbba"
# s=s.lower()
# r=reversed(s)
# if list(s)==list(r):
#     print("It is plaindrome String")
# else:
#     print("It is not palinfrome String")    


'''Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.
   The string will only contain lowercase characters a-z.
'''

# s = 'janj'
# def solution(s):
#     for i in range(len(s)):
#         t = s[:i] + s[i+1:]
#         if t == t[::-1]: 
#             return True
#     return s == s[::-1]
# print(solution(s))



# l=[(1,3),(3,1),(5,0),(3,2)]
# l.sort(key=lambda x:x[1])
# print(l)


# def A(*args,**kwrgs):
#    print(type(args),type(kwrgs))

# print(A(1,2))
# print(A(x=1))
# print(A(1,x=1))   



# class A:
#    pass
# class B(A):
#    pass

# l=[1,2,3,'@','None',[],{}]
# l1=[]
# for i in l:
#    if type(i)==int:
#       l1.append(i)
# print(l1)      




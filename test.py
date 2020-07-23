
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
#     cn=i
#     count=0
#     for j in range(1,cn+1):
#         if cn%j==0:
#             count=count+1
#     if count==2:
#         print(cn)                


# for i in range(101):
#     for j in range(2,i-1):
#         if i%j==0: break
#     else:
#         print (i)


'''To check leap year or not '''


# year=int(input("Enter the Year :"))
# if(year%4==0 and year%100!=0 or year%400==0):
#     print("It is a leap Year")
# else:
#     print("It is not a leap year")    



'''Check the give Number is palindrome or not '''

# n=int(input("Enter any Number :"))
# temp=n
# palin=0
# while n>0:
#     r=n%10
#     palin=palin*10+r
#     n=n//10
# if temp==palin:
#     print("It is Plaindrome Number ")
# else:
#     print("It is not a Plaindrome Number")        


'''check and print the armstrong of a given range'''

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
      


# for n in range(1000):
#     d=len(str(n))
#     temp=n
#     arm=0
#     while n>0:
#         r=n%10
#         arm=arm+r**d
#         n=n//10
#     if temp==arm:
#         print(arm)


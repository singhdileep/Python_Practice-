
'''Code to check the give number is spy number.'''

# for n in range(1000):
    # d=len(str(n))
# n=int(input("Enter any Number:"))    
# a=0
# p=1
# while n>0:
#     r=n%10
#     a=a+r
#     p=p*r
#     n=n//10
# if a==p:
#     print("this number is spy number")
# else:
#     print("This number is not a spy Number")    


'''Convert nested list into flated list using function '''


# l=[1,2,[3,4,5,[4,6,[2]]]]
# l1=[]
# def sublist(l):
#     for i in l:
#         if type(i)==list:
#             sublist(i)
#         else:
#             l1.append(i)
# sublist(l)              
# print(l1)              





# l=[1,2,3,4,5,6,7,8,9,10]
# a=[]
# b=[]
# c=[]
# x=l[len(l)//2]
# l.remove(l[len(l)//2])
# for i in range(len(l)//2):
#     a.append(l[i])
#     b.append(l[len(l)-i-1])
# for i in range(len(b)):
#     c.append(b[i])
#     c.append(a[i]) 
# c.append(x)   
# print(c) 

'''Change the position of the list '''

# def change_pos(my_list):
#     for i in range(0,len(l),2):
#         l[i],l[i+1]=l[i+1],l[i]
#         return l
# l=[0,1,2,3,4,5]
# print(change_pos(l))


# l=[0,1,2,3,4,5]
# for i in range(0,len(l),2):
#     l[i],l[i+1]=l[i+1],l[i]
# print(l)    


''' Python program to right rotate a list by n '''


# l=[1,2,3,4,5,6,7,8,9,10]
# l1=[]
# n=3
# for i in range(len(l)-1,len(l)-n-1,-1):
#     l1.append(l[i])
# for i in range(0,n):
#     l1.append(l[i]) 
# print(l1)       


# n = 2
# list_1 = [1, 2, 3, 4, 5, 6,7,8,9,10] 
# list_1 = (list_1[-n:] + list_1[:-n]) 
# print(list_1) 





'''find nth fibonacci series'''

# def fib(n):
#     if n<0:
#         print("Incorrect Input")
#     elif n==1:
#         return 0
#     elif n==2:
#         return 1
#     else:
#         return fib(n-1)+fib(n-2)
# print(fib(9)) 
                 

# n=int(input("Enter any Number:"))
# f,l=0,1
# print(f)'
# print(l)
# for i in range(2,n):
#     next=f+l
#     print(next)
#     f,l=l,next


# def fib(n):
#     if n<0:
#         print("Incorrect Input")
#     elif n==1:
#         return [0]
#     elif n==2:
#         return [0,1]
#     else:
#         x = fib(n-1)
#         x.append(sum(x[:-3:-1]))
#         return x
# x=fib(10)
# print(x)



# def fibo(n):  
#    if n <= 1:  
#        return n  
#    else:  
#        return(fibo(n-1) + fibo(n-2))  
# n = int(input("How many terms? "))  
# if n <= 0:  
#    print("Plese enter a positive integer")  
# else:  
#    print("Fibonacci sequence:")  
#    for i in range(n):  
#        print(fibo(i),end=',')  



# n=int(input("Enter the number: "))
# c=0
# a=1
# b=1
# if n==0 or n==1:
#     print("It is a fibonacci Number")
# else:
#     while c<n:
#         c=a+b
#         b=a
#         a=c
#     if c==n:
#         print("It is a fibonacci Number")
#     else:
#         print("It is not a fibonacci Number")




# l=[1,2,3,4,4,4,5,6,7,89,7,7,78,77]
# d={}
# for i in l:
#     if i in d:
#         d[i]=d.get(i,0)+1
#     else:
#         d[i]=1
# print(d)    


# s="My name is dileep Kumar my name is dileep singh."
# s1=s.split()
# d={}
# for i in s1:
#     if i in d:
#         d[i]=d.get(i,0)+1
#     else:
#         d[i]=1
# print(d)            


# l=[1,2,3]
# l+='de'
# print(l)



# def findMinimumDeletion(l, r, dp, s): 
  
#     if l > r: 
#         return 0
#     if l == r: 
#         return 1
#     if dp[l][r] != -1: 
#         return dp[l][r] 
  
#     # When a single character is deleted 
#     res = 1 + findMinimumDeletion(l + 1, r,dp, s) 
#     for i in range(l + 1, r + 1):  
#         if s[l] == s[i]: 
#             res = min(res, findMinimumDeletion(l + 1, i - 1, dp, s) +
#                            findMinimumDeletion(i, r, dp, s)) 
#     dp[l][r] = res 
#     return res 
# if __name__ == "__main__": 
  
#     s = "aabb"
#     n = len(s) 
#     N = 10
#     dp = [[-1 for i in range(N)]  
#               for j in range(N)] 
#     print(findMinimumDeletion(0, n - 1, dp, s)) 
  
# # This code is contributed by Rituraj Jain 





# def linearsearch(arr, x):
#    for i in range(len(arr)):
#       if arr[i] == x:
#          return i
#    return -1
# arr = ['t','u','t','o','r','i','a','l']
# x = 'a'
# print("element found at index "+str(linearsearch(arr,x)))

# l1=[]
# l=[1,2,4,22,4,3]
# for i in l:  
#     l1.append(i+1)
# print(l1)


# x = [[1,2,3,4],[4,5,6]]
# y=[[z+1 for z in y] for y in x]
# print(y)

# test_data = [
#     [1,2,3]
#     ,[2,4]
#     ,5
#     ,[6,7,[8,9]]
#     ]

# import types
# import numbers

# def inc_el(list_or_num):
#     if isinstance(list_or_num, numbers.Number):
#         return list_or_num +1
#     elif type(list_or_num) == types.ListType:
#         return (map(inc_el, list_or_num))
# print (map(inc_el, test_data))


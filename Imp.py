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



# s="dileep singh"
# s1=''.join([i for i in s if i not in ('a','e','i','o','u')])
# print(s1)

# s="dileep singh"
# l=[]
# for i in s:
#    if i not in ('a','e','i','o','u'):
#       l.append(i)
# print("".join(l))      


# t=(1,2,3,[1,2,3])
# t[3].append(4)
# print(t)

# l=[1,2,3,(1,2,3)]
# l[3][0]=80
# print(l)



'''Nutanix qst  Reverse string '''

# def rev_words(s):
#    s1=s.strip().split()
#    output=""
#    for i in s1:
#       if i[0].isupper() and len(i)>1:
#          s2=i[::-1]
#          l=list(s2)
#          l[0]=l[0].upper()
#          # print(l)
#          l[-1]=l[-1].lower()
#          # print(l)
#          s2="".join(l)
#          output=output+" "+s2.strip()
#       else:
#          output=output+" "+i[::-1]
#    output=output.strip()
#    return output
# print(rev_words("I work at Nutanix  ") ) 


# def find_longest_word(word_list):  
#    longest_word = ''  
#    longest_size = 0   
#    for word in word_list:    
#       if len(word) > longest_size
#          longest_word = word
#          longest_size = len(word)      
#    return longest_word

# words = input('Please enter a few words')  
# word_list = words.split()  
# find_longest_word(word_list)  


# def longestWord(words):
#    ans = ""
#    wordset = set(words)
#    for word in words:
#       if len(word) > len(ans) or len(word) == len(ans) and word < ans:
#          if all(word[:k] in wordset for k in range(1, len(word))):
#             ans = word
#    return ans
# print(longestWord("this is dileep here"))


# def solution(S, D):
#    D.sort(key=len, reverse=True)
#    found = False
#    for word in D:
#       i = 0
#       for ch in word:
#          n = S.find(ch,i)
#          if n is not -1:
#             found = True
#             i = n + 1
#          else:
#             found = False
#             break
#          if found:
#             return word
#    return -1

# a_string = "abppplee"
# words = ["able", "ale", "apple", "bale", "kangaroo","appple","applee"]

# result = solution(a_string, words)
# print(result)


# def subsetsum(array,num):
#    if num == 0 or num < 1:
#       return None
#    elif len(array) == 0:
#       return None
#    else:
#       if array[0] == num:
#          return [array[0]]
#       else:
#          with_v = subsetsum(array[1:],(num - array[0])) 
#          if with_v:
#             return [array[0]] + with_v
#          else:
#             return subsetsum(array[1:],num)
# array=[1,2,3,4,6,10,5,8]
# num=10
# print(subsetsum(array,num))


# def findSubSeq(arr, n, sum) :  
#    for i in range(n - 1, -1, -1):  
#       if (sum < arr[i]) : 
#          arr[i] = -1  
#       else : 
#          sum =sum - arr[i]  
#    for i in range(n) : 
#       if (arr[i] != -1) : 
#          print(arr[i], end = " ") 
# arr = [ 1,2,3,4,5,6,10,8 ]
# n = len(arr);  
# sum = 10;  
# findSubSeq(arr, n, sum)
  
''' Print all subsequences '''
# l=[]
# a= [1,23,4,5,6,2,8,10]
# for i in range(0,len(a)): 
#    for j in range(i+1,len(a)):
#       for k in range(j+1,len(a)): 
#          v=a[i],a[j],a[k]
#          l.append(v)
# print (l) 

# def sub_lists (l): 
#     l1 = []   
#     lists = [l1] 
#     for i in range(len(l)): 
#         orig = lists[:] 
#         new = l[i] 
#         for j in range(len(lists)): 
#             lists[j] = lists[j] + [new] 
#         lists = orig + lists 
          
#     return lists
#     lists.pop(0)
 
  
# driver code 
l1 = [1, 2, 3] 
print(sub_lists(l1)) 



 


# # Driver program 
# arr = [1, 2, 3, 4] 
# n = len(arr) 
# print ("All Non-empty Subarrays") 
  
# subArray(arr, n); 


# t=(1,2,3,4,4,5)
# t1=list(t)
# t1.remove(2)
# t2=tuple(t1)
# print(t2)


# l=[1,2,3,44,55,6,7,8]
# max=0
# for i in l:
#    if i>max:
#       max=i
# print(max)      

# # print(max)

# n=int(input("Enter any number:"))
# if n>=1 and n<=100:
#    print("The given number is between 1 to 100")
# else:
#    print("The given Number is not between 1 to 100")   

# s="Learning Python is very easy"
# l=len(s)-1
# rev=""
# for i in range(l,-1,-1):
#    rev=rev+s[i]
# print(rev)
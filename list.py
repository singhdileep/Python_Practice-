'''Sum of the list which having string type'''


# l=[1,2,3,4,'a','5']
# l1=[]
# l2=[]
# s1=[]
# for i in l:
#     if type(i)==int or i.isdigit():
#         l1.append(int(i))
#     else:
#         l2.append(i) 
# s=sum(l1)
# s1.append(s)
# s1.extend(l2)
# # s.extend(l1)
# print(s1)


''' Conver list into string '''

# l=['a','b','Dileep']
# s=''.join(l)
# print(s)


''' code for frequency of a list '''

# l=['a','b','a','c','d','a','b']
# d={}
# for i in l:
#     if i in d:
#         d[i]=d.get(i,0)+1
#     else:
#         d[i]=1    
# print(d)    



# s="my name is Dileep Kumar Singh I am from Deoria  my  my my"
# s1=s.split()
# d={}
# for i in s1:
#     if i in d:
#         d[i]=d.get(i,0)+1
#     else:
#         d[i]=1
# print(d)            


# l=[1,2,3,3,4,4,4,5,6,6,6,7,7,7,8]   
# d={}
# for i in l:
#     if i not in d:
#         d[i]=0
#     d[i]=d[i]+1
# print(d)    
# # for k,v in d.items():
# #     print(k,":",v)         


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


'''Change the position of the list '''
# o/p--l=[1,0,3,2,5,4]

# l=[0,1,2,3,4,5]
# for i in range(0,len(l),2):
#     l[i],l[i+1]=l[i+1],l[i]
# print(l)    


# '''Remove 0 from the list '''

# l=[1,2,3,0,4,0,7,0,0,6,0]
# def rem_list(l):
#     for i in l:
#         if i==0:
#             l.remove(0)
#             l.append(0)
#     return l        
# print(rem_list(l))    



'''Python code to find the index , whose sum is equal to the target number '''



# def twosum(nums,target):
#     for i,num in enumerate(nums):
#         pair=target-num
#         if pair in nums[i+1:]:
#             return[i,nums.index(pair,i+1)]
#     return None
# print(twosum([1,8,9,2,34,4,10,1],11))  


# def addlen(l,target):
#     for i in range(len(l)):
#         for j in range(i+1,len(l)):
#             if l[i]+l[j]==target:
#                 return [i,j]
#     return None 
# print(addlen([1,2,3,6,7,8,9],9))   
            

'''Add Two List Numbers find the reverse of its sum'''

# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.



# l=[1,2,3,4,5]
# l2=[6,7,8,9,10]
# l3=l[::-1]
# l4=l2[::-1]
# s=""
# s1=""
# for i in l3:
#     s=s+str(i)
# for j in l4:
#     s1=s1+str(j)
# s2=int(s)+int(s1)
# s3=str(s2)[::-1]
# print(s3)



# s="abccbaaa"
# def longest_substr(s):
#     longest = 0
#     for start_index in range(len(s)):
#         s1 = set()
#         for letter in s[start_index:]:
#             if letter in s1:
#                 break
#             s1.add(letter)
#         longest = max(longest,len(s1))
#     return longest
# print(longest_substr(s))    



# s="abcabcdbca"
# length = 0
# for i in range(len(s)):
#     for j in range(i+1,len(s)):
#         if s[i] == s[j]:
#             length = len(s[:j+2])
#         else:
#             length=len(s)
# print(length)


# l=[1,2,3,4,6,8,9,10]
# for i in range(1,len(l)):
#     if i in l:
#         None
#     else:
#         print(i)    


# import re
# x="[^<b></b>]"
# pattern=re.finditer(x,"<b>This is dileep</b>this is dilll<b>I love</b>")
# for i in pattern:
#     print(i.start(),"...",i.end())


# import re

# content = '''<p>The <code>Pattern</code> is a compiled
# representation of a regular expression.</p>'''

# pattern = re.compile(r'(</?[a-z]*>)')

# found = re.findall(pattern, content)

# for tag in found:
#     print(tag)


# import djang
# print(django.get_version())
# import random 
# for i in range(5): 
#     print(random(1, 5))


# def make_pretty(func):
#     def inner():
#         print("I got decorted")
#         func()
#     return inner

# @make_pretty
# def ordinary():
#     print("I am ordinary") 
# ordinary()    

# # pretty=make_pretty(ordinary)
# # pretty()      


# l=[1,2,3,4,5,6,7]
# l1=iter(l)
# for i in l1:
#     print(next(l1))



# class InfIter:
#     """Infinite iterator to return all
#         odd numbers"""

#     def __iter__(self):
#         self.num = 1
#         return self

#     def __next__(self):
#         num = self.num
#         self.num += 2
#         return num
# a = iter(InfIter())
# print(next(a))
# print(next(a))

# l=[33,45,2,46,5,7]
# n=len(l)
# l1=[]
# for i in range(n):
#     for j in range(0,n-i-1):
#         if l[j]>l[j+1]:
#             l[j],l[j+1]=l[j+1],l[j]
# for i in range(len(l)):
#     l1.append(l[i])
# print(l1)


# 

# import json 
  
# # JSON string 
# employee ='{"id":"09", "name": "Nitin", "department":"Finance"}'

# # Convert string to Python dict 
# employee_dict = json.loads(employee) 
# print(employee_dict) 
  
# print(employee_dict['name']) 
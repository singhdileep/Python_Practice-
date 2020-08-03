'''Sum of the list which having string type'''


# l=[1,2,3,4,'a','5']
# l1=[]
# l2=[]
# for i in l:
#     if type(i)==int or i.isdigit():
#         l1.append(int(i))
#     else:
#         l2.append(i) 
# print((sum(l1)))  


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
# for k,v in d.items():
#     print(k,":",v)         


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


'''Remove 0 from the list '''

# l=[1,2,3,0,4,0,7,0,0,6,0]
# def rem_list(l):
#     for i in l:
#         if i==0:
#             l.remove(0)
#             l.append(0)
#     return l        
# print(rem_list(l))    


def twosum(nums,target):
    for i,num in enumerate(nums):
        pair=target-num
        if pair in nums[i+1:]:
            return[i,nums.index(pair,i+1)]
    return None
print(twosum([1,8,9,2,34,4,10,1],11))  

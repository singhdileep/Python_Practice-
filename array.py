'''Array rotate i/n= l=[1,2,3,4,5,6,7]
o/p=l[6,7,1,2,3,4,5]'''

# nums=[1,2,3,4,5,6,7]
# k=2
# for i in range(k):
#     previous = nums[-1]
#     for j in range(len(nums)):
#         nums[j], previous = previous, nums[j]
#         print("previous {}".format(previous))        
#         print("p{}".format(nums[j]))        
# print(nums) 


# def rotate(l, x):
#   return l[-x:] + l[:-x] 
# l=[1,2,3,4,5,6,7]
# x=2 
# print(rotate(l,x)) 


'''Array rotate i/n= l=[1,2,3,4,5,6,7]
o/p=l[3,4,5,6,7,1,2]'''


# def rotate(l, x):
#   return l[x % len(l):] + l[:x % len(l)]
# l=[1,2,3,4,5,6,7]
# x=2 
# print(rotate(l,x))   


# l=[1,2,3,4,5,6,7]
# l1=[]
# n=2
# for i in range(len(l)-n,len(l)):
#     l1.append(l[i])
# for j in range(0,len(l)-n):
#     l1.append(l[j])
# print(l1)        


# l=[1,2,3,4,5,6,7]
# n=2
# l1=[]
# for i in range(n,len(l)):
#     l1.append(l[i])
# for j in range(0,n):
#     l1.append(l[j])
# print(l1)    


# def rotation(n):
#   rotations = set()
#   for i in range( len( str(n) ) ):
#     n = int( str(n)[1:] + str(n)[:1] )
#     rotations.add(n)
#   return rotations
# print(rotation(1234))  




  
# s="Dileep"
# s1="applek"
# l1=list(s)
# l2=list(s1)
# l3 = [i for i in l1 if i not in l2]
# print(l3)


# s="Dileep"
# s1="applek"
# l1=list(s)
# l2=list(s1)
# l3=[]
# for i in l1:
#     if i not in l2:
#         l3.append(i)
# print("".join(l3))        

'''reverse of string'''

# s="My name is dileep"
# print(s[::-1])


# s="my name is dileep singh"
# l=len(s)-1
# rev=""
# for i in range(l,-1,-1):
#     rev=rev+s[i]
# print(rev)    

# s="my name is dileep singh"
# print("".join(reversed(s)))


# s="my name is   dileep     singh   "
# s1=s.split()
# l=len(s1)-1
# l1=[]
# for i in range(l,-1,-1):
#     l1.append(s1[i][::-1])
# print(" ".join(l1))    



# s="aaaabbbxxxcc"
# var=""
# for i in s:
#     if i in s:
#         if i in var:
#             pass
#         else:
#             var=var+i
# print(var)   
# 
# 

# s="aaabbbaaabbcccbddd"
# d={}
# for i in s:
#     if i in d:
#         d[i]=d.get(i,0)+1
#     else:
#         d[i]=1
# print(d)                     


# s="aaababbababacbcbcjsjsjjs"
# d={}
# for i in s:
#     if i in d.keys():
#         d[i]=d[i]+1
#     else:
#         d[i]=1
# print(d)   
# 


# import datetime
# date=datetime.datetime.now()
# # print("It's now:{:%d%m%y %H:%M:%S}".format(date))
# print(date)


'''find all subsequences'''

# def findsubseq(l,sum):
#     sum1=0
#     for i in range(len(l)):
#         for j in range(i,len(l)):
#             sum1=sum1+l[j]
#             if sum1==sum:
#                 print(l[i:j+1])
#             # else:
#             #     print("There is no any subsequences ")
# l=[1,2,3,4,5,6,8,10]
# sum=10 
# findsubseq(l,sum)                   

# def findSublists(A, sum):
# 	for i in range(len(A)):
# 		sum_so_far = 0
# 		for j in range(i, len(A)):
# 			sum_so_far += A[j]
# 			if sum_so_far == sum:
# 				print(A[i:j+1])
# # A = [3, 4, -7, 1, 3, 3, 1, -4]
# A=[1,2,3,4,5,6,7,8,10]
# sum = 10

# findSublists(A, sum)


# def generate(st, s): 
#     if len(s) == 0: 
#         return
  
#     # If current string is not already present. 
#     if s not in st: 
#         st.add(s) 
  
#         # Traverse current string, one by one 
#         # remove every character and recur. 
#         for i in range(len(s)): 
#             t = list(s).copy() 
#             t.remove(s[i]) 
#             t = ''.join(t) 
#             generate(st, t) 
  
#     return
  
  
# # Driver Code 
# if __name__ == "__main__": 
#     s = "xyz"
#     st = set() 
#     generate(st, s) 
#     for i in st: 
#         print(i) 



# def subarray_sum(arr,sum):
#     dict1={}
#     curr_sum=0
#     for i in range(len(arr)):
#         curr_sum=curr_sum+arr[i]
#         if curr_sum ==sum:
#             print("Subarray starts from 0 to",i)
#             break
#         if curr_sum-sum in dict1:
#             print("Subarray starts from",dict1[curr_sum-sum]+1 ,"to" ,i)
#             break
#         dict1[curr_sum]=i
#     print("No subarray found")

# arr=[1,4,20,3,10,5]
# sum=5
# print(subarray_sum(arr,sum))

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



# def isSubSequence(s,vocabulary): 
#     a = len(s); 
#     b = len(vocabulary); 
#     j = 0
#     i = 0; 
#     while (i < b and j < a): 
#         if (s[j] == vocabulary[i]): 
#             j += 1 
#         i += 1 
#     return (j == a) 
# def Longest_word(dict1,s): 
#     result = "" 
#     length = 0   
#     for word in dict1: 
#         if (length < len(word) and isSubSequence(word,s)): 
#             result = word 
#             length = len(word)
#     if result=="":
#         return "none"         
#     return result  
# dict1 = ["ale", "apple", "monkey", "plea"] 
# s = "abpcplea"   
# print(Longest_word(dict1,s)) 



# def isSubSequence(s,vocabulary): 
#     a = len(s); 
#     b = len(vocabulary); 
#     j = 0
#     i = 0
#     while (i < a and j < b): 
#         if (s[i] == vocabulary[j]): 
#             i += 1 
#         j += 1 
#     return (i == a)
# def Longest_word(s,vocabulary): 
#     result = "" 
#     length = 0   
#     for word in vocabulary: 
#         if (length < len(word) and isSubSequence(word,s)): 
#             result = word 
#             length = len(word)
#     if result=="":
#         return "none"         
#     return result  
# vocabulary = ["ale", "apple", "monkey", "plea"] 
# s = "abpcplea"   
# print(Longest_word(s,vocabulary)) 


# def solution(S, D):
#    print(S)

#    D.sort(key=len,reverse=True)
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
#    return "none"
# a_string = "abppplee"
# words = ["able", "ale", "apple", "bale", "kangaroo","appple","applee"]
# result = solution(a_string, words)
# print(result)



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




# l=['aaa','a','xyz']
# s='a'
# if s in l:
#     print(True)
# else:
#     print(False)    


# def sumSubsets(sets, n, target) : 
#     x = [0]*len(sets); 
#     j = len(sets) - 1;  
#     while (n > 0) : 
#         x[j] = n % 2;  
#         n = n // 2;  
#         j -= 1;  
#     sum = 0;  
#       for i in range(len(sets)) : 
#         if (x[i] == 1) : 
#             sum += sets[i];  
#     if (sum == target) : 
#         print("{",end="");  
#         for i in range(len(sets)) : 
#             if (x[i] == 1) : 
#                 print(sets[i],end= ", ");  
#         print("}, ",end="");  
# def findSubsets(arr, K) : 
#     x = pow(2, len(arr));  
#     for i in range(1, x) : 
#         sumSubsets(arr, i, K);  
# if __name__ == "__main__" :  
#     arr = [ 5, 10, 12, 13, 15, 18 ];  
#     K = 30; 
#     findSubsets(arr, K); 


# def bubbleSort(arr): 
#     n = len(arr) 
#     for i in range(n): 
#         for j in range(0, n-i-1): 
#             if arr[j] > arr[j+1] : 
#                 arr[j], arr[j+1] = arr[j+1], arr[j] 
# arr = [64, 34, 25, 12, 22, 11, 90] 
# bubbleSort(arr) 
# print (arr) 



# s="test-1-str"
# s1="t"
# l=[]
# for i in range(len(s)):
#     if s[i]=="t":
#         l1=0,i
#         l.append(l1)

# print(l)        


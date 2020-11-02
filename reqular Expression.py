# import re
# count=0
# pattern=re.compile("aba")
# matcher=pattern.finditer("abaababa")
# for i in matcher:
#     count=count+1
#     print(i.start(),"...",i.end(),"...",i.group())
# print("The number of occurence:",count)   



'''We can pass pattern directly as argunment to the finditer function '''


# import re
# count=0
# matcher=re.finditer("ab","abaabbbabababababbbbaaaa")
# for i in matcher:
#     count=count+1
#     print(i.start(),"...",i.end(),"...",i.group())
# print("The pattern occurnce is :",count)    



'''Character Classes '''


# import re
# matcher=re.finditer("[^a-zA-z0-9]","a7b@k9z")
# for i in matcher:
#     print(i.start(),"...",i.end(),"....",i.group())



'''Match(): it is basically use to check the given pattern at beginning of target string.'''

# import re
# s=input("Enter pattern to check :")
# m=re.match(s,"abcdefgh")
# if m!=None:
#     print("Match is availabe in the Pattern at beginning")
#     print("Start index ",m.start(),"And end index :",m.end())
# else:
#     print("Match is not available at the beginning of the String")    


'''Fullmatch():This function is used to match pattern of the target string :'''

# import re
# s=input("Enter Pattern to check: ")
# m=re.fullmatch(s,"abcdef")
# if m!=None:
#     print("Full string is matched")
# else:
#     print("String is not matched")    


'''findall():It is basically used to find all the occurence of the 
the match and it will return in list object which contain alll occurence'''

import re
f=re.findall("[a-z]","my name is dileep singh")
print(f)

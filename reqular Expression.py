import re
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


'''search(): It is basically used to search pattern into the given target string
if the match is available then it will return the match object which present first occurence ot the match othewise It will
return None'''

# import re
# s=input("Enter the search pattern :")
# m=re.search(s,"abbaabxba")
# if m!=None:
#     print("Match available ")
#     print("First occurnce of match satrt with :",m.start(),"and end with :",m.end())
# else:
#     print("Match is not available")


'''findall():It is basically used to find all the occurence of the 
the match and it will return in list object which contain alll occurence'''

# import re
# f=re.findall("[a-z]","my name is dileep singh")
# print(f)


# l=re.split("\.","This.is.Dileep.Singh")
# print(l)
# for i in l:
#     print(i)

''' ^ this symbol is basically used to check whether the given string start with provided pattern or not '''
# s="Learning python is very easy"
# l=re.search("^very",s)
# if l!=None:
#     print("Target Start with Learning")
# else:
#     print("Target string not start with Learning")    

'''$  this symbol is basically used to check whether the given string end with provided pattern or not '''

# s="Learning python is very easy"
# l=re.search("easy$",s)
# if l!=None:
#     print("Target end with easy")
# else:
#     print("Target string not end with easy")


''' Write a python program to check whether the given string is Yava
language identifier or not?'''

# s=input("Enter Identifier:")
# m=re.fullmatch("[a-k][0369][a-zA-Z0-9#]*",s)
# if m!= None:
#     print(s,"is valid Yava Identifier")
# else:
#     print(s,"is invalid Yava Identifier")


'''App4: Write a Python Program to check whether the given number
is valid mobile number or not?'''

# n=input("Enter Mobile Number :")
# m=re.fullmatch("[7-9]\d{9}",n)
# if m!=None:
#     print(n,"It is a valid Mobile Number")
# else:
#     print(n,"It is invalid Mobile Number ")    


'''App5: Write a python program to extract all mobile numbers present in
input.txt where numbers are mixed with normal text data'''

# f1=open("mobile.txt","r")
# f2=open("mob.txt","w")
# for line in f1:
#     list=re.findall("[7-9]\d{9}",line)
#     for n in list:
#         f2.write(n+"\n")
# print("Extracted all Mobile Numbers into output.txt")
# f1.close()
# f2.close()



# import re,urllib
# import urllib.request
# sites="accenture".split()
# print(sites)
# for s in sites:
#     print("Searching...",s)
#     u=urllib.request.urlopen("http://"+s+".com")
#     text=u.read()
#     title=re.findall("<title>.*</title>",str(text),re.I)
#     print(title[0])


'''Q. Write a Python Program to check whether the given mail id is
valid gmail id or not?'''


# s=input("Enter any email id :")
# m=re.fullmatch("\w[a-zA-Z0-9_.]*@gmail[.]com",s)
# if m!=None:
#     print("It is a valid Email id")
# else:
#     print("It is invalid Mial id")

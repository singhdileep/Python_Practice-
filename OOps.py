''''Instace variable : Is is also called object level variable'''

# class Test:
#     '''my name is dileep singh'''
#     def __init__(self,name,rollno,addr):
#         self.name=name
#         self.rollno=rollno
#         self.addr=addr
#     def display(self):
#         self.m=100
#         print("the emp name is :",self.name)
#         print("the emp rollno is :",self.rollno)
#         print("the emp addr is :",self.addr)
# s=Test("Dileep",100,"GKP")
# s.display()
# print(s.__dict__)        
# print(s.__doc__)        

'''Passing members of one class to another class: '''

# class Employee:
#     def __init__(self,eno,ename,esal):
#         self.eno=eno
#         self.ename=ename
#         self.esal=esal
#     def display(self):
#         print("Employee Number is :",self.eno)
#         print("Employee Name is :",self.ename)
#         print("Employee salary is :",self.esal)
# class Test:
#     def modify(emp):
#         emp.esal=emp.esal+1000
#         emp.display() 
# e=Employee(100,"Dileep",2000)
# Test.modify(e)               


# class duck:
#     def talk(slef):
#         print("Duck is talking")
# class dog:
#     def talk(slef):
#         print("Dog is talking")
# class hen:
#     def talk(slef):
#         print("hen is talking")
# class parrot:
#     def talk(slef):
#         print("parrot is talking")
# def f1(obj):
#     obj.talk()
# l=[duck(),dog(),hen(),parrot()]
# for i in l:
#     f1(i)



'''Method Overriding'''


# class P:
#     def property(self):
#         print('Gold+Land+Cash+Power')
#     def marry(self):
#         print('Appalamma')
# class C(P):
#     def marry(self):
#         super().marry()
#         print('Katrina Kaif')
# c=C()
# c1=P()
# c.property()
# c.marry()
# c1.marry()
                                


# l=[1,2,3,4]
# print(l[-5:-3])


# count = 1  
# def doThis(): 
#     global count 
#     for i in (1, 2, 3):  
#         count += 1
#         print(i)
# doThis()   
# print (count)

# dictionary = {} 
# dictionary[1] = 1
# dictionary['1'] = 2
# dictionary[1] += 1 
# sum = 0
# for k in dictionary: 
#     sum += dictionary[k] 
#     print(k) 
# print(sum)


# l=['dileep','pranjal','pratoon']
# l1=[]
# for i in range(len(l)):
#     l1.append(l[i][-1])
# print(l1)    


# nameList = ['Harsh', 'Pratik', 'Bob', 'Dhruv']  
# pos = nameList.index("Bob")  
# print(pos * 5) 

# l=[1,2,3,4]
# print(l[-5:-3])

# list = ['a', 'b', 'c', 'd']
# print(list[10:]) 
# print(list) 

# dictionary1 = {'Google' : 1, 
#                'Facebook' : 2, 
#                'Microsoft' : 3
#                } 
# dictionary2 = {'GFG' : 1, 
#                'Microsoft' : 2, 
#                'Youtube' : 3
#                } 
# dictionary1.update(dictionary2); 
# for key, values in dictionary1.items(): 
#     print(key, values) 

# dictionary1 = {'GFG' : 1, 
#                'Google' : 2, 
#                'GFG' : 2
#                } 
# print(dictionary1['GFG']); 



# data = [2, 3, 9] 
# temp = [[x for x in[data]] for x in range(3)] 
# print (temp) 

# L1 = [] 
# L1.append([1, [2, 3], 4]) 
# L1.extend([7, 8, 9]) 
# print(L1)
# print(L1[0][1][1] + L1[2])


# List = [True, 50, 10]
# List.insert(2, 5)    
# print(List, "Sum is: ", sum(List))


# d={}
# for i in enumerate(range(2)):
#     print(i)

# mylist = ['geeks', 'forgeeks'] 
# for i in mylist: 
#     l=mylist.append(i.upper()) 
# print(mylist) 
# print(l) 


# my_string = 'geeksforgeeks'
# for i in range(len(my_string)): 
#     print (my_string) 
#     my_string = 'a'


# import json 
  
# # {key:value mapping} 
# a ={"name":"John", 
#    "age":31, 
#     "Salary":25000} 
  
# # conversion to JSON done by dumps() function 
# b = json.dumps(a) 
  
# # printing the output 
# print(b) 
# print(type(a))

# import json
# with open("sample.json", "w") as p: 
#      json.dumps(var, p)
# 


e= int(input(""))
eStudents = set(input().split())
f =int(input(""))
fStudents = set(input().split())

print(len(eStudents ^ fStudents))
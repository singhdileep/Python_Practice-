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
                                

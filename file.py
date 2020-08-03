
'''W+ means read and write if the file is not exist ,if it is existing then it will be override
   git init
   git add .
   git commit -m "first commit" 
   git remote add origin https://github.com/singhdileep/Python_Practice-.git
   git push -u origin master


'''


# with open("abc.txt","w+") as f:
#     f.write("Hi My name is Dileep Singh\n")
#     f.write("I am from Deoria \n")
#     f.write("I am working in Accenture \n")
#     f.seek(0)
#     data=f.read()
# print(data)


'''a+ means read and append and it wont be override if the file is exists.'''  


# with open("abc.txt","a+") as f:
#     f.write("I have 2+ year experience in Accenture")
#     f.seek(0)
#     data=f.read()
# print(data)    


'''Program to count the occurence of the word from the file '''

# with open("abc.txt","r") as f:    
#     wordcount={}
#     for word in f.read().split():
#         if word not in wordcount:
#             wordcount[word] = 1
#         else:
#             wordcount[word] += 1
#     print (word,wordcount)


'''Write a program to check whether the given file exists or not. If it is available then print its content.
   To check file is exist or not we shoud use isfile() function along with os library and its module and its submodue
   os.path.isfile(fname)
'''

# import os,sys
# fname=input("Enter the file name:")
# if os.path.isfile("abc.txt"):
#     print("File is exists",fname)
#     f=open(fname,"r")
# else:
#     print("File not exists",fname)
#     sys.exit()
# print("The content of the file is :")
# data=f.read()
# print(data)



'''Code to print no of line ,words and characters present in file '''


# f=open("abc.txt","r")
# lcount=wcount=ccount=0
# for line in f:
#     lcount=lcount+1
#     ccount=ccount+len(line)
#     word=line.split()
#     wcount=wcount+len(word)
# print("The required Details Below")
# print("------------------------------")
# print("The count of Line :",lcount)    
# print("The count of character :",ccount)    
# print("The count of Words :",wcount)    


'''CSV file - It means comma seperated values 
   Create CSV file 
'''


# import csv
# with open("emp.csv","w",newline='') as f:
#    w=csv.writer(f)
#    w.writerow(["Eno","Ename","Esal","Eaddr"])
#    n=int(input("Enter the number of Emplyees: "))
#    for i in range(n):
#       eno=input("Enter the Employee No :")
#       ename=input("Enter the Employee Name :")
#       esal=input("Enter the Employee Salary :")
#       eaddr=input("Enter the Employee Address :")
#       w.writerow([eno,ename,esal,eaddr])
# print("The total Employees data written to csv is Successfully")



'''Reading data from CSV file'''

# import csv
# with open("emp.csv","r") as f:
#    data=csv.reader(f)
#    d=list(data)
#    for line in d:
#       for word in line:
#          print(word,"\t",end='') 
#       print()


'''Zipping and UnZipping file

The main Advantages of Zip file is that
It improves memory Utilization 
We can reduce the transport time
We can improves performances.
synax of zip file is 
f=ZipFile("abc.zip","w","ZIP_DEFLATED")
For that we have to import zip module
'''

# from zipfile import *
# f=ZipFile("file.zip",'w',ZIP_DEFLATED)
# f.write("abc.txt")
# f.write("emp.csv")
# # f.write("file3.txt")
# # f.write("file4.txt")
# f.close()
# print("Zip file is created Successfully")

'''UnZipping the file '''

# from zipfile import *
# f=ZipFile("file.zip",'r',ZIP_STORED)
# names=f.namelist()
# for name in names:
#    print("File name is ",name)
#    f1=open(name,'r')
#    print(f1.read())
#    print()


# import os
# for dirpath,dirnames,filenames in os.walk('.'):
#    print("Current Directory Path:",dirpath)
#    print("Directories:",dirnames)
#    print("Files:",filenames)
#    print()



'''To get information about file '''

# import os
# stats=os.stat("file.py")
# print(stats)


# import pickle
# class Employee:
#    def __init__(self,eno,ename,esal,eaddr):
#       self.eno=eno;
#       self.ename=ename;
#       self.esal=esal;
#       self.eaddr=eaddr;
#    def display(self):
#       print(self.eno,"\t",self.ename,"\t",self.esal,"\t",self.eaddr)
# with open("emp.dat","wb") as f:
#    e=Employee(100,"Durga",1000,"Hyd")
#    pickle.dump(e,f)
#    print("Pickling of Employee Object completed...")
# with open("emp.dat","rb") as f:
#    obj=pickle.load(f)
#    print("Printing Employee Information after unpickling")
#    obj.display()


'''yet to learn load and loads ,dump and dumps and pickle and unpickle '''



'''To check the information of a file '''
# import os
# stats=os.stat("abc.txt")
# print(stats)

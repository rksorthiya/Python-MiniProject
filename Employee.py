#1
from connect import *
from PermanentEmployee import *
from Validation import *
class Employee:
      
      _empname=""
      _emptype=""
      _empemail=""
      _empsalary=""

      def __init__(self):
            self._empname = input("enter name: ")
            self._empemail=input("enter email : ")
            objvalidation = Validation()
            while(not objvalidation.Validationemail(self._empemail)):
                  self._empmob=input("enter email : ")
            self._empmob=input("enter mobile no : ")
            objvalidation = Validation()
            while(not objvalidation.Validationmob(self._empmob)):
                  self._empmob=input("enter mobile no : ")
            self._emptype = input("enter type : ")
            while(not (self._emptype == 'p' or self._emptype == 'P')):
                  print("Invalid Employee. Please enter only 'p' or 'P'")
                  self._emptype = input("enter type : ")
            self._empexp = int(input("enter experience: "))
            self._empsalary = self.getsalary()
            
            
      def getsalary(self):
            if self._emptype=="P" or self._emptype=="p":
                  Opemp = Per_Emp()
                  return Opemp.calculatesalary(self._empexp)
            else:
                  print("Invalid Employee. Please enter only 'p' or 'P'")
                  self._emptype = input("enter type : ")
                  return False
                  
      #3
      @staticmethod
      def addnote() :
            note = input("Enter note : ")
            f = open("note.txt","a")
            f.write(note)
            print("Note Added...")
            f.close()
                  
print("1. Add Emp")
print("2. Display Emp")
print("3. Add Notes")
choice = int(input("Enter your Choice:"))
if choice == 1:
      c = Employee()
      obj = myconnect()
      obj.savetodb(c._empname,c._empemail,c._empmob,c._emptype,c._empexp,c._empsalary)
elif choice==2:
      obj = myconnect()
      obj.display()
elif choice==3:
      Employee.addnote()
else:
      print("invalid choice")
      

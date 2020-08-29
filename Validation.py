import re

class Validation :

    def Validationemail(self,email):
        pattern=re.compile(r'[\w\.-]+@[\w\.-]+')
        if pattern.match(email):
            return True
        else:
            print("Enter valid email")
            return False

    def Validationmob(self,mob):
        pattern=re.compile(r'\d{10}')
        if pattern.match(mob):
            return True
        else:
            print("Enter valid Mobile no")
            return False
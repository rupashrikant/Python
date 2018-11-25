import re
class User:
    def __init__(self, name = None, phoneNumber = None, password = None, email = None):
        self.name = name;
        self.phoneNumber = phoneNumber;
        self.password = password;
        self.email = email;        
        
    def validatePassword(self, password):
        if re.match('((?=.*\\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%]).{8,})', password):
            if len(password) >= 8:
                return 1;
        return 0;
    
    def validatePhoneNumber(self, pno):
        if re.match('((?=.*\\d).{10,})', pno):
            if len(pno) == 10:
                return 1;
        return 0;
    
    def validateEmail(self, email):
        if(re.match('[^@]+@[^@]+\.[^@]+', email)):
            return 1;
        return 0;
    
    def displayUserDetails(self):
        print "Name : ", self.name;
        print "PhoneNumber : ",self.phoneNumber;
        print "Email : ", self.email;
        print "Password : ", self.password;
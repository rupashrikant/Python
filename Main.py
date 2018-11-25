import User

name = raw_input("Enter the name :\n");
pn = raw_input("Enter the mobile number :\n");
u1 = User.User()
valid = 0;
while 1 :
    valid = u1.validatePhoneNumber(pn);
    if valid == 1:
        break;
    else:
        print "Invalid mobile number";
        print "Enter the valid mobile number";
        pn = raw_input();
        
password= raw_input("Enter the password :\n");
while 1 :    
    valid = u1.validatePassword(password);
    if valid == 1:
        break;
    else:
        print "Invalid password";
        print "Enter the valid password";
        password = raw_input();
        
email = raw_input("Enter the email :\n");
while 1 :    
    valid = u1.validateEmail(email);
    if valid == 1:
        break;
    else:
        print "Invalid email";
        print "Enter the valid email";
        email = raw_input();
        

u = User.User(name, pn, password, email);
u.displayUserDetails()
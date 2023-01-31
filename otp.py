email="prabhu@gmail.com"
pwd="123456"
cemail=input("enter your email:")
cpwd=input("enter your cpwd:")
otp=6789
if(email==cemail and pwd==cpwd):
    print("login successful")
    cotp=int(input("enter otp"))
    if(otp==cotp):
        print("welcome to page")
    else:
        print("otp is mismatched")    
elif(email==cemail and pwd!=cpwd):
    print("login failed due to wrong password")
elif(email!=cemail and pwd==cpwd):
    print("login failed due to incorrect email")
else:
    print("login failed due to incorrect email and password")

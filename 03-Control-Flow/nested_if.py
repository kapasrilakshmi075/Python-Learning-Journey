age=21
has_voterid=False
if age>=18:
   if has_voterid:
        print("You can Vote")
   else:
       print("You need a voter id")
else:
    print("You can't Vote")
     
username="kapasrilakshmi"
password=987654321
if username=="kapasrilakshmi":
    if password==987654321:
        print("Login System")
    else:
        print("Incorrect password")
else:
    prnt("incorrect unsername and password")

marks=75
if marks>=50:
    if marks>=75:
        print("Distinction")
    else:
        print("Pass")
else:
    print("Fail")

age=18
driving_license=True
if age>=18:
    if driving_license:
        print("Can drive")
    else:
        print("Need license")
else:
    print("Can't drive")

number=26
if number>0:
    if number%2==0:
       print("Even")
    else:
       print("Odd")
else:
    print("Number is zero or negative")

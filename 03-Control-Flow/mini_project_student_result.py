choice="yes"
while choice=="yes":
   name=input("Enter the name:")
   marks=float(input("Enter the marks:"))

   if marks>=90:
       print("Grade A")
   elif marks>=75:
    print("Grade B")
   elif marks>=50:
       print("Grade C")
   else:
       print("Fail")

   if marks>=50:
       print("Passed")
       if marks>=75:
           print("Excellent Performance")
       else:
           print("Good Performance")
   else:
       print("Needs Improvement")

   for i in range(3):
       print(name)
    

   choice=input("Do you want to check another student? (yes/no):")
print("Program ended")    

    

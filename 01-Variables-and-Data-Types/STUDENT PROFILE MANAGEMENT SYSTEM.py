student_name="Lakshmi"
age=21
degree="B-Tech"
branch="CSE"
cgpa=8.7
college_name="Mohan Babu University"
career_goal="Python Full Stack Developer"
skills=["pyhton","java","c","c++","data analyst"]
academic_details=("B-Tech", "CSE","2027", 8.7)
technologies={"Python","SQL","Power BI","Python"}
student_profile={"name":"Lakshmi",
                 "age":21,
                 "degree":"B-Tech",
                 "branch":"CSE",
                 "CGPA":8.7,
                 "skills":"python programming"}
                 
print("------student details-----")
print(student_name)
print(age)
print(degree)
print(branch)
print(cgpa)
print(college_name)
print(career_goal)
print(career_goal.upper())
print(len(career_goal))
print(skills)
skills.append("sql")
print(skills)
skills.remove("data analyst")
print(skills)
print(academic_details)
print(academic_details[0])
print(len("academic_details"))
print(technologies)
technologies.add("tableau")
print(technologies)
print(student_profile)
student_profile["career_goal"]="Data analyst"
print(student_profile)
student_profile["CGPA"]=9.0
print(student_profile)
print(student_profile.keys())
print(student_profile.values())
print(student_profile.items())
print("\n----- STUDENT PROFILE MANAGEMENT SYSTEM -----")
print(student_profile)




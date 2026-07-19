# Python Strings Practice

# Q1. Create a variable containing your name and print it.
name = "Lakshmi"
print(name)


# Q2. Find the length of the string "Python Programming".
text = "Python Programming"
print(len(text))


# Q3. Print the first character of "Python".
text = "Python"
print(text[0])


# Q4. Print the last character using negative indexing.
text = "Python"
print(text[-1])


# Q5. Extract "Python" from "Python Programming" using slicing.
text = "Python Programming"
print(text[0:6])


# Q6. Convert "python programming" to uppercase.
text = "python programming"
print(text.upper())


# Q7. Convert "PYTHON PROGRAMMING" to lowercase.
text = "PYTHON PROGRAMMING"
print(text.lower())


# Q8. Convert "python full stack developer" to title case.
text = "python full stack developer"
print(text.title())


# Q9. Remove extra spaces from the string.
text = "   Python   "
print(text.strip())


# Q10. Replace "Java" with "Python".
text = "I am learning Java"
print(text.replace("Java", "Python"))


# Q11. Split the string into separate items.
skills = "Python,SQL,Excel,Power BI"
print(skills.split(","))


# Q12. Combine first name and last name.
first_name = "Sri"
last_name = "Lakshmi"
full_name = first_name + " " + last_name
print(full_name)


# Q13. Print name and age using an f-string.
name = "Lakshmi"
age = 21
print(f"My name is {name} and I am {age} years old.")


# Q14. Check whether "Python" exists in the string.
text = "I am learning Python"
print("Python" in text)


# Q15. Count how many times "a" occurs in "banana".
text = "banana"
print(text.count("a"))


# Q16. Find the index of "Programming".
text = "Python Programming"
print(text.index("Programming"))

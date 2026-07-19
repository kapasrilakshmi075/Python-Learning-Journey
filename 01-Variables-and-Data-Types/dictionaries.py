# Python Dictionaries Practice

# Q1. Create a dictionary containing student details and print it.
student = {
    "name": "Lakshmi",
    "age": 21,
    "course": "Python"
}
print(student)


# Q2. Check the data type of the dictionary.
student = {
    "name": "Lakshmi",
    "age": 21
}
print(type(student))


# Q3. Find the length of the dictionary.
student = {
    "name": "Lakshmi",
    "age": 21,
    "course": "Python"
}
print(len(student))


# Q4. Access the value of the "name" key.
student = {
    "name": "Lakshmi",
    "age": 21,
    "course": "Python"
}
print(student["name"])


# Q5. Access the value of "course" using get().
student = {
    "name": "Lakshmi",
    "age": 21,
    "course": "Python"
}
print(student.get("course"))


# Q6. Add a new key-value pair to the dictionary.
student = {
    "name": "Lakshmi",
    "age": 21
}
student["course"] = "Python"
print(student)


# Q7. Change the value of an existing key.
student = {
    "name": "Lakshmi",
    "age": 21
}
student["age"] = 22
print(student)


# Q8. Change a value using update().
student = {
    "name": "Lakshmi",
    "age": 21
}
student.update({"age": 22})
print(student)


# Q9. Remove an item using pop().
student = {
    "name": "Lakshmi",
    "age": 21,
    "course": "Python"
}
student.pop("age")
print(student)


# Q10. Remove an item using del.
student = {
    "name": "Lakshmi",
    "age": 21,
    "course": "Python"
}
del student["course"]
print(student)


# Q11. Remove the last inserted item using popitem().
student = {
    "name": "Lakshmi",
    "age": 21,
    "course": "Python"
}
student.popitem()
print(student)


# Q12. Get all keys using keys().
student = {
    "name": "Lakshmi",
    "age": 21,
    "course": "Python"
}
print(student.keys())


# Q13. Get all values using values().
student = {
    "name": "Lakshmi",
    "age": 21,
    "course": "Python"
}
print(student.values())


# Q14. Get all key-value pairs using items().
student = {
    "name": "Lakshmi",
    "age": 21,
    "course": "Python"
}
print(student.items())


# Q15. Check whether the "name" key exists in the dictionary.
student = {
    "name": "Lakshmi",
    "age": 21
}
print("name" in student)


# Q16. Remove all items using clear().
student = {
    "name": "Lakshmi",
    "age": 21,
    "course": "Python"
}
student.clear()
print(student)

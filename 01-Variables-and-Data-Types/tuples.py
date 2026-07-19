# Python Tuples Practice

# Q1. Create a tuple of fruits and print it.
fruits = ("apple", "banana", "mango", "orange")
print(fruits)


# Q2. Check the data type of the tuple.
fruits = ("apple", "banana", "mango")
print(type(fruits))


# Q3. Find the length of the tuple.
fruits = ("apple", "banana", "mango", "orange")
print(len(fruits))


# Q4. Access the first item in the tuple.
fruits = ("apple", "banana", "mango")
print(fruits[0])


# Q5. Access the last item using negative indexing.
fruits = ("apple", "banana", "mango")
print(fruits[-1])


# Q6. Extract items from index 1 to 3 using slicing.
numbers = (10, 20, 30, 40, 50)
print(numbers[1:4])


# Q7. Print the first three items using slicing.
numbers = (10, 20, 30, 40, 50)
print(numbers[:3])


# Q8. Print items from index 2 to the end.
numbers = (10, 20, 30, 40, 50)
print(numbers[2:])


# Q9. Count how many times 20 appears in the tuple.
numbers = (10, 20, 30, 20, 40, 20)
print(numbers.count(20))


# Q10. Find the index of 30.
numbers = (10, 20, 30, 40, 50)
print(numbers.index(30))


# Q11. Demonstrate tuple immutability.
fruits = ("apple", "banana", "mango")

# The following statement will give an error because tuples are immutable.
# fruits[1] = "orange"

print(fruits)


# Q12. Convert a tuple to a list, change an item, and convert it back to a tuple.
fruits = ("apple", "banana", "mango")

temp = list(fruits)
temp[1] = "orange"
fruits = tuple(temp)

print(fruits)


# Q13. Join two tuples using the + operator.
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

result = tuple1 + tuple2
print(result)


# Q14. Repeat a tuple using the * operator.
numbers = (1, 2, 3)
print(numbers * 2)


# Q15. Check whether "banana" exists in the tuple.
fruits = ("apple", "banana", "mango")
print("banana" in fruits)


# Q16. Check whether "orange" does not exist in the tuple.
fruits = ("apple", "banana", "mango")
print("orange" not in fruits)

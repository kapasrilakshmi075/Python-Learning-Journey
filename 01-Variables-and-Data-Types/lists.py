# Python Lists Practice

# Q1. Create a list of fruits and print it.
fruits = ["apple", "banana", "mango", "orange"]
print(fruits)


# Q2. Find the length of the list.
fruits = ["apple", "banana", "mango", "orange"]
print(len(fruits))


# Q3. Access the first item in the list.
fruits = ["apple", "banana", "mango"]
print(fruits[0])


# Q4. Access the last item using negative indexing.
fruits = ["apple", "banana", "mango"]
print(fruits[-1])


# Q5. Print items from index 1 to 3 using slicing.
numbers = [10, 20, 30, 40, 50]
print(numbers[1:4])


# Q6. Change "banana" to "orange".
fruits = ["apple", "banana", "mango"]
fruits[1] = "orange"
print(fruits)


# Q7. Add "grapes" to the end of the list using append().
fruits = ["apple", "banana", "mango"]
fruits.append("grapes")
print(fruits)


# Q8. Add "orange" at index 1 using insert().
fruits = ["apple", "banana", "mango"]
fruits.insert(1, "orange")
print(fruits)


# Q9. Add multiple items using extend().
fruits = ["apple", "banana"]
fruits.extend(["mango", "orange"])
print(fruits)


# Q10. Remove "banana" using remove().
fruits = ["apple", "banana", "mango"]
fruits.remove("banana")
print(fruits)


# Q11. Remove the item at index 1 using pop().
fruits = ["apple", "banana", "mango"]
fruits.pop(1)
print(fruits)


# Q12. Delete the first item using del.
fruits = ["apple", "banana", "mango"]
del fruits[0]
print(fruits)


# Q13. Sort the numbers in ascending order.
numbers = [5, 2, 8, 1, 3]
numbers.sort()
print(numbers)


# Q14. Sort the numbers in descending order.
numbers = [5, 2, 8, 1, 3]
numbers.sort(reverse=True)
print(numbers)


# Q15. Reverse the order of the list.
numbers = [1, 2, 3, 4, 5]
numbers.reverse()
print(numbers)


# Q16. Count how many times 20 appears.
numbers = [10, 20, 30, 20, 40, 20]
print(numbers.count(20))


# Q17. Find the index of "mango".
fruits = ["apple", "banana", "mango", "orange"]
print(fruits.index("mango"))


# Q18. Clear all items from the list.
fruits = ["apple", "banana", "mango"]
fruits.clear()
print(fruits)

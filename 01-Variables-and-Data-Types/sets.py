# Python Sets Practice

# Q1. Create a set of fruits and print it.
fruits = {"apple", "banana", "mango", "orange"}
print(fruits)


# Q2. Check the data type of the set.
fruits = {"apple", "banana", "mango"}
print(type(fruits))


# Q3. Find the length of the set.
fruits = {"apple", "banana", "mango", "orange"}
print(len(fruits))


# Q4. Create a set with duplicate values and print it.
# Observe that duplicate values are automatically removed.
numbers = {10, 20, 30, 20, 40, 10}
print(numbers)


# Q5. Add one item to the set using add().
fruits = {"apple", "banana", "mango"}
fruits.add("orange")
print(fruits)


# Q6. Add multiple items to the set using update().
fruits = {"apple", "banana"}
fruits.update(["mango", "orange", "grapes"])
print(fruits)


# Q7. Remove "banana" using remove().
fruits = {"apple", "banana", "mango"}
fruits.remove("banana")
print(fruits)


# Q8. Remove "banana" using discard().
fruits = {"apple", "banana", "mango"}
fruits.discard("banana")
print(fruits)


# Q9. Use discard() with an item that does not exist.
# It will not give an error.
fruits = {"apple", "banana", "mango"}
fruits.discard("orange")
print(fruits)


# Q10. Remove an arbitrary item using pop().
fruits = {"apple", "banana", "mango"}
fruits.pop()
print(fruits)


# Q11. Find the union of two sets.
set1 = {1, 2, 3}
set2 = {3, 4, 5}

result = set1.union(set2)
print(result)


# Q12. Find the union using the | operator.
set1 = {1, 2, 3}
set2 = {3, 4, 5}

print(set1 | set2)


# Q13. Find the intersection of two sets.
set1 = {1, 2, 3}
set2 = {3, 4, 5}

result = set1.intersection(set2)
print(result)


# Q14. Find the intersection using the & operator.
set1 = {1, 2, 3}
set2 = {3, 4, 5}

print(set1 & set2)


# Q15. Find the difference between two sets.
set1 = {1, 2, 3}
set2 = {3, 4, 5}

result = set1.difference(set2)
print(result)


# Q16. Find the difference using the - operator.
set1 = {1, 2, 3}
set2 = {3, 4, 5}

print(set1 - set2)


# Q17. Check whether an item exists in a set.
fruits = {"apple", "banana", "mango"}
print("banana" in fruits)


# Q18. Remove all items from the set using clear().
fruits = {"apple", "banana", "mango"}
fruits.clear()
print(fruits)

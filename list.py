# Creating an empty list
my_list = []

# Creating a list with elements
fruits = ["apple", "banana", "cherry"]



print(fruits[0])  # Output: apple
print(fruits[1])  # Output: banana



print(fruits[-1])  # Output: cherry
print(fruits[-2])  # Output: banana


fruits[1] = "blueberry"
print(fruits)  # Output: ['apple', 'blueberry', 'cherry']



# Adding an element at the end
fruits.append("mango")
print(fruits)  # Output: ['apple', 'blueberry', 'cherry', 'mango']

# Adding an element at a specific index
fruits.insert(1, "grape")
print(fruits)  # Output: ['apple', 'grape', 'blueberry', 'cherry', 'mango']

# Extending a list with another list
fruits.extend(["pear", "orange"])
print(fruits)  # Output: ['apple', 'grape', 'blueberry', 'cherry', 'mango', 'pear', 'orange']


# Remove by value
fruits.remove("blueberry")
print(fruits)  # Output: ['apple', 'grape', 'cherry', 'mango', 'pear', 'orange']

# Remove by index
fruits.pop(2)  # Remove the element at index 2 (cherry)
print(fruits)  # Output: ['apple', 'grape', 'mango', 'pear', 'orange']

# Using del to delete an element
del fruits[1]
print(fruits)  # Output: ['apple', 'mango', 'pear', 'orange']




# Remove by value
fruits.remove("blueberry")
print(fruits)  # Output: ['apple', 'grape', 'cherry', 'mango', 'pear', 'orange']

# Remove by index
fruits.pop(2)  # Remove the element at index 2 (cherry)
print(fruits)  # Output: ['apple', 'grape', 'mango', 'pear', 'orange']

# Using del to delete an element
del fruits[1]
print(fruits)  # Output: ['apple', 'mango', 'pear', 'orange']




# Syntax: list[start:end:step]
print(fruits[1:4])  # Output: ['mango', 'pear', 'orange']
print(fruits[:3])   # Output: ['apple', 'mango', 'pear']
print(fruits[::2])  # Output: ['apple', 'pear']



new_fruits = ["peach", "plum"]
combined_fruits = fruits + new_fruits
print(combined_fruits)  # Output: ['apple', 'mango', 'pear', 'orange', 'peach', 'plum']



repeated_fruits = fruits * 2
print(repeated_fruits)  # Output: ['apple', 'mango', 'pear', 'orange', 'apple', 'mango', 'pear', 'orange']




# Squaring each number in a list
numbers = [1, 2, 3, 4]
squares = [x**2 for x in numbers]
print(squares)  # Output: [1, 4, 9, 16]

# Filtering even numbers
even_numbers = [x for x in numbers if x % 2 == 0]
print(even_numbers)  # Output: [2, 4]




# Sorting a list
numbers = [5, 3, 8, 1]
numbers.sort()
print(numbers)  # Output: [1, 3, 5, 8]

# Reversing a list
numbers.reverse()
print(numbers)  # Output: [8, 5, 3, 1]

# Finding the index of an element
index = numbers.index(5)
print(index)  # Output: 1

# Counting the occurrences of an element
count = numbers.count(3)
print(count)  # Output: 1

# Length of a list
length = len(numbers)
print(length)  # Output: 4




nested_list = [[1, 2], [3, 4], [5, 6]]
print(nested_list[0])  # Output: [1, 2]
print(nested_list[0][1])  # Output: 2




flat_list = [item for sublist in nested_list for item in sublist]
print(flat_list)  # Output: [1, 2, 3, 4, 5, 6]





mixed_list = [1, "hello", 3.14, True]
print(mixed_list)  # Output: [1, 'hello', 3.14, True]




# Stack
stack = []
stack.append(1)
stack.append(2)
stack.append(3)
print(stack.pop())  # Output: 3

# Queue
queue = []
queue.append(1)
queue.append(2)
queue.append(3)
print(queue.pop(0))  # Output: 1







fruits = ["apple", "banana", "cherry"]
removed_element = fruits.pop(1)
print(fruits)  # Output: ['apple', 'cherry']
print(removed_element)  # Output: 'banana'

# Remove the last element
last_fruit = fruits.pop()
print(fruits)  # Output: ['apple']
print(last_fruit)  # Output: 'cherry'



fruits = ["apple", "banana"]
other_fruits = ["grape", "orange"]
fruits.extend(other_fruits)
print(fruits)  # Output: ['apple', 'banana', 'grape', 'orange']



fruits = ["apple", "banana", "cherry"]
fruits.clear()
print(fruits)  # Output: []




fruits = ["apple", "banana", "cherry"]
removed_element = fruits.pop(1)
print(fruits)  # Output: ['apple', 'cherry']
print(removed_element)  # Output: 'banana'

# Remove the last element
last_fruit = fruits.pop()
print(fruits)  # Output: ['apple']
print(last_fruit)  # Output: 'cherry'


fruits = ["apple", "banana"]
other_fruits = ["grape", "orange"]
fruits += other_fruits
print(fruits)  # Output: ['apple', 'banana', 'grape', 'orange']


fruits = ["apple", "banana"]
other_fruits = ["grape", "orange"]
fruits.extend(other_fruits)
print(fruits)  # Output: ['apple', 'banana', 'grape', 'orange']

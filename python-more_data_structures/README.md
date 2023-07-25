<img src="https://miro.medium.com/v2/resize:fit:800/1*dFTVCUWG5MM9xJ5LpnFh-g.png">

#Python - More Data Structures: Set, Dictionary
In Python, sets and dictionaries are two important data structures that provide powerful ways to manage and manipulate data. Understanding how to use sets and dictionaries effectively can greatly enhance your ability to work with data in Python.

## Sets
A set is an unordered collection of unique elements. It is defined using curly braces {} or the set() function. Here are some key features of sets:

- Sets do not allow duplicate elements. If you try to add a duplicate element, it will be ignored.
- Sets are mutable, meaning you can add or remove elements from a set after it is created.
- Sets are unordered, which means that the elements have no specific order.

```Python
# Creating a set using curly braces
fruits = {'apple', 'banana', 'orange'}

# Creating a set using the set() function
colors = set(['red', 'blue', 'green'])
```

## Dictionaries
A dictionary is an unordered collection of key-value pairs. Each key in a dictionary is unique and maps to a value. Dictionaries are defined using curly braces {} and colons : to separate keys and values.

```Python
# Creating a dictionary
person = {
    'name': 'John Doe',
    'age': 30,
    'occupation': 'Engineer'
}
```
https://intranet.alxswe.com/rltoken/gMupLEVx--wpeBGaXolQzA
https://intranet.alxswe.com/rltoken/Gu5vy0GcihvtPt3lg0K8Jg
Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

General
Why Python programming is awesome
What are set and how to use them
What are the most common methods of set and how to use them
When to use sets versus lists
How to iterate into a set
What are dictionary and how to use them
When to use dictionaries versus lists or sets
What is a key in a dictionary
How to iterate into a dictionary
What is a lambda function
What is map, reduce and filter functions
Requirements
General
Recommended editor: Visual studio code
All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.4.3)
All your files should end with a new line
A README.md file, at the root of the folder of the project, is mandatory
Your code should use the PEP 8 style (version 1.7.*)
The length of your files will be tested using wc
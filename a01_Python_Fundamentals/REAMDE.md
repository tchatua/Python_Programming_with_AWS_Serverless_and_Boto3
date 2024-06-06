# Python Fundamentals: Core Concept

## What is Python

### Data types

- Integer (int)
```py
my_integer = 39
``` 
- Floating-Point Number (float)
    - Floating numbers are specified with a decimal point
```py
my_float = 75.412
``` 

- String (str)
    - Strings are sequences of character data 
```py
instance_type = 't2.micro'
``` 

- Boolean (bool)
    - One of two values, True or False
```py
is_on = True
```
### Operators: +, /, -, *

- Assignement 
    - Operator used to assign values to variables.
```py
number = 10
```

- Comparison:
    - Compare values and return if the comparison is true or false
```py
number_1 = 121
number_2 = 39

if number_1 == number_2:
    print(f"{number_1} is equal to {number_2}.")
```

- **Membership**
    - Can be used to test whether a value is a member of a sequence, like strings, lists, or tuples.
```py
sentence = "Welcome to the world of python programming" 
word = "python"

if word in sentence:
    print(f"The word '{word}' is in the sentence".)
```

- Arithmetic
    - Can be used to concatenated strings
```py
greeting = "Hello, "
name = "World!"
message = greeting + name
```

- Logical
    - Can be used to combine conditional statement
```py
number = 15

if number > 10 and number < 20:
    print(f"{number} is between 10 and 20.")
```

- **List in Python**
```py
shopping_list = [
    'eggs', 'flour', 'spinach', 'onions', 'mushrooms', 'tomatoes'
]
```
- **Dictionaries**
```py
baked_dish_fillings = {
    "quiche": "eggs, cream, cheese, spinach, onions, and mushrooms"
    "empanadas": "ground beef, vegetables, and spices"
    "chicken pot pie": "chicken, vegetables, and"
}

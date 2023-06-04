#A program to explain my understanding of Arguments passing.

# Explanation of argument passing
explanation = "In Python, an argument is a value that is accepted by a function. It is a variable, value or object passed to a function as input when it is called."

# Examples of argument passing
example1 = "1. Passing a value to a function:"
example1_code = "def show_number(num):\n       print(num)\n\n   show_number(10)"
example1_explanation = 'In this example, the function has a placeholder of num. A value must passed as argument to this function when it is called' 

example2 = "2. Passing multiple values to a function:"
example2_code = "   def add_numbers(a, b):\n       print(a + b)"
example2_explanation = ''' The above function takes, or accepts multiple input values as a, and b. It adds the values and prints the result. When an integer is passed,
a, and b is computed and the result is a number, but when a string is passed, it cocantenates them into one string.'''


example3 = "3. Passing arguments by position:"
example3_code = "   def greet(name, age):\n       print(f'Hello, {name}! You are {age} years old.')\n\n   greet('Alice', 25)"
example3_explanation = "This code defines a function called greet that takes two arguments: name and age. \
The function then prints a message that greets the person by name and tells them their age. \
The function is then called with the arguments 'Alice' and 25, which will print the message: "
# Print the explanation and examples
print("Explanation of argument passing:")
print(explanation)
print()
print("Examples of argument passing:")
print(example1)
print(example1_code)
print(example1_explanation)
print()
print(example2)
print(example2_code)
print(example2_explanation)
print()
print(example3)
print(example3_code)
print(example3_explanation)

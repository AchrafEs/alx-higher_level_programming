`0x04-loops_conditions_and_parsing`

In Bash, loops, conditions, and parsing are essential concepts for controlling the flow of execution and manipulating
data within shell scripts. Let's take a closer look at each of these concepts:

1. `Loops:`

Loops allow you to repeatedly execute a block of code until a certain condition is met. In Bash, there are mainly
two types of loops: the for loop and the while loop.

`For loop:`
The for loop iterates over a list of items and executes a block of code for each item in the list.
The basic syntax is as follows:
```
for item in list
do
    # Code to be executed for each item
done
```
Exemple:
```
for fruit in apple banana orange
do
    echo "I like $fruit"
done
```
Output:
```
I like apple
I like banana
I like orange
```
`while loop`
The while loop executes a block of code as long as a specified condition is true. The basic syntax is as follows:
```
while condition
do
    # Code to be executed while the condition is true
done
```
Example:
```
count=1
while [ $count -le 5 ]
do
    echo "Count is $count"
    ((count++))
done
```
Output:
```
Count is 1
Count is 2
Count is 3
Count is 4
Count is 5
```

2. `Conditions:`

Conditions in Bash are used to make decisions based on the evaluation of certain expressions.
The most commonly used construct for conditions is the if statement.

`if` statement:
The if statement allows you to execute different blocks of code based on the evaluation of a condition.
The basic syntax is as follows:
```
if condition
then
    # Code to be executed if the condition is true
else
    # Code to be executed if the condition is false (optional)
fi
```
Example:
```
read -p "Enter a number: " num

if [ $num -gt 0 ]
then
    echo "The number is positive."
else
    echo "The number is non-positive."
fi
```
3. `Parsing:`

Parsing in Bash refers to the process of extracting and manipulating data from strings or files. Bash provides
various tools for parsing, such as string manipulation, pattern matching, and command substitution.

String manipulation:

You can extract substrings from a string using parameter expansion or manipulate strings with various string-related
commands.
```
str="Hello, World!"
echo ${str:0:5}  # Output: "Hello"
```
Pattern matching:

Pattern matching allows you to check if a string matches a specific pattern using wildcards. The most common
wildcard characters are * (matches zero or more characters) and ? (matches any single character).
```
if [[ "$str" == H* ]]
then
    echo "String starts with 'H'"
fi
```
Command substitution:

Command substitution lets you use the output of a command as input for another command or assign it to a variable.
```
files_count=$(ls | wc -l)
echo "Number of files in the current directory: $files_count"
```
These concepts, loops, conditions, and parsing, are fundamental to creating powerful and flexible Bash scripts.
They allow you to control the execution flow and handle data efficiently, making Bash a versatile tool for automating
various tasks in the command line environment.

`0x04-python-more_data_structures:`

1.  `Lambda:`

     A lambda function is a small and anonymous function in Python. It's called anonymous
     because it doesn't have a name. Think of it as a mini-function that you can define on
     the spot without giving it a permanent name. It's useful when you need a function for
     a specific task, but you don't want to create a whole separate function for it.

For example, let's say you want to multiply a number by 2. You can define a lambda function like this:

		```python
		multiply_by_two = lambda x: x * 2
		```

     Here, lambda x means the function takes an input x, and x * 2 is the operation it performs.
     So, if you use multiply_by_two(5), it will return 10 because 5 multiplied by 2 is 10.

2.  `Filter:`

     The filter function is used to filter out elements from a list or sequence based on a specific condition.
     It takes two arguments: a function and a list. The function specifies the condition, and the list
     contains the elements that need to be filtered.

For example, let's say you have a list of numbers [1, 2, 3, 4, 5], and you want to filter out only
the even numbers. You can use the filter function like this:

		```python
		numbers = [1, 2, 3, 4, 5]
		even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
		```

     Here, lambda x: x % 2 == 0 is the condition for filtering. It checks if a number is divisible
     by 2 without leaving a remainder (i.e., it's an even number). The filter function returns
     a new list containing only the even numbers, which will be [2, 4] in this case.

3.  `Reduce:`

     The reduce function is used to apply a specific operation to a sequence of elements and reduce them
     to a single value. It takes two arguments: a function and a list.
     The function specifies the operation to be performed, and the list contains the elements to be reduced.

For example, let's say you have a list of numbers [1, 2, 3, 4, 5], and you want to find the sum of all the
numbers using the reduce function. You can do it like this:

		```python
		from functools import reduce

		numbers = [1, 2, 3, 4, 5]
		sum_of_numbers = reduce(lambda x, y: x + y, numbers)
		```

     Here, lambda x, y: x + y is the operation to be performed. It takes two numbers x and y and adds them
     together. The reduce function applies this operation to the list, starting from the left, and reduces
     it to a single value. In this case, the sum of all the numbers will be 15.

4.  `Map:`

     The map function is used to apply a specific function to each element of a list or sequence and returns
     a new list containing the results. It takes two arguments: a function and a list. The function specifies
     the operation to be performed, and the list contains the elements to which the function is applied.

For example, let's say you have a list of numbers [1, 2, 3, 4, 5], and you want to double each number using
the map function. You can do it like this:

		```python
		numbers = [1, 2, 3, 4, 5]
		doubled_numbers
		```

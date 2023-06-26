`0x05-python-exceptions`

In Python, exceptions are a way to handle errors or exceptional situations that may occur during the execution
of a program. When an error occurs, Python raises an exception, which can be caught and handled by the program,
preventing it from crashing.

Exceptions provide a mechanism for separating normal program flow from error handling code.
By using exception handling, you can anticipate and handle errors gracefully, ensuring that your program doesn't
terminate abruptly.

The basic structure of exception handling in Python involves three keywords: `try`, `except`, and optionally `finally`.

1.  `try`: The try block is used to enclose the code that might raise an exception. It is the block of code where
    you expect a potential error to occur.

2.  `except`: The except block follows the try block and specifies the type of exception that you want to catch.
    If an exception of that type (or any of its subclasses) occurs in the try block, the corresponding except
    block is executed. You can have multiple except blocks to handle different types of exceptions.

3.  `finally`: The finally block is optional and follows the except block(s). It contains code that will be executed
    regardless of whether an exception occurred or not. The finally block is typically used to perform cleanup tasks,
    such as closing files or releasing resources.

Exception handling is a powerful feature of Python that allows you to gracefully handle errors and control the flow
of your program even in the presence of unexpected events. By catching and handling exceptions appropriately, you
can make your code more robust and user-friendly.

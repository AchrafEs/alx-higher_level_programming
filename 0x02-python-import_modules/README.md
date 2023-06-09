`0x02-python-import_modules`


In Python, modules are like toolboxes that contain different sets of tools that you can use
to make your code more powerful and efficient. These tools are called functions, and they are
pre-written blocks of code that perform specific tasks.


When you want to use a module in your code, you need to tell Python that you want to use
it by using the import keyword. It's like asking Python to bring
that toolbox to you so you can use the tools inside.


For example, let's say you want to use a module called "math" to do some mathematical calculations.
To bring in the "math" module, you would write import math at the beginning of your code.


Once you import a module, you can use the functions inside it by referring to the module
name followed by a dot (.) and then the name of the function. For example, if you want to
use the square root function from the "math" module, you would write `math.sqrt()`.


Here's an example that shows how to use the "math" module to calculate the square root of a number:


                                  import math

                                  number = 16
                                  result = math.sqrt(number)

                                  print(result)


In this code, we imported the "math" module, then we used the sqrt() function from the "math" module
to calculate the square root of the number 16. The result is then printed out.


Modules can do many different things, like working with dates and times, handling files,
creating graphicaluser interfaces, and much more. They help you avoid writing the same code
over and over again by providing ready-to-use functions.


So, by importing modules, you can access and use these functions to make your code more powerful and to
perform a wide range of tasks without having to write everything from scratch.

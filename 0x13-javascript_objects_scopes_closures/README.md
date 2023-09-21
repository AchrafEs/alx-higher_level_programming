### 0x13. JavaScript - Objects, Scopes and Closures

JavaScript is a versatile and widely-used programming language that is primarily used for web development. Objects
scopes, and closures are fundamental concepts in JavaScript that play crucial roles in how the language works.
Let's break down each of these concepts:

1. `Objects:`
	Objects in JavaScript are data structures that allow you to store and organize related data and functions.
They are collections of key-value pairs where keys are called properties, and values can be of any data type, including
other objects or functions. Objects can be created using object literals, constructors, or classes
(introduced in ECMAScript 6).
Example of creating an object:
```
const person = {
    firstName: "John",
    lastName: "Doe",
    sayHello: function() {
        console.log(`Hello, my name is ${this.firstName} ${this.lastName}`);
    }
};
```
You can access object properties and methods using dot notation (person.firstName) or bracket notation
(person['firstName']).
```
console.log(person.firstName); // John
person.sayHello(); // Hello, my name is John Doe.
```

2. `Scopes:`
	Scopes in JavaScript define the accessibility and lifetime of variables and functions. JavaScript has two main
types of scope:
`Global Scope:` Variables declared outside of any function or block have global scope and can be accessed from
anywhere in the code.
`Local Scope:` Variables declared inside a function have local scope and are only accessible within that function.
Block-scoped variables, introduced with let and const, are confined to the block they are declared in.

Example of variable scope:
```
const globalVar = "I'm global"; // Global variable

function exampleFunction() {
    const localVar = "I'm local"; // Local variable
    console.log(globalVar); // Access global variable
    console.log(localVar); // Access local variable
}

exampleFunction();
console.log(globalVar); // Access global variable
console.log(localVar); // Error - localVar is not defined
```
Understanding scope is essential to prevent variable conflicts and manage variable lifetimes effectively.

3. `Closures:`
Closures are a powerful and somewhat advanced concept in JavaScript. A closure is created when a function is defined
inside another function (the outer function) and has access to the outer function's variables. Closures allow inner
functions to "remember" the environment in which they were created, even after the outer function has finished executing.

Example of a closure:
```
function outerFunction() {
    const outerVar = "I'm from outer function";

    function innerFunction() {
        console.log(outerVar); // Access outerVar from the outer function
    }

    return innerFunction;
}

const closure = outerFunction();
closure(); // Prints "I'm from outer function"
```
In this example, `innerFunction` forms a closure and retains access to `outerVar` even after `outerFunction` has
completed execution.

Closures are commonly used for encapsulation, data privacy, and creating functions that "remember" their context.
Understanding these three fundamental concepts—Objects, Scopes, and Closures—will help you become proficient
in JavaScript development.

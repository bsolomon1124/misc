## JavaScript, Its Cousins, and the Environment

https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/JavaScript_basics

- JavaScript runs
	- in the browser
	- on the server (Node.js)
	- in a variety of native modes on devices (React Native)
	- "the only true cross-platform game in town"

- Browsers load and execute JavaScript as it is found sequentially within HTML
- If you view the source code of a page in the browser that uses JavaScript, the JavaScript will not have changed the HTML, because the script works with the model of the web page that the browser has created
- Statements: end with semicolon
	- A JavaScript **script** (`.js`) is composed of statements
	- Examples:
		- `1;`
		- `false;`
	- A aprogram is a listof statements
- A code **block** is surrounded by brackets (curly braces), and can consist of multiple statements
	- group any number of statements into a single statement, called a block
- Expression: evaluates into a single value
	- A fragment of code that produces a value is called an expression.
	- Every value that is written literally (such as 22 or "psychoanalysis") is an expression. An expression between parentheses is also an expression, as is a binary operator applied to two expressions or a unary operator applied to one.

## Hello world

```javascript
function hello() {
	console.log("hello world");
}
hello();
```

```javascript
var hr = new Date().getHours(); // assignment
var greeting; // declaration without assignment; greeting is *undefined* (special value)

if (hr > 18) {
	greeting = 'Good evening'; // A statement
} else if (hr > 12) {
	greeting = 'Good afternoon'; // single or double quotes OK
} else if (hr > 0) {
	greeting = 'Good morning';
} else {
	greeting = 'Welcome';
}

document.write('<h3>' + greeting + '</h3>');
```

```javascript
/* C-style comments
   are OK too 
*/
var price = 5, quantity = 14;
var total = price * quantity;

// Fetches a tag that has <tagname id="cost"...>
var el = document.getElementById('cost');
// Replace the existing content
el.textContent = '$' + total;
```

```javascript
var inStock = true;
var shipping = false;

// Set the `class=xxx` attribute of the retrieved tag
// (Which is assumed to trigger some CSS rule - true
// shows a check, false shows an X)
var elStock = document.getElementById('stock')
elStock.className = inStock;
var elShip = document.getElementById('shipping')
elShip.className = shipping
````

## Data Types

- Number - 64 bit int & float
	Infinity, -Infinity, NaN
- String
	- You can use single quotes, double quotes, or backticks to mark strings
	- UTF-16: describes most common characters using a single 16-bit code unit but uses a pair of two such units for others (surrogates)
	- "con" + "cat" + "e" + "nate"
	- backtick-quotoed strings also called template literals - `half of 100 is ${100 / 2}`
- Boolean (`true`, `false`)
- Array
	- May be heterogeneous data types
	- 0-indexed
	- Property: `.length`
	- Members support (re)assignment
- NaN

Special values:
- `null`
- `undefined`
	- Basically interchaangeable

"Aggressive" automatic type conversion (type coercion):

```javascript
console.log("5" - 1)
-> 4
````

```javascript
// Array literal - can also write on separate lines
var colors = ['white', 'black', 'grey'];
document.getElementById('colors').textContent = colors[0];

// Array constructor (prefer the literal)
var other = new Array('purple',
                      'blue',
                      'green');
document.getElementById('colors').textContent = other.item(0);  // same as [0]
```

## Objects / Data Structures

```javascript
let sequence = [1, 2, 3];
sequence.push(4);
sequence.push(5);
console.log(sequence);
// → [1, 2, 3, 4, 5]
```

Values of the type **`object`** are arbitrary collections of properties.

```javascript
let day1 = {
  squirrel: false,
  events: ["work", "touched tree", "pizza", "running"]
};

console.log(Object.keys({x: 0, y: 0, z: 2}));
// → ["x", "y", "z"]
```

Objects are mutable

Array: a specialized `object` type

Iterating over an array: shorthand:

```javascript
let arr = ["foo", "bar", "baz"]

for (let i of arr) {
  console.log(i);
}
// foo
// bar
// baz
```

Array methods:

- `.push()`
- `.pop()`
- `.unshift()`
- `.shift()`
- `.indexOf()`
- `.lastIndexOf()`
- `.slice()`
- `.concat()`
- `.forEach()`
filter
map
reduce
some
findIndex


```javascript
["A", "B"].forEach(l => console.log(l));
// → A
// → B
```

## Properties

Example:

`myString.length`
`Math.max`

Access via dot or brackets, `value.x` or `values[x]`

### Constructor Functions

A constructor function is like a Python `__init__()` method - it creates an instance of a class.

```javascript
let protoRabbit = {
  speak(line) {
    console.log(`The ${this.type} rabbit says '${line}'`);
  }
};

function makeRabbit(type) {
  let rabbit = Object.create(protoRabbit);
  rabbit.type = type;
  return rabbit;
}
```

The easier version of the above: putting `new` in front of a function call will treat the function as a constructor:

```javascript
function Rabbit(type) {
  this.type = type;
}
Rabbit.prototype.speak = function(line) {
  console.log(`The ${this.type} rabbit says '${line}'`);
};

let weirdRabbit = new Rabbit("weird");
```

The even-less-awkward notation:

```javascript
class Rabbit {
  constructor(type) {
    this.type = type;
  }
  speak(line) {
    console.log(`The ${this.type} rabbit says '${line}'`);
  }
}

let killerRabbit = new Rabbit("killer");
let blackRabbit = new Rabbit("black");
```


### Prototypes

In addition to their set of properties, most objects also have a prototype. A prototype is another object that is used as a fallback source of properties. When an object gets a request for a property that it does not have, its prototype will be searched for the property, then the prototype’s prototype, and so on.

So who is the prototype of that empty object? It is the great ancestral prototype, the entity behind almost all objects, Object.prototype.

## Maps

A `map` behaves like a Python `dict`:

```
let ages = {
  Boris: 39,
  Liang: 22,
  Júlia: 62
};
```

The above is dangerous, though, because plain objects derive from `Object.prototype`:

```javascript
console.log("Is toString's age known?", "toString" in ages);
// → Is toString's age known? true
```

Alternative: use the `Map` class:

```javascript
let ages = new Map();
ages.set("Boris", 39);
ages.set("Liang", 22);
ages.set("Júlia", 62);
```

## Getters, Setters, and Statics

Getters - like a Python `property`:

```javascript
let varyingSize = {
  get size() {
    return Math.floor(Math.random() * 100);
  }
};

console.log(varyingSize.size);
// → 73
console.log(varyingSize.size);
// → 49
```

The `Temperature` class below allows you to read and write the temperature in either degrees Celsius or degrees Fahrenheit, but internally it stores only Celsius and automatically converts to and from Celsius in the fahrenheit getter and setter:

```javascript
class Temperature {
  constructor(celsius) {
    this.celsius = celsius;
  }
  get fahrenheit() {
    return this.celsius * 1.8 + 32;
  }
  set fahrenheit(value) {
    this.celsius = (value - 32) / 1.8;
  }

  static fromFahrenheit(value) {
    return new Temperature((value - 32) / 1.8);
  }
}

let temp = new Temperature(22);
console.log(temp.fahrenheit);
// → 71.6
temp.fahrenheit = 86;
console.log(temp.celsius);
// → 30
```

## Variables

- Declaration versus assignment
- Allowed syntax

```javascript
let mood = "light";
console.log(mood);
// → light
mood = "dark";
console.log(mood);
// → dark
```



### `let` vs `var` vs `const`

`var`: the way bindings were declared in pre-2015 JavaScript
	- "it has some confusing properties"


## Keywords & Reserved Words

```
break case catch class const continue debugger default
delete do else enum export extends false finally for
function if implements import interface in instanceof let
new package private protected public return static super
switch this throw true try typeof var void while with yield
```

## The JavaScript Environment


The collection of bindings and their values that exist at a given time is called the environment. When a program starts up, this environment is not empty. It always contains bindings that are part of the language standard, and most of the time, it also has bindings that provide ways to interact with the surrounding system. For example, in a browser, there are functions to interact with the currently loaded website and to read mouse and keyboard input.

Examples:

`console.log()`
	- In browsers, the output lands in the JavaScript console. This part of the browser interface is hidden by default
`prompt()`

let x = 30;
console.log("the value of x is", x);

## Functions

- A return keyword without an expression after it will cause the function to return undefined. Functions that don’t have a return statement at all, similarly return undefined.

```javascript
const square = function(x) {
  return x * x;
};

const power = function(base, exponent) {
  let result = 1;
  for (let count = 0; count < exponent; count++) {
    result *= base;
  }
  return result;
};

function power(base, exponent = 2) {
  let result = 1;
  for (let count = 0; count < exponent; count++) {
    result *= base;
  }
  return result;
}

// Function *declaration* (no terminating semicolon here, no leading 'const')
function square(x) {
  return x * x;
}
```

```javascript
console.log("The future says:", future());

function future() {
  return "You'll never have flying cars";
}
```

The preceding code works, even though the function is defined below the code that uses it. Function declarations are not part of the regular top-to-bottom flow of control. They are conceptually moved to the top of their scope and can be used by all the code in that scope.

Arrow functions:

```javascript
const power = (base, exponent) => {
  let result = 1;
  for (let count = 0; count < exponent; count++) {
    result *= base;
  }
  return result;
};
```

When there is only one parameter name, you can omit the parentheses around the parameter list. If the body is a single expression, rather than a block in braces, that expression will be returned from the function. So, these two definitions of square do the same thing:

```javascript
const square1 = (x) => { return x * x; };
const square2 = x => x * x;
```

### Variadic Arguments

```javascript
function max(...numbers) {
  let result = -Infinity;
  for (let number of numbers) {
    if (number > result) {
      result = number;
    }
  }
  return result;
}
console.log(max(4, 1, 9, -2));
// → 9
```

### Higher-Order Functions

A function is just a value:

```javascript
function repeat(n, action) {
  for (let i = 0; i < n; i++) {
    action(i);
  }
}

repeat(3, console.log);
// → 0
// → 1
// → 2
```

Fancier example using an **arrow function**:

```javascript
let labels = [];
repeat(5, i => {
  labels.push(`Unit ${i + 1}`);
});
console.log(labels);
// → ["Unit 1", "Unit 2", "Unit 3", "Unit 4", "Unit 5"]
````

Function factory:

```javascript
function greaterThan(n) {
  return m => m > n;
}
let greaterThan10 = greaterThan(10);
console.log(greaterThan10(11));
// → true
```

Decorators:

```javascript
function noisy(f) {
  return (...args) => {
    console.log("calling with", args);
    let result = f(...args);
    console.log("called with", args, ", returned", result);
    return result;
  };
}
noisy(Math.min)(3, 2, 1);
// → calling with [3, 2, 1]
// → called with [3, 2, 1] , returned 1
```

## Scope

## Methods

```javascript
let rabbit = {};
rabbit.speak = function(line) {
  console.log(`The rabbit says '${line}'`);
};
```

Usually a method needs to do something with the object it was called on. When a function is called as a method—looked up as a property and immediately called, as in object.method()—the binding called this in its body automatically points at the object that it was called on.

```javascript
function speak(line) {
  console.log(`The ${this.type} rabbit says '${line}'`);
}
let whiteRabbit = {type: "white", speak};
let hungryRabbit = {type: "hungry", speak};

whiteRabbit.speak("Oh my ears and whiskers, " +
                  "how late it's getting!");
// → The white rabbit says 'Oh my ears and whiskers, how
//   late it's getting!'
```

You can think of this as an extra parameter that is passed in a different way. If you want to pass it explicitly, you can use a function’s call method, which takes the this value as its first argument and treats further arguments as normal parameters.

```javascript
speak.call(hungryRabbit, "Burp!");
// → The hungry rabbit says 'Burp!'
```

Arrow functions are different—they do not bind their own this but can see the this binding of the scope around them. Thus, you can do something like the following code, which references this from inside a local function:

```javascript
function normalize() {
  console.log(this.coords.map(n => n / this.length));
}
normalize.call({coords: [0, 2, 3], length: 5});
// → [0, 0.4, 0.6]
```

Shorthand way of defining a method:

```javascript
let protoRabbit = {
  speak(line) {
    console.log(`The ${this.type} rabbit says '${line}'`);
  }
};
```

## Conventions/Style

- `camelCase`

## Operators

- `+` (also valid for string concatenation)
	- If you add a number + string, the result is a string
- `-`
- `/`
- `*`
- `++`
- `--`
- `%`
- `typeof` - unary operator

Logical:
- `&&` (binary and)
- `||` (binary or)
- `!` (unary not)
- `?:` (ternary): `true ? 1 : 2`, `false ? 1 : 2`
- Supports short-circuiting




Order of operations:
- multiplication/division
- addition/subtraction

## Events

## Functions

```javascript
function updateMessage() { // function declaration; updateMessage() is the function identifier
	var msg = 'Sign up to receive a shit ton of emails';
	document.getElementById('message').textContent = msg;
}

var getArea(height, width) {
	return height * width;
}
console.log(getArea(5, 4));
```

A function may be called before it has been declared.  This is because the interpreter parses the entire script before doing any execution.

Parameters: used in the function declaration
Arguments: what you supply in the place of parameters when calling the function

## Control Flow

```javascript
let number = 0;
while (number <= 12) {
  console.log(number);
  number = number + 2;
}
```

```javascript
let num = Number(prompt("Pick a number"));

if (num < 10) {
  console.log("Small");
} else if (num < 100) {
  console.log("Medium");
} else {
  console.log("Large");
}
```

A do loop is a control structure similar to a while loop. It differs only on one point: a do loop always executes its body at least once, and it starts testing whether it should stop only after that first execution:

```javascript
let yourName;
do {
  yourName = prompt("Who are you?");
} while (!yourName);
console.log(yourName);
```


```javascript
for (let number = 0; number <= 12; number += 2) {
  console.log(number);
}
```

```javascript
switch (prompt("What is the weather like?")) {
  case "rainy":
    console.log("Remember to bring an umbrella.");
    break;
  case "sunny":
    console.log("Dress lightly.");
  case "cloudy":
    console.log("Go outside.");
    break;
  default:
    console.log("Unknown weather type!");
    break;
}
```

## Conventions

`fuzzyLittleTurtle`, except for constructors, such as `Number`, where first letter is capitalized.

## JavaScript Is Liberal

```javascript

console.log("5" - 1)
// -> 4

function square(x) { return x * x; }
console.log(square(4, true, "hedgehog"));
// → 16

let dne = {
	a: 5
}
console.log(dne.b)
// -> undefined
```

- If you pass concat an argument that is not an array, that value will be added to the new array as if it were a one-element array.
	- That is, concat behaves like Python's append and extend at once

No truly private methods - `_methodName()` is only quasi-private

## Raising an Exception

```javascript
function promptDirection(question) {
  let result = prompt(question);
  if (result.toLowerCase() == "left") return "L";
  if (result.toLowerCase() == "right") return "R";
  throw new Error("Invalid direction: " + result);
}

function look() {
  if (promptDirection("Which way?") == "L") {
    return "a house";
  } else {
    return "two angry bears";
  }
}

try {
  console.log("You see", look());
} catch (error) {
  console.log("Something went wrong: " + error);
}
```

## Debugging

- `"use strict";`
- TypeScript

## Modules

Modules are an attempt to avoid these problems. A module is a piece of program that specifies which other pieces it relies on and which functionality it provides for other modules to use (its interface).

A package is a chunk of code that can be distributed (copied and installed). It may contain one or more modules and has information about which other packages it depends on. A package also usually comes with documentation explaining what it does so that people who didn’t write it might still be able to use it.

We need a place to store and find packages and a convenient way to install and upgrade them. In the JavaScript world, this infrastructure is provided by NPM (https://npmjs.org).  NPM is two things:

1. an online service where one can download (and upload) packages
2. a program (bundled with Node.js) that helps you install and manage them.

This is the "old-school" (improvised) way to simulate a module, pre-2015:

```javascript
const weekDay = function() {
  const names = ["Sunday", "Monday", "Tuesday", "Wednesday",
                 "Thursday", "Friday", "Saturday"];
  return {
    name(number) { return names[number]; },
    number(name) { return names.indexOf(name); }
  };
}();
```

The approach above is "mostly obsolete now."

(It seems that) JavaScript thinks about modules a little differently:

> This is precisely what we need for a module system. We can wrap the module’s code in a function and use that function’s scope as module scope.

The most widely used approach to bolted-on JavaScript modules is called CommonJS modules. Node.js uses it and is the system used by most packages on NPM.

The main concept in CommonJS modules is a function called require. When you call this with the module name of a dependency, it makes sure the module is loaded and returns its interface.

Because the loader wraps the module code in a function, modules automatically get their own local scope. [It is otherwise global!]

All they have to do is:

1. call `require` to access their dependencies
2. put their interface in the object bound to `exports`

Importing (requiring):

```javascript
const ordinal = require("ordinal");
const {days, months} = require("date-names");

exports.formatDate = function(date, format) {
  return format.replace(/YYYY|M(MMM)?|Do?|dddd/g, tag => {
    if (tag == "YYYY") return date.getFullYear();
    if (tag == "M") return date.getMonth();
    if (tag == "MMMM") return months[date.getMonth()];
    if (tag == "D") return date.getDate();
    if (tag == "Do") return ordinal(date.getDate());
    if (tag == "dddd") return days[date.getDay()];
  });
};
```

## JavaScript and the Browser

https://eloquentjavascript.net/13_browser.html
https://eloquentjavascript.net/14_dom.html

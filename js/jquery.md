# jQuery

Home page: https://jquery.com/

jQuery is a fast, small, and feature-rich JavaScript library. It makes things like HTML document traversal and manipulation, event handling, animation, and Ajax much simpler with an easy-to-use API that works across a multitude of browsers.

## What is the `$`?

It's a reasonable first question.  The `$` is ubiquitous to jQuery:

```javascript
// run code as soon as the document is ready to be manipulated
// (more eager than window.onload!)
$(document).ready(function () {
  $("a").click(function(event) {
    alert("Thanks for visiting!");
  });
});
```

The symbol `$` is a shortcut alias for an object named `jQuery`.

But what is `jQuery`?  [`jQuery`](https://api.jquery.com/jQuery/) is a property of the `window` object, a function that returns matched elements found in the DOM.

Just as you could write:

```javascript
var yourFunction = function() {
  alert('a function');
}

window.Myf = yourFunction;
```

And then call `Myf();`, `jQuery` has been assigned as a property of `window`.

So, these are the same:

```javascript
var divs = $("div");       // Find all divs
var divs = jQuery("div");  // Also find all divs
console.log($ === jQuery); // "true"
```

Some beginner examples:

```javascript
//
$("div.foo");

$( "div.foo" ).click(function() {
  $( "span", this ).addClass( "bar" );
});

// Find all p elements that are children of a div element and apply a border to them.
$( "div > p" ).css( "border", "1px solid gray" );

// Find all inputs of type radio within the first form in the document.
$( "input:radio", document.forms[ 0 ] );

// Set the background color of the page to black.
$( document.body ).css( "background", "black" );

// Hide all the input elements within a form.
$( myForm.elements ).hide();

// Apply CSS to first list item only
$( "li" ).first().css( "background-color", "red" );
```

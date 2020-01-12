# jQuery

jQuery is a client-side JavaScript library for HTML DOM traversal and manipulation, event handling, animation, and Ajax.

- API docs: https://api.jquery.com/
- Tutorial: https://learn.jquery.com/about-jquery/
- GitHub: https://github.com/jquery/jquery
- Download: https://jquery.com/download/
- CDN: https://code.jquery.com/

An excellent book on jQuery is [_jQuery in Action, 3rd edition_](https://www.amazon.com/dp/1617292079) - Bibeault et. al.

## Hello jQuery

This example selects the "body" element(s) and inserts a paragraph into the start of their content:

```html
<!DOCTYPE html>
<html lang="en-US">
  <head>
    <meta charset="utf-8">
    <title>Hello jQuery</title></head>
  <body>
    <script
              src="http://code.jquery.com/jquery-3.4.1.slim.min.js"
              integrity="sha256-pasqAKBDmFT4eHoN2ndd6lN370kFiGUFyTiUHWhU7k8="
              crossorigin="anonymous">
    </script>
    <script>
        // Insert a <p> into beginning of <body>
        $("body").prepend("<p>Hello jQuery!</p>");
    </script>
  </body>
</html>
```

## What is the `$`?

`$` is a shorthand alias for the `jQuery` object, both of which are made available when you source jQuery.

(Quite literally, `$ === jQuery`.)

From the jQuery [source code](https://github.com/jquery/jquery/blob/437f389a24a6bef213d4df507909e7e69062300b/src/exports/global.js#L27):

```javascript
import jQuery from "../core.js";
// ...
window.jQuery = window.$ = jQuery;
```

The `$` is ubiquitous to jQuery.  You can use `jQuery`/`$` as both (1) a function to select elements:

```javascript
> $("title").text()
"Hello jQuery"

> $( "input[name!='newsletter']" ).next().append( "<b>; not newsletter</b>" );
```

... and (2) an object that holds utility functions:

```javascript
> $.trim("   foo   bar  ") // Strip whitespace
"foo   bar"

> $.now() // Return a number representing the current time
1578801409916
```

(In JavaScript, [functions are objects](https://stackoverflow.com/q/7223585/7954504); functions are simply [added to the `jQuery` object](https://github.com/jquery/jquery/blob/d0ce00cdfa680f1f0c38460bc51ea14079ae8b07/src/deprecated.js#L67) as attributes.)

Like many other (almost all) methods in the library, `$()` allows for method chaining.  That is, [`jQuery()` returns a `jQuery` object](https://learn.jquery.com/using-jquery-core/jquery-object/):

```javascript
$( "p" ).css( "color", "red" ).find( ".special" ).css( "color", "green" );

$( "p" ).eq( 0 ) // First paragraph only
```

The returned `jQuery` object contains a set of DOM elements that match the given criteria and also expose many of jQuery’s
methods and properties.

Some more introductory examples:

```javascript
// Select <div class='foo'>
$("div.foo");

// Register a callback on click
$( "div.foo" ).click(function() {
  $( "span", this ).addClass( "bar" );
});

// Find all p elements that are children of a div element and apply a border to them
$( "div > p" ).css( "border", "1px solid gray" );

// Find all inputs of type radio within the first form in the document
$( "input:radio", document.forms[ 0 ] );

// Set the background color of the page to black
$( document.body ).css( "background", "black" );

// Hide all the input elements within a form
$( myForm.elements ).hide();

// Apply CSS to first list item only
$( "li" ).first().css( "background-color", "red" );
```

## Multiple Signatures

`jQuery()` has a [wide range of signatures](https://api.jquery.com/jQuery/).  For instance, in addition to the examples thus far, you can _wrap a native JavaScript object in a jQuery object_:

```javascript
> let tgt = document.getElementById("dom-and-dom-elements");
> tgt
<a id="dom-and-dom-elements" class="icon-link toc-link" href="#dom-and-dom-elements">

> $(tgt) // Wrap
Object { 0: a#dom-and-dom-elements.icon-link.toc-link, context: a#dom-and-dom-elements.icon-link.toc-link, length: 1 }
```

Another signature is `jQuery( selector [, context ] )`.  This allows you to not just select but create elements.

When creating a new element with the `$()` function, you use the `context` parameter to specify the attributes and their values for the element you're creating in the form of a JavaScript object:

```javascript
// Create an <img> element, give it attributes, and attach it to the DOM tree
// as a child of <body>
$('<img>',
  {
    src: 'images/little.bear.png',
    alt: 'Little Bear',
    title:'I woof in your general direction',
    click: function() {
      alert($(this).attr('title'));
  }
})
.appendTo('body');
```

## A Fuller Example

These two jQuery calls serve to add a 'toggle visibility' functionality for passwords and bold/asterisk fields that are required:

```html
<!DOCTYPE html>
<html lang="en-US">
<head>
  <meta charset="utf-8">
  <title>Toggle Password Visibility Demo</title>
</head>
<body>
  <label for="id_password_1">Password 1:</label>
  <input type="password" id="id_password_1">
  <br>
  <label for="id_password_2">Password 2:</label>
  <input type="password" id="id_password_2">
  <br>
  <label for="id_username">Username:</label>
  <input id="id_username" type="text" required>

  <script
          src="https://code.jquery.com/jquery-3.4.1.min.js"
          integrity="sha256-CSXorXvZcTkaix6Yvo6HppcZGetbYMGWSFlBw8HfCJo="
          crossorigin="anonymous"></script>
  <script>
    // Add a checkbox sibling to each password input.  When
    // the checkbox is clicked, toggle the visibility of the
    // password input.
    $("input[type='password']").each(function(index) {
      $(this).after('<input type="checkbox"><span>show</span>');
      $(this).next().click(function() {
        let $pBox = $(this).prev();
        if ($pBox.attr("type") === "password") {
          $pBox.attr("type", "text");
        } else {
          $pBox.attr("type", "password");
        }
      });
    });

    // Make the labels for required fields bold; place
    // an asterisk after them.  label pattern comes from
    // https://docs.djangoproject.com/en/1.11/topics/forms/#form-rendering-options
    $("input[required]").each(function(index) {
      let $i = $(this).attr("id");
      $(`label[for='${$i}']`).css({"font-weight": "bold"}).text(function(i, prevText) {
        return "*" + prevText;
      });
    });
  </script>
</body>
</html>
```

## Selectors

The [`jQUery()`](https://api.jquery.com/jQuery/#jQuery1) function accepts a string containing a CSS selector which is then used to match a set of elements.

There is a wide range of possible selectors, described here:

> https://api.jquery.com/category/selectors/

What follows is an incomplete summary.  Some are from CSS 1-3; others are invented by jQuery:

| Example | Name | Description |
| ------- | ---- | ----------- |
| `*` | [All selector](https://api.jquery.com/all-selector/) | Matches all the elements in the page |
| `#my-id` | [ID selector](https://api.jquery.com/id-selector/) | Matches the element with the ID value of `my-id` |
| `.my-class` | [Class selector](https://api.jquery.com/class-selector/) | Matches all elements with the class `my-class` |
| `a` | [Element selector](https://api.jquery.com/element-selector/) | Matches all anchor (`a`) elements |
| `a.my-class` | [Class selector](https://api.jquery.com/class-selector/) | Matches all anchor (`a`) elements that have the class `my-class` |
| `.cls1.my-cls` | [Class selector](https://api.jquery.com/class-selector/) | Matches all elements with the class `cls1` _and_ class `my-cls` |
| `ul.topnav > li` | [Child selector](https://api.jquery.com/child-selector/) | Matches all direct child elements specified by "li" of elements specified by "ul.topnav" | `form fieldset input` | [Descendant selector](https://api.jquery.com/descendant-selector/) | Matches `input` that are descendants of a `fieldset` that is a descendant of a `form` |
| `input[value='Hot Fuzz']` | [Attribute equals selector](https://api.jquery.com/attribute-equals-selector/) | Matches `input` that have the specified attribute `value` with a value exactly equal to `'Hot Fuzz'` |

jQuery also offers **extension selectors**.  These are selectors that are not part of the CSS specification.  Examples:

```javascript
// first-child: finds the first span in each matched div to underline
$( "div span:first-child" ).css( "text-decoration", "underline" )

// has(): adds the class "test" to all divs that have a paragraph inside of them
$( "div:has(p)" ).addClass( "test" );

// header: selects all elements that are headers, like h1, h2, h3 and so on
$( ":header" ).css({ background: "#ccc", color: "blue" });

// button: equivalent to $( "button, input[type='button']" ) e.g. all button elements and elements of type button
$( ":button" ).addClass( "marked" );
```

## jQuery Conventions

**Prepend a dollar sign** to the name of variables that are results of selections made with jQuery.  This is used a reminder of what the variable is storing:

```javascript
let $allElements = $('*');
```

**Use a local jQuery copy as a fallback** if a CDN load fails:

```html
<!--CDN version-->
<script src="//code.jquery.com/jquery-1.11.3.min.js"></script>

<!--if window.jQuery is not defined, CDN load has failed
    and we inject code that will load a local hosted copy that-->
<script>window.jQuery || document.write('<script src="js/jquery-1.11.3.min.js"><\/script>');</script>
```

**Place scripts just before the closing body tag.**  This obviates the need for `$(document).ready()`, because at that point, all the other elements are already in the DOM.

```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8" />
    <title>Foo Bar</title>
    <link rel="stylesheet" href="../css/main.css"/>
    <style>/* STYLES GO HERE */</style>
  </head>
    <body>
      <p id="main-content">CONTENT GOES HERE</p>
      <script src="../js/jquery-1.11.3.min.js"></script>
      <script>
         $('p#main-content').html("JavaScript code goes here!");
      </script>
  </body>
</html>
```

Summary: `<link>`s and `<style>` goes in `<head>`, `<script>` at end of `<body>`.

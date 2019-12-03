# Document-Object Model (DOM)

## Four Nodes Types

- Document node: the entire page; synonymous with the `document` object
- Element node: tags that give the page structure
- Attribute node: tied to opening tags; they are _not_ children of the tag but rather part of it
- Text node: the text within an element; cannot have children

## Why Doesn't The HTML Source Change?

Scripts access and update the in-browser-memory DOM tree, not the source HTML file.  Changes made to the DOM are reflected in the browser, not in the "view-source" HTML.

## DOM Queries & Traversal

Returns an individual element node:

getElementById
querySelector

Returns a NodeList (multiple elements):

getElementsByClassName
getElementsByTagName
querySelectorAll

DOM traversal:

parentNode
previousSibling
nextSibling
firstChild
lastChild

Element node properties:

innerHTML
textContent
innerText

Text node properties:

nodeValue

### Whitespace Nodes

Chrome, Firefox, Safari, and Opera create text nodes from HTML whitespace (spaces and newlines/carriage returns).

## Example Query Selectors

// Each li element that has an id attribute
querySelectorAll('li[id]')

## Events

You browser register events, and JavaScript can respond to these events.

Some terminology: when an event has occured, it is often described as being **fired**.  Events **trigger** an action or script.

Three steps to handle an event:

- Select the element node(s) you want the script to respond to\*
- Indicate which event on the selected node(s) should trigger a response
- Define the response (a callable)

<sup>\*The UI events that relate to the browser window work with the `window` object rather than an element node.</sup>

Three ways to bind an event to an element:

1. _Suboptimal_: HTML event handler, i.e. `<a href="_blank" onclick="functionName()">`
	- Better practice is to _separate the JS from the HTML_
2. _Suboptimal_: Traditional DOM event handlers, i.e. `element.onevent = functionName`
	- You can only attach a single function to any event
	- Function typically uses `this`, which most browsers know refers to the element on which the event happened
3. _Preferred_: DOM level 2 event listeners, i.e. `element.addEventListener('onclick', functionName, false)`
	- Allows one event to trigger multiple functions.

Example: traditional DOM event handler:

```javascript
function checkUserName() {
	var message = document.getElementById('feedback');
	if (this.value.length) < 5 {
		message.textContent = 'Username must be 5 characters or longer';
	} else {
		message.textContent = '';
	}
}

var username = document.getElementById('username');
username.onblur = checkUsername;
```

> **What is `this`?**  The `this` keyword refers to the owner of a function.  In this example, `this` refers to the element that the event is on.

Level 2 event listener handlers:

```javascript
// [checkUserName defined same as above]

var username = document.getElementById('username');
username.addEventListener('blur', checkUsername, false);
```

Signature for `.addEventListener()`:

TODO

You must pass a callable to `.addEventListener()`.  One trick for using arguments is to embed an anonymous function:

```javascript
username.addEventListener('blur', function() {
	checkUsername(5);
}, false);
```

### The `event` Object

The `event` object is implicitly passed to any function that is the event handler or listener.

```javascript
// 'e' is the event object
// Compared to checkUserName(), this can check the length of any
// text input
function checkLength(e, minLength) {
	var el, msg;

	// el is the target of the event, i.e. what element the event
	// occurred upon
	el = e.target;
	msg = el.nextSibling;
	if (el.value.length < minLength) {
		msg.innerHTML = 'Username must be' + minLength + 'characters or more';
	} else {
		msg.innerHTML = '';
	}
}

var username = document.getElementById('username');
username.addEventListener('blur', function (e) {
	checkLength(e, 5);
}, false);
```

Two examples:

```javascript
var msg = `\
<div class="header"><a id="close" href="#">close X</a></div>
'<div>
<h2>System Maintenance</h2>'
<p>
Our servers are being updated between 3 and 4 a.m.
'During this time, there may be minor disruptions to service.
</p>
</div>'```

var elNote = document.createElement('div');       // Create a new element
elNote.setAttribute('id', 'note');                // Add an id of note
elNote.innerHTML = msg;                           // Add the message
document.body.appendChild(elNote);                // Add it to the page

function dismissNote() {                          // Declare function
  document.body.removeChild(elNote);              // Remove the note
}

var elClose = document.getElementById('close');   // Get the close button
elClose.addEventListener('click', dismissNote, false);// Click close-clear note
```

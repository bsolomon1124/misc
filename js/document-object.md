- The page in the current web browser window is modeled using a `document` object.
- All major browsers support and implement the document object in the same way.
- The `.title` property corresponds to the `<title>` head tag.
- The browser represents each window or tab using a `window` object.
- The `.location` property of the window tells you the URL of its page.

A browser creates a _model_ of a document's HTML, with the **document object** at the top of the hierarchy.  Each descendant is also called a node.
When you use JavaScript in the browser, there is a part of the browser called an interpreter (scripting engine)
JavaScript is an interpreted programming language
Some users browse with JavaScript turned off, so you need to make sure the page still works for them

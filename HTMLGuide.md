# Contents

# Resources & references
- w3schools.com: [HTML5 tutorial](https://www.w3schools.com/html/default.asp)
- The [HTML document tree](http://web.simmons.edu/~grabiner/comm244/weekfour/document-tree.html)
- [6 Best HTML & CSS Books](https://tutorials.hostucan.com/6-best-html-css-books)
- [What's an HTTP request?](http://rve.org.uk/dumprequest)

# Overview

# The HTML document tree
Each HTML document can actually be referred to as a document tree. We describe the elements in the tree like we would describe a family tree.

Use the sample HTML document below for these examples. The `<head>` section of the document is omitted for brevity.

```html
<body>

  <div id="content">
    <h1>Heading here</h1>
    <p>Lorem ipsum dolor sit amet.</p>
    <p>Lorem ipsum dolor <em>sit</em> amet.</p>
    <hr>
  </div>

  <div id="nav">
    <ul>
      <li>item 1</li>
      <li>item 2</li>
      <li>item 3</li>
    </ul>
  </div>

</body>
```

A diagram of the above HTML document tree would look like this:

![](http://web.simmons.edu/~grabiner/comm244/weekfour/tree.gif)

## Ancestor
An ancestor refers to any element that is connected but further up the document tree - no matter how many levels higher. In the diagram below, the `<body>` element is the ancestor of all other elements on the page.

![](http://css.maxdesign.com.au/selectutorial/images/tree_ancestor.gif)

## Descendant
A descendant refers to any element that is connected but lower down the document tree - no matter how many levels lower. In the diagram below, all elements that are connected below the `<div>` element are descendants of that `<div>`.

![](http://css.maxdesign.com.au/selectutorial/images/tree_descendant.gif)

## Parent & child
A parent is an element that is directly above and connected to an element in the document tree. In the diagram below, the `<div>` is a parent to the `<ul>`.

A child is an element that is directly below and connected to an element in the document tree. In the diagram above, the `<ul>` is a child to the `<div>`.

![](http://css.maxdesign.com.au/selectutorial/images/tree_parent.gif)

## Sibling
A sibling is an element that shares the same parent with another element. In the diagram below, the `<li>`'s are siblings as they all share the same parent - the `<ul>`.

![](http://css.maxdesign.com.au/selectutorial/images/tree_siblings.gif)

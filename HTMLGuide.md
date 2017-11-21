# Contents

# Resources & references
- w3schools.com: [HTML5 tutorial](https://www.w3schools.com/html/default.asp)
    - [Examples](https://www.w3schools.com/html/html_examples.asp)
    - [Tag reference](https://www.w3schools.com/tags/default.asp)
    - [Tryit Editor](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_default): interactive HTML rendering
- The [HTML document tree](http://web.simmons.edu/~grabiner/comm244/weekfour/document-tree.html)
- [6 Best HTML & CSS Books](https://tutorials.hostucan.com/6-best-html-css-books)
- [What's an HTTP request?](http://rve.org.uk/dumprequest)
- The Beautiful Soup [documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

# Overview
Hypertext Markup Language (HTML) is the standard markup language for creating web pages and web applications.

Filename extensions: `.html`; `.htm`.  (They are equivalent.)

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

# Tags & attributes

## Tags
HTML **tags** most commonly come in pairs like `<h1>` and `</h1>`, although some represent empty elements and so are unpaired, for example `<img>`. The first tag in such a pair is the _start tag_, and the second is the _end tag_ (they are also called _opening tags_ and _closing tags_).

```html
<tagname>content</tagname>
```

HTML tags are not case sensitive: `<P>` means the same as `<p>`.  Lowercase is generally preferred and more widely used.

### Paragraph versus break


## Attributes
Tags have optional **attributes**.  These indicate other information, such as identifiers for sections within the document or identifiers used to bind style information to the presentation of the document.
- Most of the attributes of an element are name-value pairs, separated by `=` and written within the start tag of an element after the element's name.
    - There are also some attributes that affect the element simply by their presence in the start tag of the element
- Single or double quotes are okay; leaving attribute values unquoted is considered unsafe.
- See also: the Wikipedia [page](https://en.wikipedia.org/wiki/HTML#Attributes) on HTML attributes.

HTML attributes are generally classed as required attributes, optional attributes, standard attributes, and event attributes.

Similar to tags, attributes are case-insensitive; but, prefer lowercase.


| Attribute | Description |
| --------- | ----------- |
| alt | Specifies an alternative text for an image, when the image cannot be displayed |
| disabled |  Specifies that an input element should be disabled |
| href |  Specifies the URL (web address) for a link |
| id | Specifies a unique id for an element |
| src | Specifies the URL (web address) for an image |
| style | Specifies an inline CSS style for an element |
| title | Specifies extra information about an element (displayed as a tool tip) |

## Elements
An **element** is a broader term that includes a pair of corresponding tags and "everything in between.""  (Attributes, other tags, and contents.)  The general structure of an element is therefore:

```html
<tag attribute1="value1" attribute2="value2">''content''</tag>
```

For example,

```html
<a href="https://www.wikipedia.org/">A link to Wikipedia.</a>
```

HTML elements with no content are called empty elements. Empty elements do not have an end tag, such as the `<br>` element (which indicates a line break).  Use of empty elements will lead to **broken HTML**, which may still render correctly but have difficulty being read by XML parsers.

## Doctype
The **document type declaration** (doctype) triggers standards mode rendering.  It must only appear once, at the top of the page (before any HTML tags).

```html
<!DOCTYPE html>
<!-- Defaults to HTML5 -->
```

# Comments

```html
<!-- This is a comment -->
<input type="text" /> <!-- Comments can be inline-->
```

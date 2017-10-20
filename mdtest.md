# Contents


# Resources & References
- Metis: [Markdown](https://github.com/thisismetis/dsp/blob/master/00a-markdown.md)
- Math Overflow: [Markdown help](https://mathoverflow.net/editing-help)
- GitHub Guides: [Mastering Markdown](https://guides.github.com/features/mastering-markdown/)
- MakeUsOf: [What Is Markdown? 4 Reasons Why You Should Learn It Now](http://www.makeuseof.com/tag/markdown-4-reasons-learn-now/)
- aaronsw: [Markdown](http://www.aaronsw.com/weblog/001189)
- Stack Overflow: [Markdown help](https://stackoverflow.com/editing-help)
- SourceForge: [Markdown Syntax Guide](https://sourceforge.net/p/forge/documentation/markdown_syntax/)
- Reddit: [Markdown Primer](https://www.reddit.com/r/reddit.com/comments/6ewgt/reddit_markdown_primer_or_how_do_you_do_all_that/)
- [Writing on GitHub](https://help.github.com/categories/writing-on-github/)
- [Markdown home page](https://daringfireball.net/projects/markdown/)
- John Gruber: [Dive Into Markdown](https://daringfireball.net/2004/03/dive_into_markdown)
- codebase: [Syntax highlighting in markdown](https://support.codebasehq.com/articles/tips-tricks/syntax-highlighting-in-markdown)
- [Markdown Cheat Sheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Here-Cheatsheet)

# Overview
From Wikipedia:

_Markdown is a lightweight markup language with plain text formatting syntax. It is designed so that it can be converted to HTML and many other formats using a tool by the same name. Markdown is often used to format readme files, for writing messages in online discussion forums, and to create rich text using a plain text editor. As the initial description of Markdown contained ambiguities and unanswered questions, many implementations and extensions of Markdown appeared over the years to answer these issues._

# Line breaks
End a line with two spaces to add a `<br/>` linebreak or add a literal newline.

## Option 1 (2 spaces)
How do I love thee?  
Let me count the ways.

## Option 2 (newline, no end spaces)
How do I love thee?

Let me count the ways.

## Using neither will not create any break:
How do I love thee?
Let me count the ways.

# Separation lines
You can use three or more of: hyphens, asterisks, or underscores.  Note that headers in markdown automatically have a thin separation line underneath.
---
Hyphens
***
Asterisks
___

Underscores

# Bare URLs
The Markdown parser now supports "naked" URLs: I often visit http://example.com.

Force URLs by enclosing them in angle brackets: Have you seen <http://example.com>?

# Bold & italic
*This text will be italic*.  
_This will also be italic_.

**This text will be bold**.  
__This will also be bold__.

_You **can** combine them_ _**like so**_.

# Simple lists
- Use a minus sign for a bullet
+ Or plus sign
* Or an asterisk
* Another "asterisk" bullet

Note that the above bullets are separated by spaces because each uses a different symbol in its code.
# Numbered lists
1. Numbered lists are easy
2. Markdown keeps track of the numbers for you
7. So this will be item 3.

# Blockquotes
> The syntax is based on the way email programs
> usually do quotations. You don't need to hard-wrap
> the paragraphs in your blockquotes, but it looks much nicer if you do.  Depends how lazy you feel.

# Images
Images are exactly like links, but they have an exclamation point in front of them:
![Valid XHTML](http://w3.org/Icons/valid-xhtml10).


# Inline HTML

```html
<dl>
  <dt>Definition list</dt>
  <dd>Is something people use sometimes.</dd>

  <dt>Markdown in HTML</dt>
  <dd>Does *not* work **very** well. Use HTML <em>tags</em>.</dd>
</dl>
```
Result:

<dl>
  <dt>Definition list</dt>
  <dd>Is something people use sometimes.</dd>

  <dt>Markdown in HTML</dt>
  <dd>Does *not* work **very** well. Use HTML <em>tags</em>.</dd>
</dl>

# Language-specific highlighting
Ruby:
```ruby
def index
  puts "hello world"
end
```

CSharp:
```csharp
private void index(){
  MessageBox.Show("hello world");
}
```

Python:
```python
print("hello world!")
print("hello moon")
```

without the highlighting:
```
print("hello world!")
print("hello moon")
```

# Links
There are three ways to write links. Each is easier to read than the last:

Here's an inline link to [Google](http://www.google.com/).

Here's a reference-style link to [Google][1].

Here's a very readable link to [Yahoo!][yahoo].

  [1]: http://www.google.com/
  [yahoo]: http://www.yahoo.com/

Note that the link references don't need to necessarily be at the bottom
of the document.


# Tables
First Header | Second Header
------------ | -------------
Content from cell 1 | Content from cell 2
Content in the first column | Content in the second column

# LaTex
Does LaTex work in .md?  We shall see...

The *Gamma function* satisfying $\Gamma(n) = (n-1)!\quad\forall
n\in\mathbb N$ is via through the Euler integral

$$
\Gamma(z) = \int_0^\infty t^{z-1}e^{-t}dt\,.
$$

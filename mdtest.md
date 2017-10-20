# Contents


# Resources & References
- The official Markdown syntax reference [page](https://daringfireball.net/projects/markdown/syntax) and the [Markdown home page](https://daringfireball.net/projects/markdown/)
- Metis: [Markdown](https://github.com/thisismetis/dsp/blob/master/00a-markdown.md)
- Math Overflow: [Markdown help](https://mathoverflow.net/editing-help)
- GitHub Guides: [Mastering Markdown](https://guides.github.com/features/mastering-markdown/)
- MakeUsOf: [What Is Markdown? 4 Reasons Why You Should Learn It Now](http://www.makeuseof.com/tag/markdown-4-reasons-learn-now/)
- aaronsw: [Markdown](http://www.aaronsw.com/weblog/001189)
- Stack Overflow: [Markdown help](https://stackoverflow.com/editing-help)
- SourceForge: [Markdown Syntax Guide](https://sourceforge.net/p/forge/documentation/markdown_syntax/)
- Reddit: [Markdown Primer](https://www.reddit.com/r/reddit.com/comments/6ewgt/reddit_markdown_primer_or_how_do_you_do_all_that/)
- [Writing on GitHub](https://help.github.com/categories/writing-on-github/)
- John Gruber: [Dive Into Markdown](https://daringfireball.net/2004/03/dive_into_markdown)
- codebase: [Syntax highlighting in markdown](https://support.codebasehq.com/articles/tips-tricks/syntax-highlighting-in-markdown)
- [Markdown Cheat Sheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Here-Cheatsheet)

# Overview
From Wikipedia:

_Markdown is a lightweight markup language with plain text formatting syntax. It is designed so that it can be converted to HTML and many other formats using a tool by the same name. Markdown is often used to format readme files, for writing messages in online discussion forums, and to create rich text using a plain text editor. As the initial description of Markdown contained ambiguities and unanswered questions, many implementations and extensions of Markdown appeared over the years to answer these issues._

**How to use** this document: it is easiest to display the [raw code](https://raw.githubusercontent.com/bsolomon1124/misc/master/mdtest.md) as a means to follow along with the formatted output.

# Headers

Preface with the '#' sign.

# Header 1
## Header 2
### Header 3
#### Header 4
##### Header 5
###### Header 6

You can also include HTML within headers to make them easier for referencing.  For instance,

## <a name="section-a"></a>1) Line Breaks 

could be referenced as 

[1)  Line Breaks](#section-a)

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
You can use three or more of: hyphens, asterisks, or underscores.  Note that headers in markdown automatically have a thin separation line underneath.  Note that this text itself needs a newline under it prior to the '---'.  I.e., make sure to have a blank line above hyphens unless you'd like it to indicate a header.

---
Hyphens
***
Asterisks
___
Underscores

# Bare URLs
The Markdown parser now supports "naked" URLs: I often visit http://example.com.  Any URL (like http://www.github.com/) will be automatically converted into a clickable link.

Force URLs by enclosing them in angle brackets: Have you seen <http://example.com>?

# Bold, italic, & strikethrough
*This text will be italic*.  
_This will also be italic_.

**This text will be bold**.  
__This will also be bold__.

_You **can** combine them_ _**like so**_.

Strikethrough uses two tildes. ~~Scratch this.~~

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

# Nested lists
To put other Markdown blocks in a list; just indent four spaces for each nesting level:

1. Lists in a list item:
    - Indented four spaces.
        * indented eight spaces.
    - Four spaces again.
2.  Multiple paragraphs in a list items:
    It's best to indent the paragraphs four spaces
    You can get away with three, but it can get
    confusing when you nest other things.
    Stick to four.
 
    We indented the first line an extra space to align
    it with these paragraphs. In real use, we might do
    that to the entire list so that all items line up.
 
    This paragraph is still part of the list item, but it looks messy to humans. So it's a good idea to wrap your nested paragraphs manually, as we did with the first two.
 
3. Blockquotes in a list item:
 
    > Skip a line and
    > indent the >'s four spaces.
 
4. Preformatted text in a list item:
 
        Skip a line and indent eight spaces.
        That's four spaces for the list
        and four to trigger the code block.

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

Note that [Markdown only supports a very strict subset of HTML]https://meta.stackexchange.com/questions/1777/what-html-tags-are-allowed-on-stack-exchange-sites).

To reboot your computer, press <kbd>ctrl</kbd>+<kbd>alt</kbd>+<kbd>del</kbd>.

Block-level HTML elements have a few restrictions:

1. They must be separated from surrounding text by blank lines.
2. The begin and end tags of the outermost block element must not be indented.
3. Markdown can't be used within HTML blocks.

<pre>
    You can <em>not</em> use Markdown in here.
</pre>

# Inline code
Blocks of code are either fenced by lines with three back-ticks, \`\`\`, or are indented with four spaces. Only fenced code blocks support syntax highlighting (see below).
```
def a(x):
    pass
```

    def b(x):
        pass

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

Colons can be used to align columns:
| Tables        | Are           | Cool  |
| ------------- |:-------------:| -----:|
| col 3 is      | right-aligned | $1600 |
| col 2 is      | centered      |   $12 |
| zebra stripes | are neat      |    $1 |


# LaTex
Markdown doesn't natively support LaTex: 

$$
\Gamma(z) = \int_0^\infty t^{z-1}e^{-t}dt\,.
$$

However, pandoc, a "universal document converter," [does](http://www.juanshishido.com/markdownlatex.html).

# Task lists

- [x] @mentions, #refs, [links](), **formatting**, and <del>tags</del> supported
- [x] list syntax required (any unordered or ordered list supported)
- [x] this is a complete item
- [ ] this is an incomplete item

# Stack overflow tags
See the many questions tagged [tag:elephants] to learn more.

# Vim Guide

## Resources & References

- [Vim home page](https://www.vim.org/)
- [Vim source code on GitHub](https://github.com/vim/vim)
- [A Good Vimrc](https://dougblack.io/words/a-good-vimrc.html)
- [Steve Oualline - The Vim Tutorial and Reference (~800 pgs)](http://www.oualline.com/vim-book.html)

## Starting Vim

```bash
$ vim [options] [file ..]
```

## Useful Command-Line Options

From the man page, in order of usefulness.  These should be all that you need:

       +[num]      For the first file the cursor will be positioned on line "num".
                   If "num" is missing, the cursor will be positioned on the last line.

       -o[N]       Open N windows stacked.  When N is omitted, open one window for each file.

       -O[N]       Open N windows side by side (columns).  When N is omitted, open one window for each file.
                   Example: `vim -O2`

       -p[N]       Open N tab pages.  When N is omitted, open one tab page for each file.

       -r          List swap files, with information about using them for recovery.

       -r {file}   Recovery  mode.   The  swap file is used to recover a crashed editing session.
                   The swap file is a file with the same filename as the text file with
                   ".swp" appended.  See ":help recovery".

       +/{pat}     For the first file the cursor will be positioned in the line with the first occurrence of {pat}.
                   See ":help search-pattern" for the available search patterns.

       --version   Print version information and exit.

## Modes

Vim is a model editor, behaving differently depending on which mode you are in.

- Normal (command) mode: bottom of screen displays file name or is blank.  You use ex-style commands (prefaced with colon `:`) from here.
- Insert mode.  Bottom of screen displays `--INSERT--`.
- Visual mode.  Bottom of screen displays `--VISUAL--`.

To enter insert mode, type `i`.  To exit, press <Esc>.

## Configuration

`~/.vimrc` is for your personal Vim initializations.

Example: https://github.com/bsolomon1124/config/blob/master/.vimrc

## Cursor (Direction) Keys

`k` is up, `h` is left, `l` si right, `j` is down:

      k
    h   l
      j

Mnemonic: `j` key looks like down arrow.

## Commands

The general syntax of commands is `[number]command[motion]`.

You can optionally precede all movement commands with a number.

Examples:

- `9dd` to delete 9 lines
- `5o` to insert 5 lines
- `5fx` to move up 5 occurrences of "x"
- `d3w` deletes 3 words
- `3a!` adds three exclamation points after the cursor

For commands like `yw` (yank/copy one word) and `c$` (delete from cursor to end of line), the first character is the command, and the second is the motion.

General commands:

Insertion, deletion, copying & pasting:

    i               enter insert mode.  will insert text *before* the character under cursor
    a               enter insert mode, but will insert text *after* character under cursor
    x               delete character under cursor

    O               insert line *above* the cursor, then enter insert mode
    o               insert line *below* the cursor, then enter insert mode

    d{motion}       delete.  doesn't enter insert mode after
    dd              delete current line
    dw              delete current word
    d$              delete from cursor til end of current line
    D               delete from cursor til end of current line

    c{motion}       change text.  like d{motion}, but puts you in insert mode after
    c$              delete from cursor to end of line
    cw              delete from cursor to end of word, then enter insert word

    p               put yanked text after the cursor (like paste)
    P               put yanked text before the cursor
    y               yank (like copy)
    yw              yank (copy) one word
    yy              yank lines

    r{x}            replace single character under the cursor with character {x}

Undoing and redoing:

    u               undo last edit
    U               undo whole line.  undoes all the changes made on the last line that was edited
    <Ctrl> + R      redo
    .               redo last change or delete command

Searching:

    /{phrase}       search forward for {phrase}.  to get rid of the highlights, use `:noh`
    ?{phrase}       search backwards for {phrase}

    n               get next search result
    N               get previous search result

*Note*: characters `.*[]ˆ%/\?~$` are metacharacters.  To find them literally, escape them with `\`.

Other:

    ZZ              write and exit.  note the Z's are capitalized

    z + <Enter>     make current line the top one on the screen
                    (sort of like "scroll past end")

    ~               change current character's case
    g~w             invert case of current word
    g~~             invert case of current line
    gUU             make current line uppercase
    guu             make current line lowercase

    >>              indents selected lines by one "shift width."
                    amount of whitespace is set with the `:set shiftwidth` option
    <<              de-dents selected lines by one "shift width."

    J               join next line with current one, separated by spaces
    {n}J            join n lines, separated by spaces
    {n}gJ           join n lines, with no separator

    v               visual mode (highlight text with cursor keys)

    <Ctrl> + G      show file status and your location in the file

## Motions

Movement motions (all of these can take optional numeric arguments!):

    w               start of next word (2w, 3w, 4w)
    e               end of current word (2e, 3e, 4e)
    b               start of previous word

    $               end of line.  2$: end of next line, etc
    0               start of line
    ^               first non-blank character of the line

    gg              go to top of file
    G               go to bottom of file

    <Ctrl> + U      scrolls up half a screen of text
    <Ctrl> + D      scrolls you down half a screen

    <Ctrl> + B      scroll window [count] pages Backwards (upwards) in the buffer
    <Ctrl> + F      scroll window [count] pages Forwards (downwards) in the buffer
                    see also `:set window`

    %               jump cursor to a matching enclosure: ), ], or }

    f{c}            move to the next occurrence of character c on current line.
                    for example, if you are at start of the line "Searching Along a Single Line,"
                    `fS` will move to the S in "Single"
                    this command is case sensitive

## Ex-Style Commands

Any command that begins with a colon `:` is considered an ex-style command.

All of these must be finished by pressing <Enter>.

    :q                  exit Vim
    :q!                 exit and discard changes without writing/saving
    :qa!                exit/discard *all* changes.  this is for multiple tabs/windows/buffers
    :w [filename]       write (save) file, stay in Vim
    :wq [filename]      write (save) file and exit

    :{number}           go to a line number (or, use `{number}G`)

    :set {option}[=val] set an option i.e. :set ic.  See "setting options" section

    :shell              takes you to the shell temporarily.  you can exit back to Vim with `exit` (from shell)
    :!{cmd}             execute the external shell command cmd.  example: :!ls

    :s/old/new          substitute first occurrence of `new` for `old` in current line
    :s/old/new/g        substitute all occurrences of `new` for `old` in current line
    :%s/old/new/g       substitute all occurrences of `new` for `old` in entire file
    :%s/old/new/gc      find every occurrence in the whole file, with a prompt whether to substitute or not

    :vim {file}          edit file
    :e {file}           edit file
    :r {file}           read file
    :!rm {file}         remove file

    :next               change files, allowing you to edit the next file
    :previous           like next, but move back
    :wnext              like :w plus :next, combined as one command

    :args               displays the list of the files currently being edited
    :sp [file]          split vertical.  by default, opens the same file in two windows
    :vs [file]          split horizontal
    :new                like split, but open up new file

    :syntax [on|off]    syntax highlighting

    :noh                clear current highlighting

    :digraphs           show currently defined digraphs.
                        digraphs are used to enter characters that normally cannot be entered by an ordinary keyboard.
                        these are mostly printable non-ASCII characters.
    :cd {direc}         change directory within Vim

### Setting Options

For help:

    :help set

Full list:

    :help option-summary
    :help Q_op

General/meta options:

    :set                    show all options that differ from their default value
    :set all                show all but terminal options
    :se[t] {option}?        show value of {option}
    :se[t] {option}         for "toggle" options, switch it on.  for anything else, shows the value
    :se[t] no{option}       for "toggle" options: reset/switch it off
    :se[t] {option}&        reset option to its default value
    :se[t] all&             set all options to their default value
    :se[t] {option}={val}   set string or number option to {value}

Specific options listed below.

Toggle options (optionally preface the "positive" form with `no` i.e. `ic` or `noic`):

    :set [no]ic             ignore case in global search patterns
                            full name: `:set [no]ignorecase`
    :set [no]number         print the line number in front of each line
    :set [no]paste          put Vim in Paste mode, allow pasting text.
                            This is useful if you want to cut or copy
                            some text from one window and paste it in Vim.

    :set [no]incsearch      incremental search.  search & highlight as characters are entered
    :set [no]hlsearch       turn highlighting on in search.  highlight matches

    :set [no]autoindent     take indent for new line from previous line

    :set [no]ruler          show line and column number of cursor position, separated by comma

    :set [no]antialias      Mac OS X: use smooth, antialiased fonts
    :set [no]endofline      write <EOL> for last line in file

    :set [no]wrap           long lines wrap and continue on the next line.  this wraps lines that
                            are longer than the screen width.  (not the `textwidth`, if you have
                            specified that.)
    :set [no]smartcase      no ignore case when a search pattern has uppercase

    :set [no]expandtab      use spaces when <Tab> is inserted
    :set [no]smartindent    smart autoindenting for C programs
    :set [no]smarttab       use 'shiftwidth' when inserting <Tab>
                            if on: tabs inserted at the beginning of a line are treated
                            like soft tabs of size 'shiftwidth'

    :set [no]termguicolors  use GUI colors for the terminal

Numeric options:

    :set shiftwidth         number of spaces to use for (auto)indent step.  defaults to 'tabstop'
    :set tabstop            number of spaces that a <Tab> in the file counts for.
                            this is for visual rendering only.
    :set sotftabstop        number of spaces that <Tab> uses while editing, for insert or backspace
    :set scroll             number of lines to scroll with <CTRL> + U and <CTRL> + D commands
    :set textwidth          maximum width of text. a longer line will be broken after white space to
                            get this width.  A 0 value disables this.
                            set to 0 when the 'paste' option is set and restored when 'paste' is reset
    :set linebreak          wrap long lines at a blank

    :set colorcolumn        column(s) to highlight.  set a line-length colored column marker
                            can set multiple, for example: `:set colorcolumn=72,80`

    :set cmdheight          number of lines to use for the command-line
    :set cmdwinheight       height of the command-line window

    :set wrapmargin         chars from the right where wrapping starts

    :set window             number of lines to scroll for CTRL-F and CTRL-B (TODO)

String options:

    :set syntax             syntax to be loaded for current buffer
                            to switch on: `:set syntax enable`
    :set background         "dark" or "light", used for highlight colors
    :set filetype           type of file, used for autocommands
                            use `:set filetype on` to enable file type detection
    :set fileformat         gives the <EOL> of the current buffer (i.e :set fileformat=unix
                            uses newline, not newline + carriage return.)
    :set helpheight         minimum height of a new help window (default 20)

    :set pythonthreedll     name of the Python 3 dynamic library
    :set pythonthreehome    name of the Python 3 home directory
    :set pyxversion         Python version used for pyx* commands

Summary of options related to shifting, indentation, tabs, & wrapping:

The term _columns_ is used to be agnostic to tabs versus spaces.  In other words, a tab may be 4 columns wide, the equivalent of 4 spaces.

    :set shiftwidth         number of spaces to use for (auto)indent cmds, >> and <<.  defaults to 'tabstop'
    :set tabstop            number of spaces that a <Tab> in the file counts for.
                            this is concerned with rendering only
    :set sotftabstop        number of columns that <Tab> uses while in Insert mode
    :set [no]expandtab      use spaces when <Tab> is inserted in Insert mode

    :set textwidth          maximum width of text. a longer line will be broken after white space to
                            get this width.  A 0 value disables this.
                            set to 0 when the 'paste' option is set and restored when 'paste' is reset

    :set [no]wrap           long lines wrap and continue on the next line.  this wraps lines that
                            are longer than the screen width.  (not the `textwidth`, if you have
                            specified that.)
    :set wrapmargin         chars from the right where wrapping starts


    :set [no]smartindent    smart autoindenting for C programs
    :set [no]smarttab       use 'shiftwidth' when inserting <Tab>
                            if on: tabs inserted at the beginning of a line are treated
                            like soft tabs of size 'shiftwidth'.  not really needed.

See also: https://tedlogan.com/techblog3.html

## Plugins/Extensions & Language-Specific Features

## Using a Package Manager (Vundle)

[Vundle](https://github.com/VundleVim/Vundle.vim) is a popular Vim package manager.

To [install](https://github.com/VundleVim/Vundle.vim#quick-start):

```bash
$ git clone https://github.com/VundleVim/Vundle.vim.git ~/.vim/bundle/Vundle.vim
```

Make sure that `~/.vimrc` has these bare minimums:

```
set nocompatible
filetype off

" set the runtime path to include Vundle and initialize
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()
" alternatively, pass a path where Vundle should install plugins
"call vundle#begin('~/some/path/here')

" let Vundle manage Vundle, required
Plugin 'VundleVim/Vundle.vim'

"
" Specify plugins here
"

" All of your Plugins must be added before the following line
call vundle#end()            " required
filetype plugin indent on    " required
```

Launch Vim and run `:PluginInstall`.

For some examples, see [here](https://github.com/VundleVim/Vundle.vim/wiki/Examples).

Brief help guide for Vundle:

    :PluginList             lists configured plugins
    :PluginInstall          installs plugins; append `!` to update or just :PluginUpdate
    :PluginSearch {foo}     searches for foo; append `!` to refresh local cache
    :PluginClean            confirms removal of unused plugins

    :h vundle               more help details

## Installing Packages with Vundle

To install a new plugin (such as [YouCompleteMe](https://github.com/Valloric/YouCompleteMe) for code completion:

1. Add it to `~/.vimrc`, i.e. `Bundle 'Valloric/YouCompleteMe'`
2. Launch Vim, then run `:PluginInstall`.

The package will be downloaded to `~/.vim/bundle/`.

### Vim + Python

To check that your Vim install supports Python, see `vim --version | grep "[+-]python"`.  If `python` or `python3` has a plus-symbol next to it, it is supported.

To see which specific version of Python Vim is using, enter `vim` and then, in Vim, use:

```vim
:python3 import sys; print(sys.version)
```

## Using Regex

    Example                 matches
    -------                 -------
    ab\{2,3}c               "abbc" or "abbbc"
    a\{5}                   "aaaaa"
    ab\{2,}c                "abbc", "abbbc", "abbbbc", etc.
    ab\{,3}c                "ac", "abc", "abbc" or "abbbc"
    a[bc]\{3}d              "abbbd", "abbcd", "acbcd", "acccd", etc.
    a\(bc\)\{1,2}d          "abcd" or "abcbcd"
    a[bc]\{-}[cd]           "abc" in "abcd"
    a[bc]*[cd]              "abcd" in "abcd"

## Miscellaneous

### Column Typing

Stack Overflow: [In Vim how do I effectively insert the same characters across multiple lines?](https://stackoverflow.com/a/9549765/7954504).

You have the following:

```
a = (1, 2, 3)
b = (4, 5, 6)
c = (7, 8, 9)
```

And want:

```
a = list((1, 2, 3))
b = list((4, 5, 6))
c = list((7, 8, 9))
```

How to:

1. Move cursor to the `a`
2. Enter visual block mode with `<Ctrl> + v`
3. Press `j` (down) three times
4. Press `I`
5. Type the text
6. Press `<Esc>`

### See Colors for `ctermbg` Argument

    :help ctermbg

### Delete All Text in Open File

    gg
    dG

### Searching Through Your Command History

Enter the first letters of your previous command and push the <Up> arrow.

Type `q:` in normal mode to open commands window.

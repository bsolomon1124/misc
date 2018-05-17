# Contents

- [Contents][0]
- [Resources & References][1]
- [Terminology][2]
- [Environment Variables][3]
- [The Home Directory][4]
- [Special Path Characters][5]
- [Running an Application][6]
- [Quoting][7]
    - [Single Quotes][8]
    - [Double Quotes][9]
    - [Examples][10]
- [Arrays][11]
    - [General Rules][12]
    - [Indexed Arrays][13]
    - [Associative Arrays][14]
    - [Examples][15]
- [Commands][16]
    - [`mkdir`][17]
    - [`cd`][18]
    - [`rmdir` & `rm`][19]
    - [`touch`][20]
    - [The Directory Stack: `dir`, `pushd` & `popd`][21]
    - [`cp`][22]
    - [`mv`][23]
    - [View (Page Through) a File (`less`, `more`)][24]
    - [`cat`][25]
    - [`grep`][26]
    - [Finding Things: `find` & `locate`][27]
        - [`locate`][28]
        - [`find`][29]
    - [`clear`][30]
- [Redirection][31]
- [Users & Superusers (`sudo`, `su`, `sudoers`)][32]
- [Chaining Commands][33]
- [Expansion][34]
    - [Command Substitution][35]
    - [Variable/Parameter Substitution][36]
    - [Brace Expansion][37]
    - [Filename/Pathname Expansion][38]
- [Shell Functions][39]
    - [Scope][40]
- [Operators][41]
    - [Operators for Lists of Commands][42]
- [Flow Control][43]
    - [Syntaxes][44]
    - [`for`][45]
    - [`if`][46]
    - [`case`][47]
- [Getting Help][48]
- [Keyboard Shortcuts][49]
- [Invoking a Script][50]
    - [Shebang Line][51]
    - [What File Extension Do I Use? (`.sh`, `.bash`)][52]
    - [The `exit` command][53]
- [Other Tricks][54]
    - [Show Hidden Files][55]
    - [Change Frequency with Which App Store Checks for Updates][56]
    - [Forcing Mac not to Sleep][57]
    - [Downloading Files][58]
    - [Zipping & Unzipping][59]
    - [Dragging Files to Terminal][60]
    - [Process Information][61]
    - [Making Your Own Shorthand: Aliases][62]
    - [Word Count][63]
    - [Shorten the Prompt][64]
    - [Execute in Background][65]

[0]: #contents
[1]: #resources--references
[2]: #terminology
[3]: #environment-variables
[4]: #the-home-directory
[5]: #special-path-characters
[6]: #running-an-application
[7]: #quoting
[8]: #single-quotes
[9]: #double-quotes
[10]: #examples
[11]: #arrays
[12]: #general-rules
[13]: #indexed-arrays
[14]: #associative-arrays
[15]: #examples
[16]: #commands
[17]: #mkdir
[18]: #cd
[19]: #rmdir--rm
[20]: #touch
[21]: #the-directory-stack-dir-pushd--popd
[22]: #cp
[23]: #mv
[24]: #view-page-through-a-file-less-more
[25]: #cat
[26]: #grep
[27]: #finding-things-find--locate
[28]: #locate
[29]: #find
[30]: #clear
[31]: #redirection
[32]: #users--superusers-sudo-su-sudoers
[33]: #chaining-commands
[34]: #expansion
[35]: #command-substitution
[36]: #variableparameter-substitution
[37]: #brace-expansion
[38]: #filenamepathname-expansion
[39]: #shell-functions
[40]: #scope
[41]: #operators
[42]: #operators-for-lists-of-commands
[43]: #flow-control
[44]: #syntaxes
[45]: #for
[46]: #if
[47]: #case
[48]: #getting-help
[49]: #keyboard-shortcuts
[50]: #invoking-a-script
[51]: #shebang-line
[52]: #what-file-extension-do-i-use-sh-bash
[53]: #the-exit-command
[54]: #other-tricks
[55]: #show-hidden-files
[56]: #change-frequency-with-which-app-store-checks-for-updates
[57]: #forcing-mac-not-to-sleep
[58]: #downloading-files
[59]: #zipping--unzipping
[60]: #dragging-files-to-terminal
[61]: #process-information
[62]: #making-your-own-shorthand-aliases
[63]: #word-count
[64]: #shorten-the-prompt
[65]: #execute-in-background

# Resources & References

- GNU: official [Bash Reference Manual](https://www.gnu.org/software/bash/manual/bashref.html)
- [Linux Bash Shell Cheat Sheet](https://learncodethehardway.org/unix/bash_cheat_sheet.pdf)
- Jim Hoskins: [Introduction to the Mac OS X Command Line](http://blog.teamtreehouse.com/introduction-to-the-mac-os-x-command-line) [Sep 2012]
- From _Learn Python the Hard Way_: [Command Line Crash Course](https://learnpythonthehardway.org/book/appendixa.html)
- techonthenet tutorials: [Unix](https://www.techonthenet.com/unix/index.php)
- [An A-Z Index of the Apple macOS command line (OS X)](https://ss64.com/osx/)
- Machtelt Garrels - [Bash Guide for Beginners](https://linux.die.net/Bash-Beginners-Guide/)
- Mendel Cooper - [Advanced Bash-Scripting Guide](http://tldp.org/LDP/abs/html/index.html)
- Mike G - [BASH Programming - Introduction HOW-TO](http://tldp.org/HOWTO/Bash-Prog-Intro-HOWTO.html)
- developer.apple.com - [Shell Scripting Primer](https://developer.apple.com/library/content/documentation/OpenSource/Conceptual/ShellScripting/BeforeYouBegin/BeforeYouBegin.html#//apple_ref/doc/uid/TP40004268-CH1-SW1)
- [Sample .bashrc and .bash_profile Files](http://tldp.org/LDP/abs/html/sample-bashrc.html)

# Terminology

- The **console** is the system as a whole. This is both the command line as well as the output from previous commands.
- A **shell** is a special **command-line tool (interface)** and _interpreter_ that is designed specifically to provide text-based **interactive control over other command-line tools.**  It uses alphanumeric characters typed on a keyboard to provide instructions and data to the operating system, interactively.  From the Bash docs:

> At its base, a shell is simply a macro processor that executes commands. The term macro processor means functionality where text and symbols are expanded to create larger expressions. ... A Unix shell is both a command interpreter and a programming language.

- You **run Terminal to get access to a shell prompt.**  The Terminal is an _emulator_ and a text input/output application (_Applications > Utilities > Terminal.app_) that lets you interact with a **command-line environment.**  You could also interact with an environment using a remote connection method such as **secure shell (SSH)**.  A terminal window provides access to the input and output of a **shell process.**
- The standard OS X shell is **Bash**.  Bash is a Unix shell and command language **interpreter** first released in 1989.  In addition to running in a text window, Bash can also read and execute commands from a file, called a script.
- You run **command-line tools** (or just _commands_; one example would be `cd`) that OS X provides by _typing the name of the tool_.
    - Most tools can also take a number of **flags** aka **switches**.  `-l` would be one such flag.  Flags **change behavior.**
    - Flags can be used together after one hyphen.  For example, `-l` and `-a` are both flags to `ls`.  You can use `ls -la` to (1) display detailed info for each entry and (2) list all directory contents, including hidden files/folders.
    - Separately, some tools take **arguments**.  For example, in `ls /Users/brad/temp`, the second chunk is an argument.
- The shell (no matter the command, really) also has a notion of a **current working directory**. When you specify a filename or path that does not start with a slash, that path is assumed to be relative to this directory.  Otherwise, it is an absolute path.
    - Given a current directory `pwd` --> `/Users/brad`:
    - `bin/` is a relative path that becomes `/Users/brad/bin/`
    - `/etc/shells` is an absolute path
- The **prompt** is the beginning of the command line. It usually provides some contextual information like who you are, where you are and other useful info. It typically ends in a "$".

```bash
 ~$ locate Terminal.app | grep "Terminal.app$"
/Applications/Utilities/Terminal.app
```

# Environment Variables

**Environment variables** are variables inherited by all programs executed in the shell’s context. The shell itself uses environment variables to store information such as the name of the current user, the name of the host computer, and the paths to any executable programs.

`export` is used to create and view environment variables.  Use `export -p` or just `env`/`printenv` to view a list of all names exported in the current shell:

One important environment variable is `PATH`.  Command line tools are located in specific directories, and the shell searches `PATH` for them when you run a command.  `PATH` contains a **colon-delimited list of paths** to search-- `/usr/bin:/bin:/usr/sbin:/sbin`, for example.

```bash
# added by Anaconda3 5.0.0 installer
export PATH="/Applications/anaconda3/bin:$PATH"
```

For more on `sbin`/`bin` and the like, see:

- [How to understand the Ubuntu file system layout?](https://askubuntu.com/questions/138547/how-to-understand-the-ubuntu-file-system-layout)
- [Filesystem Hierarchy Standard](https://en.wikipedia.org/wiki/Filesystem_Hierarchy_Standard)

# The Home Directory

Your home directory (aliases `$HOME` or `~`) might not be the same as your _root_ directory.  To see your home directory, use

```bash
~ $ cd ~  # or cd $HOME
~ $ pwd
/Users/brad
```

In the example above, `brad` is actually 2 levels below the _top-level_ (root) of your hard drive.  Use `cd /` to move to root:

```bash
~ $ cd /  # or cd ../..
/ $ pwd
/

 ~$ tree -F -L 1 /
/
├── Applications/
├── Library/
├── Network/
├── System/
├── Users/
├── Volumes/
├── app/
├── bin/
├── cores/
├── data/
├── dev/
├── etc -> private/etc/
├── home/
├── installer.failurerequests
├── keybase/
├── net/
├── private/
├── sbin/
├── tmp -> private/tmp/
├── usr/
└── var -> private/var/
```

In Python, `os` doesn't accept (expand) the tilde character.  Expand it with `os.path.expanduser`:

> On Unix, an initial ~ is replaced by the environment variable `HOME` if it is set; otherwise the current user's home directory is looked up in the password directory through the built-in module `pwd`.

I.e.:

```python
>>> import os
>>> home = os.path.expanduser('~')
>>> print(home)
/Users/brad
```

# Special Path Characters

In addition to `~`, the shell supports a number of directory names that have a special meaning:

| Path string | Description |
| ----------- | ----------- |
| `.` | points to the current working directory | For example, if you type `./mytool` and press return, you are running the `mytool` command in the current directory.
| `..` | points to the parent directory (up 1 level) | The path `../Test` is a file or directory (named "Test") that is a **sibling of** the current directory. |
| `~` | At the beginning of a path, the tilde character represents the home directory of the current user. | `$HOME` is the same thing (usually); technically, it is an environment variable that can be manipulated. |

A few examples:

```bash
/ $ cd ~
~ $ pwd
/Users/brad
~ $ cd ~/Downloads
Downloads $ pwd
/Users/brad/Downloads
Downloads $ cd ../..
Users $ pwd
/Users
```

# Running an Application

There are two ways to run an application (.app) from the command line.  (Example: current directory is `/Applications`.)
1. Use `open`: `$ open BitTorrent.app`
2. Specify the pathname of the executable file inside the package.  This may be confusing because of the hidden nature of the directory: in the GUI, you simply see `<application>.app`.  But underneath, there is a path to an executable file:

```bash
$ ls BitTorrent.app/Contents
Frameworks  Info.plist  Library     MacOS       PkgInfo     Resources   _CodeSignature
$ BitTorrent.app/Contents/MacOS/BitTorrent
```

# Quoting

Double quotes dereference variables, while single quotes go literal.

## Single Quotes

- Enclosing characters in single quotes (‘'’) preserves the literal value of each character within the quotes.
- A single quote may not occur between single quotes, even when preceded by a backslash.

## Double Quotes

- Enclosing characters in double quotes (‘"’) preserves the literal value of all characters within the quotes, **with the exception of** ‘$’, ‘\`’, ‘\’, and, when history expansion is enabled, ‘!’
- Shell expansions with `$` and backticks are enabled within double quotes.
- The backslash retains its special meaning only when followed by one of the following characters: ‘$’, ‘\`’, ‘"’, ‘\’, or newline

## Examples

```bash
 ~$ a='first' b="second"
 ~$ echo $a
first
 ~$ echo "$a"
first
 ~$ echo '$b'
$b
```

# Arrays

Docs: [Arrays](https://www.gnu.org/software/bash/manual/bashref.html#Arrays)

## General Rules

- There is no maximum limit on the size of an array, nor any requirement that members be indexed or assigned contiguously.
- Any element of an array may be referenced using `${name[subscript]}`
- Expand to all members: `${name[@]}` or `${name[*]}`.  When there are no array members, `${name[@]}` expands to nothing.
- See the keys: `${!name[@]}` or `${!name[*]}`
- Referencing an array variable without a subscript is equivalent to referencing with a subscript of 0.
- To destroy, use `unset`:
    - `unset name[subscript]` destroys the array element at index `subscript`.
    - `unset name` destroys the array

## Indexed Arrays

- Indexed arrays are referenced using integers and are zero-based.
- An indexed array is created automatically if any variable is assigned to using the syntax `name[subscript]=value`.
- To create: `declare -a name`
- To assign: `name=( [sub1]=string1 [sub2]=string2 ... )`, or just `name=( val1 val2 val3 ... )`

## Associative Arrays

- Available in Bash 4+.  Check `echo $BASH_VERSION` and [upgrade to Bash 4](http://clubmate.fi/upgrade-to-bash-4-in-mac-os-x/) if needed.
- Associative arrays use arbitrary strings as indexes.
- To create: `declare -A name`
- To assign: `name=( [sub1]=string1 [sub2]=string2 ... )`

## Examples

```bash
 ~$ echo $BASH_VERSION
4.4.19(1)-release

 ~$ declare -A modes
 ~$ modes=( ["---"]=0 ["--x"]=1 ["-w-"]=2 ["-wx"]=3 ["r--"]=4 ["r-x"]=5 ["rw-"]=6 ["rwx"]=7 )
 ~$ echo ${modes["r--"]}
4
 ~$ echo ${modes[@]}
3 0 5 6 2 7 4 1

 ~$ declare -a iarr
 ~$ iarr=( 1 9 0 8 )
 ~$ echo ${iarr[@]}
1 9 0 8
 ~$ echo ${!iarr[@]}
0 1 2 3

# Referencing an array variable without a subscript is
# equivalent to referencing with a subscript of 0.
 ~$ echo $iarr
1
```

# Commands

## `mkdir`

Say you first make a single directory and then want to make a directory one level down without `cd`ing.  You'll need to specify the "full relative path".  If you want to make subdirectories multixple levels down, you'll need `-p` to create intermediate directories as required.

```bash
$ pwd
/Users/brad
$ mkdir temp
$ mkdir temp/stuff
$ mkdir temp/stuff/things/files  # this will fail: +1 levels down
$ mkdir -p temp/stuff/things/files  # need -p in this case
```

To make a directory with a space in its name, use quotes:

```bash
$ mkdir 'new folder1'
$ mkdir "new folder2"
```

Or, backslash escape the space literal:

```bash
$ mkdir new\ folder1
```

If you `mkdir` a directory that already exists, you'll get an error:

```bash
$ mkdir temp
$ mkdir temp
mkdir: temp: File exists
```

You can't specify _files_ this way.  Using `mkdir file.txt` creates a folder called "file.txt" rather than a text file.  For this you'll need the [`touch`](#touch) command.

## `cd`

```bash
$ mkdir -p dir1/dir2/dir3/dir4
$ pwd
/Users/brad
$ cd dir1/dir2/dir3
$ pwd
/Users/brad/dir1/dir2/dir3
$ cd ..
$ pwd
/Users/brad/dir1/dir2
$ cd ..; pwd  # one folder up
/Users/brad/dir1
$ cd ../..; pwd  # two folders up
/Users
```

You can put quotes around any file/folder in any command:

```bash
$cd "long folder name"
```

## `rmdir` & `rm`

If you try to do `rmdir` on Mac OSX and it refuses to remove the directory even though you are positive it's empty, then there is likely a hidden file contained there such as _.DS_Store_. In that case, type `rm -rf <dir>` instead (where `<dir>` is directory name).

| Syntax | Use |
| ------ | --- |
| `rm <fileName> ..` | delete file(s) |
| `rm -i <fileName> ..` | ask for confirmation for each file |
| `rm -f <fileName>` | force deletion of file |
| `rm -r <foldername>/` | delete folder |

## `touch`

Use touch to create blank files.  Make sure to specify the extension.

```bash
$ touch testfile.txt
```

Note that if the specified file already exists, the file itself will not be modified, but its last-modified-timestamp will be updated to "now."

## The Directory Stack: `dir`, `pushd` & `popd`

Docs: [Directory Stack Builtins](https://www.gnu.org/software/bash/manual/bashref.html#Directory-Stack-Builtins)

The directory stack is a list of recently-visited directories.

- The `dirs` builtin displays the contents of the directory stack.
    - The current directory is always the "top" of the directory stack.
    - To clear, use `dirs -c`
- `pushd` adds directories to the stack as it changes the current directory
- `popd` removes specified directories from the stack and changes the current directory to the directory removed
    - Read these as "push directory" and "pop directory."  These commands let you **temporarily go to a different directory and then come back, easily switching between the two.**

If we open up a new shell, our stack will just be our starting directory:

```bash
 ~$ dirs -p  # p: one entry per line
~
```

Now,

- The `pushd` command takes your current directory and "pushes" it into a list for later, then it changes to another directory. It's like saying, "Save where I am, then go here."
    - `pushd`, if you run it by itself with no arguments, will switch between your current directory and the last one you pushed. It's an easy way to switch between two directories.
- The `popd` command takes the last directory you pushed and "pops" it off, taking you back there.

It is easiest to see both in action:

```bash
# We add two directories to the stack
# each also cds to that directory
 ~$ pushd Scripts/python/
~/Scripts/python ~
 python$ pushd ~/Downloads/
~/Downloads ~/Scripts/python ~

 Downloads$ pwd
/Users/brad/Downloads

 Downloads$ dirs -p
~/Downloads
~/Scripts/python
~

# With no args, exchanges the top 2 directories
 Downloads$ pushd
~/Scripts/python ~/Downloads ~

 python$ pwd
/Users/brad/Scripts/python

# popd, no args:
# - removes top directory *and*
# - cd's to the new top directory
 python$ dirs -p
~/Scripts/python
~/Downloads
~
 python$ pwd
/Users/brad/Scripts/python
 python$ popd
~/Downloads ~
 Downloads$ pwd
/Users/brad/Downloads

 Downloads$ dirs -p
~/Downloads
~
```

## `cp`

The first argument is the file to copy.  The second is its destination, which may be **either a file (essentially copy + rename) or a directory**.

```bash
$ cp
usage: cp [-R [-H | -L | -P]] [-fi | -n] [-apvXc] source_file target_file
       cp [-R [-H | -L | -P]] [-fi | -n] [-apvXc] source_file ... target_directory
```

```bash
 shellscripts$ mkdir mult && cd mult
 mult$ touch file.txt
 mult$ cp file.txt file2.txt  # As new file
 mult$ mkdir sub/
 mult$ cp file.txt sub/file3.txt
 mult$ cp file.txt sub/
 mult$ tree
.
├── file.txt
├── file2.txt
└── sub
    ├── file.txt
    └── file3.txt  # To directory; retain name

# Move multiple.  file.txt will be overwritten
 mult$ cp *.txt sub/
overwrite sub/file.txt? (y/n [n]) y
 mult$ tree
.
├── file.txt
├── file2.txt
└── sub
    ├── file.txt
    ├── file2.txt
    └── file3.txt
```

Note that putting a `/` (slash) at the end of a directory checks that the file is really a directory, so if the directory doesn't exist, you'll get an error.

To copy directories rather than files, use the `-r` flag:

```bash
 mult$ cp -r sub/ sub2/
```

**`cp` will overwrite files that already exist**, so be careful copying files around.

To summarize:

| Syntax | Use |
| ------ | --- |
| `cp image.jpg newimage.jpg` | rename _image.jpg_ to _newimage.jpg_ |
| `cp image.jpg <folderName>/` | copy _image.jpg_ to _folderName/_ directory |
| `cp image.jpg folder/sameImageNewName.jpg`| copy _image.jpg_ to _folderName/_ directory and rename it |
| `cp -R stuff/ otherStuff/` | rename a directory |
| `cp -r stuff/ otherStuff/` | copy a directory |
| `cp *.txt stuff/` | copy all of the specified file type to folder |

## `mv`

The syntax to move is similar to that of copy:

```bash
$ mv
usage: mv [-f | -i | -n] [-v] source target
       mv [-f | -i | -n] [-v] source ... directory
```

```bash
$ pwd; ls
/Users/brad/temp
file2.txt
$ mkdir subtemp; mv file2.txt subtemp
$ ls
subtemp
$ ls subtemp
file2.txt
```

When you use two files, the operation becomes _renaming_:

```bash
$ touch temp/file1.txt
$ ls temp
file1.txt
$ cd temp
$ mv file1.txt file2.txt
$ ls
file2.txt
```

That is, `mv` with two file arguments is a means of "renaming by moving."

To summarize:

| Syntax | Use |
| ------ | --- |
| `mv file.txt Documents/` | move file to a folder |
| `mv <folderName> <folderName2>` | move folder to (within) other folder |
| `mv filename.txt filename2.txt` | rename file |
| `mv <fileName> stuff/newfileName` | move file to folder and give it a new name |
| `mv <folderName>/ ..` | move folder up in hierarchy |


## View (Page Through) a File (`less`, `more`)

`less` and `more` are similar commands, but do have [slight differences](https://unix.stackexchange.com/questions/81129/what-are-the-differences-between-most-more-and-less). `more` will display the file without hiding your command history; `less` will hide your command history until you press `q`.

- 'less' is a program similar to 'more', but which allows backward movement in the file as well as forward movement.
- less does not have to read the entire input file before starting, so with large input files it starts up faster than text editors like Vim.

```bash
$ less test.txt
```

To get out of `less` just type `q` (as in quit).

## `cat`

While `less` lets you page through a file, `cat` prints the entire file to STDOUT.

```bash
$ cat test.txt
This is the first line

And this is the third.
```

## `grep`

The `grep` utility searches any given input files, selecting lines that match one or more patterns.  grep is used for simple patterns and basic regular expressions.

The following pipes two commands together.  `cat` prints the file and `grep` finds all lines with occurences of `ax`.

```bash
$ cat braille.py | grep ax
fig, ax = plt.subplots()
ax.imshow(codes[5], cmap=cmap)
```

We can pipe any output to `grep`:

```bash
 mult$ history | grep " cp "
  287  cp funcs funcs2 &
  292  cp funcs funcs2 &; jobs
  293  cp funcs funcs2 &
  297  cp funcs funcs2 &
  523  cp file.txt file2.txt  # As new file
  524  cp file.txt NewFolder/file3.txt
  526  cp -R file.txt NewFolder/file3.txt
  527  cp -p file.txt NewFolder/file3.txt
  531  cp file.txt file2.txt  # As new file
  # ...
```

## Finding Things: `find` & `locate`

- `locate`: "find filenames quickly."  Searches a database for all pathnames which match the specified pattern.
- `find`: recursively walks a file hierarchy.

### `locate`

`locate` supports shell globbing and quoting, but not regex.  To enable regex, pipe with `grep`:

```bash
/usr/bin/bunzip2
/usr/bin/bzip2
/usr/bin/bzip2recover
/usr/bin/funzip
/usr/bin/gunzip
/usr/bin/gzip
/usr/bin/unzip
/usr/bin/unzipsfx
/usr/bin/zip
/usr/bin/zipcloak
/usr/bin/zipdetails
/usr/bin/zipdetails5.18
/usr/bin/zipgrep
/usr/bin/zipinfo
/usr/bin/zipnote
/usr/bin/zipsplit
```

You can see some statistics about the path database itself with:

```bash
 ~$ locate -S

Database: /var/db/locate.database
Compression: Front: 14.03%, Bigram: 59.84%, Total: 10.01%
Filenames: 1148539, Characters: 120204898, Database size: 12028142
Bigram characters: 4830994, Integers: 73081, 8-Bit characters: 164
```

To update the database, use `/usr/libexec/locate.updatedb`.  This is run regularly under the hood.

### `find`

`find` is for "finding files the hard way," recursively searching a directory based on a variety of attributes.

Syntax: you provide `find` one or more paths and an optional expression.

```bash
find [-H | -L | -P] [-EXdsx] [-f path] path ... [expression]
```

The simplest case of `find` is to pass `.` as the path, which recursively lists the subcontents with your current directory as root:

```bash
 shellscripts$ find .
.
./file2.txt
./file.txt
./helloworld
./temp
./template.sh
./messages
./hello_world
./msg
./imgs
./imgs/2009
./imgs/2009/q
# ...
```

A few useful flags:

- `-s`: Traverse the file hierarchies in lexicographical order, i.e., alphabetical order within each directory.
- `-E`: Interpret regular expressions followed by `-regex` and `-iregex` primaries as extended (modern) regular expressions rather than basic regular expressions (BRE's).

Separate from _flags_, the `expression` itself consists of "primaries and operands" that look similar to flags.  For example, `-type <t>` filters down on the file type.  (d=directory, f=regular file, and others.)

```bash
# Find only regular files, not directories, symlinks, etc
 shellscripts$ find . -type f
./file2.txt
./file.txt
./helloworld
./template.sh
./messages
./hello_world
./msg

# Find only 2-level nested .txt files
 shellscripts$ find . -type f -name "*.txt" -mindepth 2
./mult/file2.txt
./mult/file.txt
./mult/sub/file2.txt
./mult/sub/file.txt
./mult/sub/file3.txt
./mult/sub2/file2.txt
./mult/sub2/file.txt
./mult/sub2/file3.txt
```

_Operators_ tie together the primaries (tests) above by describing logical relationships between them.

- `-not expression`
- `expression -and expression`
- `expression -or expression`

More info on the man page.

Additional examples: `man find | grep examples -A 33`.

```bash
# Print out a list of all the files whose names do not end in .c.
find / \! -name "*.c" -print

# Print out a list of all the files owned by user ``wnj'' that are newer than the file ttt.
find / -newer ttt -user wnj -print

# Print out a list of all the files which are not both newer than ttt and owned by ``wnj''.
find / \! \( -newer ttt -user wnj \) -print
```

## `clear`

In Sublime Text, there is a feature "Scroll Past End" that allows you to scroll the area of code you’re editing to the center of the window, even if it’s at the end of the file.

There is no direct equivalent functionality in terminal, but we can use `clear`, which clears the terminal screen and gets us a "blank page."

# Redirection

Before a command is executed, its input and output may be redirected using a special notation interpreted by the shell.

Redirections are processed in the order they appear, from left to right.

Keeping with the Unix theme of "everything is a file," programs such as `ls` actually send their results to a special file called standard output (often expressed as stdout) and their status messages to another file called standard error (stderr).  (These are at `/dev/stdout` ...)

```bash
 ~$ ls /dev | grep "std.*"
stderr
stdin
stdout
```

I/O redirection allows us to change where output goes and where input comes from.

- Redirect output: `[n]>[|]word`
    -  If the file does not exist it is created; if it does exist it is truncated to zero size.
    - With just `>`: the redirection will fail if the file whose name results from the expansion of `word` exists and is a regular file.
    - With `>|`: the redirection is attempted even if the file named by word exists.
    - Using just `> word` truncates the file `word`.
- Appending redirected output: `[n]>>word`
    - Causes the file whose name results from the expansion of `word` to be opened for appending on file descriptor `n`, or the standard output (file descriptor 1) if `n` is not specified.
    - If the file does not already exist, it is created just as though the `>` operator had been used.
- Redirect input: `[n]<word`

```bash
# We need `echo`, otherwise there's no output.
 shellscripts$ echo "some text here" > redirected.txt
 shellscripts$ cat redirected.txt
some text here

# Example 2
 shellscripts$ ls -l /usr/bin > ls-output.txt
 shellscripts$ head -n 5 ls-output.txt
total 139056
-rwxr-xr-x   4 root   wheel       925 Jul 15  2017 2to3-
lrwxr-xr-x   1 root   wheel        74 Nov 18 14:05 2to3-2.7 -> ../../System/Library/Frameworks/Python.framework/Versions/2.7/bin/2to3-2.7
-rwxr-xr-x   1 root   wheel     55072 Mar 28 00:02 AssetCacheLocatorUtil
-rwxr-xr-x   1 root   wheel     53472 Mar 28 00:02 AssetCacheManagerUtil

# `msg` is just a file.
 shellscripts$ echo "something" > msg
 shellscripts$ cat msg
something
```

Here's an example of redirecting stdin: `cat` with no arguments reads from stdin.  Using the `<` redirection operator, we change the source of standard input from the keyboard to a file. We see that the result is the same as passing a single filename argument.

```bash
 shellscripts$ cat < redirected.txt
some text here
```

To redirect standard error we must refer to its **file descriptor**:

- stdin --> 0
- stout --> 1
- stderr --> 2

Example: if `ls` encounters an error, it by default sends this to stderr.  We can redirect that error to `ls-error.txt`

```bash
 shellscripts$ ls -l /path/does/not/exist/ 2> ls-error.txt
 shellscripts$ cat ls-error.txt
ls: /path/does/not/exist/: No such file or directory
```

The preferred (newer) way to redirect both stdout and stderr to the same place is `&>`:

```bash
 shellscripts$ ls -l /bin/usr &> ls-output.txt
```

Note that this is semantically equivalent to `>word 2>&1`, which is an older syntax.

Disposing of "unwanted" output by redirecting to `/dev/null`, which is a _bit bucket_ that accepts input and does nothing with it.

```bash
# Suppress error msgs
 shellscripts$ ls /path/dne/ 2> /dev/null
```

Examples: [All about redirection](http://tldp.org/HOWTO/Bash-Prog-Intro-HOWTO-3.html)

# Users & Superusers (`sudo`, `su`, `sudoers`)

`sudo` stands for "superuser do."

If you have a lot of root-type work to do in a session, type `sudo -s` to create a new superuser shell, and work from there.

The default security policy is `sudoers`, which is configured via the file `/private/etc/sudoers`.  This defines specific commands that particular users are permitted to execute under an assumed identity.

The security policy determines what privileges, if any, a user has to run `sudo`.  The policy may require that users authenticate themselves with a password or another authentication mechanism.

TODO: more here (nobody, root, daemon users?)

Let's say you try to get a glimpse of the file `/private/etc/sudoers`:

```bash
 ~$ head /private/etc/sudoers
head: /private/etc/sudoers: Permission denied
```

Why is permission denied?

```bash
 ~$ ls -l /private/etc/sudoers
-r--r-----  1 root  wheel  1563 Dec 10  2016 /private/etc/sudoers
```

The file is owned by `root`, (and you are not `root`), while "world"/global permission are "---".

In this case, you will need `sudo` (where `!!` is the last command run, `head /private/etc/sudoers`):

```bash
 ~$ head /private/etc/sudoers
head: /private/etc/sudoers: Permission denied
 ~$ sudo !!
sudo head /private/etc/sudoers
#
# Sample /etc/sudoers file.
#
# This file MUST be edited with the 'visudo' command as root.
#
# See the sudoers man page for the details on how to write a sudoers file.

##
# Override built-in defaults
##
```

While `sudo` allows for single execution of a command as another user (default superuser), `su` allows you to assume the identity of another user and either _start a new shell session with that user’s ID_ or issue a single command as that user.  The default user for `su` is also the superuser.

```bash
su [-] [-flm] [login [args]]
```

`-l` simulates a _full login shell_.  This means that the user’s environment is loaded and the working directory is changed to the user’s home directory.

If you get `su: Sorry` when trying to use `su`, this is probably because your user is not a member of group `wheel`.

One workaround is `sudo -i`, which mimics `sudo su`.  (`sudo` asks for your own password; `su` asks for a root password.)

```bash
 ~$ sudo -i
Password:
Bradleys-MacBook-Pro:~ root# whoami
root
Bradleys-MacBook-Pro:~ root# pwd
/var/root
```

The trailing `#` indicates the current user has superuser privleges.  When finished, use `exit` to return to the regular shell.

TODO: more

# Chaining Commands

Use the pipe operator ("|") at the end of a command to redirect its _output_ to the next command.  Note that this is different than a semicolon which is simply the equivalent of using the commands _separately_ on two different lines.

# Expansion

Manual: [shell expansions](https://www.gnu.org/software/bash/manual/bashref.html#Shell-Expansions)

Expansion is performed on the command line after it has been split into tokens. There are seven kinds of expansion performed:

- brace expansion
- tilde expansion (`echo ~`)
- parameter and variable expansion
- command substitution
- arithmetic expansion
- word splitting
- filename expansion

## Command Substitution

Command substitution **allows the output of a command to replace the command itself.**

Use either

    $(command)  # newer

or

    `command`  # old

```bash
 shellscripts$ my_wd=`pwd`
 shellscripts$ echo $my_wd
/Users/brad/Scripts/playground/shellscripts

 ~$ ls -l $(which cp)
-rwxr-xr-x  1 root  wheel  29008 Oct 25  2017 /bin/cp

 ~$ file $(ls /usr/bin/* | grep zip)
/usr/bin/bunzip2:        Mach-O 64-bit executable x86_64
/usr/bin/bzip2:          Mach-O 64-bit executable x86_64
/usr/bin/bzip2recover:   Mach-O 64-bit executable x86_64
/usr/bin/funzip:         Mach-O 64-bit executable x86_64
/usr/bin/zipdetails:     Perl script text executable
/usr/bin/zipdetails5.18: Perl script text executable
/usr/bin/zipgrep:        POSIX shell script text executable, ASCII text
/usr/bin/zipinfo:        Mach-O 64-bit executable x86_64
# ...
```

Bash performs the expansion by executing `command` in a subshell environment and replacing the command substitution with the standard output of the command, with any trailing newlines deleted.

Command substitutions may be nested. To nest when using the backquoted form, escape the inner backquotes with backslashes.

## Variable/Parameter Substitution

The basic form of parameter & variable expansion is `${parameter}` or just `$parameter`.  Use the former if you need to protect the variable to be expanded from characters immediately following it which could be interpreted as part of the name.

```bash
 ~$ foo=bar
 ~$ qux=7
 ~$ echo $foo
bar
 ~$ echo $qux
7
 ~$ echo ${qux}{foo}
7{foo}
 ~$ echo ${qux}${foo}
7bar
 ~$ echo 1${qux}10
1710
```

There is a whole host of special syntax that can be used within the braces.  For example, `${parameter:-word}` says, "If `parameter` is unset or null, the expansion of `word` is substituted. Otherwise, the value of `parameter` is substituted."

```bash
 ~$ def=10  # is defined
 ~$ echo ${def:-default}
10
 ~$ echo ${undef:-default}
default
```

For the full list, see [Shell Parameter Expansion](https://www.gnu.org/software/bash/manual/bashref.html#Shell-Parameter-Expansion).

With parameter expansion, if you misspell the name of a variable, the expansion will still take place but will result in an empty string:

```bash
 shellscripts$ echo $SUER

```

## Brace Expansion

- syntax: `preamble{pattern}postscript`
- Supports nesting
- Sequence expression: `{x..y[..incr]}` i.e. `{1..10..2}`. This is inclusive at both endpoints.

Examples:

```bash
 imgs$ echo Front-{A,B,C}-Back
Front-A-Back Front-B-Back Front-C-Back
 imgs$ echo {1..10}  # {start..stop}
1 2 3 4 5 6 7 8 9 10
 imgs$ echo {1..10..2}  # {start..stop..step}
1 3 5 7 9
 imgs$ echo {a..f}
a b c d e f
 imgs$ echo {R..f}  # lexicographically sorted
R S T U V W X Y Z [  ] ^ _ ` a b c d e f
 imgs$ echo {10..1}
10 9 8 7 6 5 4 3 2 1
 imgs$ echo a{A{1,2},B{3,4}}b  # nesting
aA1b aA2b aB3b aB4b

mkdir -p pckg/{dist,src,lib,old}
 shellscripts$ ls pckg
dist    lib old src

 imgs$ mkdir -p 20{09..11}/q{1..4}
 imgs$ tree
.
├── 2009
│   ├── q1
│   ├── q2
│   ├── q3
│   └── q4
├── 2010
│   ├── q1
│   ├── q2
│   ├── q3
│   └── q4
└── 2011
    ├── q1
    ├── q2
    ├── q3
    └── q4

 imgs$ echo {2009..2011}-0{1..9} {2009..2011}-{10..12}  # alternate - flat
2009-01 2009-02 2009-03 2009-04 2009-05 2009-06 2009-07 2009-08 2009-09 2010-01 2010-02 2010-03 2010-04 2010-05 2010-06 2010-07 2010-08 2010-09 2011-01 2011-02 2011-03 2011-04 2011-05 2011-06 2011-07 2011-08 2011-09 2009-10 2009-11 2009-12 2010-10 2010-11 2010-12 2011-10 2011-11 2011-12
```

## Filename/Pathname Expansion

TODO

# Shell Functions

When using the braces, the list inside brackets must be terminated by a semicolon, a "&", or a newline:

 ~$ func () { echo "defined"; }  # semicolon required

To delete a function: `unset -f name`

```
 ~$ func () { echo "defined"; }
 ~$ func
defined
 ~$ unset -f func
 ~$ func
-bash: func: command not found
```

When a function is executed, the arguments to the function become the positional parameters during its execution

`$*` expands to the positional parameters, starting from one.

```bash
 ~$ function params { echo $*; }
 ~$ params 1 2 3 4 5
1 2 3 4 5
```

To list functions: `declare -f`.

## Scope

Variables local to the function may be declared with the `local` builtin. These variables are visible only to the function and the commands it invokes.

```bash
 ~$ HELLO=Hello
 ~$ function hello {
>         local HELLO=World
>         echo $HELLO
> }
 ~$ echo $HELLO
Hello
 ~$
 ~$ hello
World
 ~$ echo $HELLO
Hello
```

TODO: elaborate

# Operators

## Operators for Lists of Commands

- A list is a sequence of one or more pipelines separated by one of the operators `;`. `&`, `&&`, `||`, and optionally terminated by one of `:`, `&`, or a newline.
- Of these list operators, `&&` and `||` have equal precedence, followed by `;` and `&`, which have equal precedence.

AND and OR lists are sequences of one or more pipelines separated by the control operators `&&` and `||`, respectively. AND and OR lists are executed with left associativity.

An AND list has the form:

| Type of List | Syntax | Note |
| ------------ | ------ | ---- |
| AND list | `command1 && command2` | `command2` is executed if, and only if, `command1` returns an exit status of zero. |
| OR list | `command1 || command2` | `command2` is executed if, and only if, `command1` returns a non-zero exit status. |

The return status of AND and OR lists is the exit status of the last command executed in the list.

```bash
 Downloads$ cd ~/Downloads && ls | grep \.gz
abs-guide.html.tar.gz
mcalc-1.6.tar.gz

# Test for the existence of the directory 'temp'
# and only if the test fails will the directory be created.
 shellscripts$ [ -d temp ] || mkdir temp
```

# Flow Control

- Docs: [Compound Commands](https://www.gnu.org/software/bash/manual/bashref.html#Compound-Commands)
- http://tldp.org/LDP/abs/html/loops1.html
- http://tldp.org/HOWTO/Bash-Prog-Intro-HOWTO-6.html

Note that wherever a `;` appears in the description of a command’s syntax, it may be replaced with one or more newlines.

## Syntaxes

| Construct | Syntax |
| --------- | ------ |
| `until` | `until test-commands; do consequent-commands; done` |
| `while` | `while test-commands; do consequent-commands; done` |
| `for` | `for name [ [in [words …] ] ; ] do commands; done`<br>or<br>`for (( expr1 ; expr2 ; expr3 )) ; do commands ; done` |
| `case` | `case word in [ [(] pattern [| pattern]…) command-list ;;]… esac` |
| `select` | `select name [in words …]; do commands; done` |
| `if` | <code>if test-commands; then<br>    consequent-commands;<br>[elif more-test-commands; then<br>    more-consequents;]<br>[else alternate-consequents;]<br>fi</code> |

## `for`

```bash
 ~$ var1=foo
 ~$ var2=bar
 ~$ for arg in $var1 $var2;
> do
>     echo $arg
> done
foo
bar

 ~$ for planet in Mercury Venus Earth Mars Jupiter Saturn Uranus Neptune Pluto
> do
>   echo $planet
> done
Mercury
Venus
Earth
Mars
Jupiter
Saturn
Uranus
Neptune
Pluto

 shellscripts$ filename="*txt"
 shellscripts$
 shellscripts$ for file in $filename
> do
>    echo "Contents of $file"
>    echo "---"
>    cat "$file"
>    echo
> done
Contents of foo.txt
---

Contents of ls-error.txt
---
ls: /path/does/not/exist/: No such file or directory

Contents of ls-output.txt
---
ls: /bin/usr: No such file or directory

Contents of redirected.txt
---
some text here
```

## `if`

Syntax:

```
if test-commands; then
  consequent-commands;
[elif more-test-commands; then
  more-consequents;]
[else
    alternate-consequents;]
fi
```

The _expression_ syntax itself is at https://www.gnu.org/software/bash/manual/bashref.html#Bash-Conditional-Expressions.

```bash
# The key here is the *return* value!
 ~$ true
 ~$ if [ `echo $?` ]; then
>     echo "true indeed"
> fi
true indeed
```

See also: `man test`.

Another example:

```bash
 ~$ x=5
 ~$ if [ $x = 5 ]; then
>     echo "x equals 5."
> fi
x equals 5.
 ~$ if [ $x -eq 5 ]; then
>     echo "it still does"
> fi
it still does
```

Combining `if` and `for` with a logical AND (`&&`):

```bash
 ~$ var1=5; var2=8
 ~$ for var in $var1 $var2
> do
>     if [[ $var -lt 7 && $var -gt 4 ]]; then
>         echo "$var is gt 4 and lt 7"
>     else
>         echo "$var is not"
>     fi
> done
5 is gt 4 and lt 7
8 is not
```

## `case`

The bash multiple-choice compound command is called `case`.  Its formal syntax is

```
case word in
    [ [(] pattern [| pattern]...) command-list ;;]...
esac
```

Example:

```bash
filemode () {
    # Get the octal representation from file
    # mode as a string.
    # filemode rwx --> 7
    case $1 in
        "---")      echo 0;;
        "--x")      echo 1;;
        "-w-")      echo 2;;
        "-wx")      echo 3;;
        "r--")      echo 4;;
        "r-x")      echo 5;;
        "rw-")      echo 6;;
        "rwx")      echo 7;;
        *)          echo "Invalid entry" >&2
                    exit 1
                    ;;
    esac
}

 ~$ filemode rwx
7
 ~$ filemode bad
Invalid entry
```

# Getting Help

Simply typing `help` gets you a non-exhaustive list of commands and their options.

You can type `help name` to find out more about the function `name`.

```bash
$ help pwd
pwd: pwd [-LP]
    Print the current working directory.  With the -P option, pwd prints
    the physical directory, without any symbolic links; the -L option
    makes pwd follow symbolic links.
```

Note that only the commands listed under `help` are available through `help name`.  Some, like `help ls`, will throw an error because they aren't present in the list.  `help` gets you acccess to **built-in** shell commands.  A list of built-ins can be found at `man builtin`.

Another form of documentation is man pages (short for manual).  This directory is more extensive than `help`.  To access a man page, type the `man` command followed by the name of the thing you want to look up: `man <command>`.  The link to the full OS X Man Pages is [here](https://developer.apple.com/legacy/library/documentation/Darwin/Reference/ManPages/).  To exit, press "q."

`man command` where `command` is a builtin will redirect to `man builtin`, i.e. all the commands you can examine with `help`.

# Keyboard Shortcuts

| Key | Use |
| --- | --- |
| ArrowUp | Step through recent commands, starting with the most recently used. |
| ArrowDown | Step forwards towards more recent commands. |
| CTRL+A | Move cursor to beginning of line. |
| CTRL+E | Move cursor to end of line. |
| CTRL+C | Abort a command. |
| CTRL+U | Delete all to **left** of cursor. |
| CTRL+K | Delete all to **right** of cursor. |
| CTRL+W | Delete the word before the cursor only. |
| CTRL+R | Search your command history for specific phrases. |
| !! | Alias for the last command run. |

# Invoking a Script

So, you've written a script, say `helloworld` (no extension):

```bash
 shellscripts$ echo "echo hello world" > helloworld
 shellscripts$ cat helloworld
echo hello world
```
How do you call the script from the command line?  There are two ways:

1. Invoke it by `bash helloworld` or `sh helloworld`, following the call syntax `bash [options] [command_string | file]`.  (`sh` may turn off Bash-specific extensions.)
2. make the script itself directly executable with `chmod mode file`.  This is the preferred method.

For an easy explanation of `mode`s for `chmod`, see Schotts - _The Linux Command Line_, chapter 9.  A few common ones are:

```bash
chmod 555 helloworld  # read-execute permission for everyone
chmod 755 helloworld  # read-write-ex permission for owner, read-ex for others
chmod 700 helloworld  # only owner
```

Keep in mind that a script **needs read**, as well as execute permission for it to run, since the shell needs to be able to read it.

Here's a function that gets the corresponding code (requires Bash 4+):

```bash
 ~$ filemode () {
>     declare -A modes
>     modes=( ["---"]=0 ["--x"]=1 ["-w-"]=2 ["-wx"]=3 ["r--"]=4 ["r-x"]=5 ["rw-"]=6 ["rwx"]=7 )
>     echo ${modes[$1]}
> }
 ~$ filemode rwx
7
```

Now, call the script:

```bash
 shellscripts$ ./helloworld
hello world
```

Notice the leading dot, indicating the current directory.  Why is this needed?  If `helloworld` is _not_ in `$PATH`, the script will not be found.

As a final step, you can place the script somewhere in `$PATH`.  One common location for "user-only" scripts is `~/bin/`, or `/usr/local/bin/` for scripts to be shared.  Then `export PATH="~/bin/:$PATH"` in your `.bash_profile`.  The script could then be invoked by simply typing `scriptname [ENTER]` from the command line.

## Shebang Line

`#!/bin/bash` is the proper first line for a Bash script.  If Bash is your default shell, then the `#!` isn't technically necessary, but it's best to have it for portability.

This is the path to the program that interprets the commands in the script, whether it be a shell, a programming language, or a utility.  It tells your system that this file is a set of commands to be fed to the command interpreter indicated.

## What File Extension Do I Use? (`.sh`, `.bash`)

The short answer is that you don't technically need either.  The naming of the script is for "aesthetic purposes" and has nothing to do with how it's run.

From [Advanced Bash-Scripting Guide](https://linux.die.net/abs-guide/why-shell.html):

> By convention, user-written shell scripts that are Bourne shell compliant generally take a name with a `.sh`extension.

The more important distinction is which is used in the shebang line.  `#!/bin/sh` may not be the same as `#!/bin/bash`.

## The `exit` command

Using `exit` is the right and proper method of "exiting" from a script.

- `exit [n]` exits the shell with a status of `n`.
- If `n` is omitted, the exit status is that of the last command executed.
- 0 is the only "okay" return code; all others indicate errors of some type.
- When executed, the exit status of a function is the exit status of the last command executed in the body.
- `$?` is a special Bash variable that’s set to the exit code of each command after it runs.
- tldp.org: [Reserved Exit Codes](http://tldp.org/LDP/abs/html/exitcodes.html#EXITCODESREF)

```bash
# Illustration of `$?`
 ~$ grep not_there /dev/null
 ~$ echo $?
1
 ~$ echo "a man's dream" | grep man
a man's dream
 ~$ echo $?
0
```

# Other Tricks

## Show Hidden Files

By default, the Finder in OS X hides some files away from view (mostly irrelevant ones) but if you want to see everything on your computer, then use:

```bash
defaults write com.apple.finder AppleShowAllFiles TRUE
```
## Change Frequency with Which App Store Checks for Updates

The integer is the day-frequency of update-checking.

```bash
defaults write com.apple.SoftwareUpdate ScheduleFrequency -int 1
```

## Forcing Mac not to Sleep

Sometimes, you don’t want your computer to fall asleep automatically. You can "caffeinate" your Mac so that it doesn’t fall asleep until you say so:

```bash
$ caffeinate
```

You can give your Mac a break once it is done by hitting `Control+C` in the Terminal or quitting Terminal altogether. Yes, this command only continues to work as long as Terminal stays open.

Perhaps you need your computer to stay awake for a few hours but want it to go to sleep after a set time when the task it needs to finish completes. It’s easy. All you have to do is enter the following command:

```bash
$ caffeinate -i -t 3600
```

The number at the end represents the number of seconds. So, 3600 = 1 hour.

## Downloading Files

We can use `curl` for this in place of `wget`, which is not available by defualt on all systems.

```bash
# Save the downloaded .zip to Downloads/
$ curl http://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/F-F_Research_Data_Factors_CSV.zip --output Downloads/frenchdata.zip
```

## Zipping & Unzipping

View info without unzipping with `zipinfo`.  For other extensions you may need `gzip`, `tar`, or `bzip2`.

```bash
~ $ zipinfo Downloads/frenchdata.zip
Archive:  Downloads/frenchdata.zip
Zip file size: 12071 bytes, number of entries: 1
-rw-a--     6.3 fat    52440 bx defN 17-Nov-27 11:08 F-F_Research_Data_Factors.CSV
1 file, 52440 bytes uncompressed, 11879 bytes compressed:  77.3%
```

Alternatives:
- `tar -tf Downloads/frenchdata.zip`


Unzip the contents from above to a new directory:

```bash
$ unzip frenchdata.zip -d frenchdata/
```

Zipping contents of a folder:

```bash
~ $ ls Downloads/
file1.txt   file2.txt   file3.txt   file4.txt
~ $ tar -zcvf my_archive.tar.gz Downloads/
```

## Dragging Files to Terminal

You can drag a file directly to Terminal to add its file path to the command line.

https://www.youtube.com/watch?v=mgazHxDtiu8

## Process Information

Use `top` to mimic the functionality of Window's Task Manager.  The top program periodically displays a sorted list of system processes.  The default sorting key is pid, but other keys can be used instead.

```bash
$ top -o cpu  # sort by cpu usage descending
Processes: 332 total, 2 running, 330 sleeping, 1253 threads            17:35:08
Load Avg: 1.64, 1.78, 1.65  CPU usage: 6.29% user, 5.32% sys, 88.37% idle
SharedLibs: 196M resident, 55M data, 20M linkedit.
MemRegions: 39801 total, 2567M resident, 164M private, 1108M shared.
PhysMem: 7382M used (2177M wired), 809M unused.
VM: 1458G vsize, 1096M framework vsize, 0(0) swapins, 0(0) swapouts.
Networks: packets: 1669245/2252M in, 427135/55M out.
Disks: 497805/8364M read, 308242/7396M written.

PID   COMMAND      %CPU TIME     #TH   #WQ  #PORT MEM    PURG   CMPRS  PGRP PPID
2038  Terminal     12.6 00:41.13 10    5    348   70M+   1836K- 0B     2038 1
0     kernel_task  7.2  22:28.95 152/4 0    2     833M   0B     0B     0    0
```

## Making Your Own Shorthand: Aliases

In your `~/.bash_profile`, you can create a custom shortcut called an `alias`.  Add a line like this to `~/.bash_profile`:

```bash
alias la='ls -A'
```

Now, whenever you type `la`, the Terminal will run `ls` with the `-a` modifier, which includes hidden files.

## Word Count

Use `wc`.  Outputs: word, line, character, and byte count.

## Shorten the Prompt

Manual: https://www.gnu.org/software/bash/manual/bashref.html#Controlling-the-Prompt

In `~/.bash_profile`, add:

```bash
PS1='\W \$ '
```

to abbreviate your prompt to the working directory + a "$".

For more options: [Bash Shell PS1: 10 Examples to Make Your Linux Prompt like Angelina Jolie](https://www.thegeekstuff.com/2008/09/bash-shell-ps1-10-examples-to-make-your-linux-prompt-like-angelina-jolie/)

## Execute in Background

Add `&` to end of command:

```bash
 shellscripts$ cp funcs funcs2 &
[1] 3546
 shellscripts$ atq
[1]+  Done                    cp -i funcs funcs2
 shellscripts$ atq  # null
```

If a command is terminated by the control operator `&`, the shell executes the command asynchronously in a subshell. This is known as executing the command in the background. The shell does not wait for the command to finish, and the return status is 0 (true).

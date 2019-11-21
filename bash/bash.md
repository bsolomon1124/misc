# Bash

## Contents

<!---toc start-->

* [Bash](#bash)
  * [Contents](#contents)
  * [Covered Here](#covered-here)
  * [Resources & References](#resources--references)
  * [Version](#version)
  * [Terminology](#terminology)
  * [Bash Syntax](#bash-syntax)
    * [Command Usage](#command-usage)
    * [Control Operators](#control-operators)
    * [Reserved Words](#reserved-words)
    * [Pipelines](#pipelines)
    * [Lists](#lists)
    * [Conditional Expressions](#conditional-expressions)
    * [Quoting](#quoting)
      * [Examples](#examples)
    * [Special Parameters](#special-parameters)
    * [Redirection](#redirection)
      * [Redirecting Input](#redirecting-input)
      * [Redirecting Output](#redirecting-output)
        * [Redirect `stderr`](#redirect-stderr)
        * [Redirect `stderr` to `stdout` (and Vice Versa)](#redirect-stderr-to-stdout-and-vice-versa)
        * [Redirect `stderr` _and_ `stdout`](#redirect-stderr-and-stdout)
    * [Flow Control](#flow-control)
      * [`for`](#for)
      * [`if`](#if)
      * [`case`](#case)
    * [Expansion](#expansion)
      * [Command Substitution](#command-substitution)
      * [Variable/Parameter Substitution](#variableparameter-substitution)
      * [Brace Expansion](#brace-expansion)
      * [Filename/Pathname Expansion](#filenamepathname-expansion)
      * [History Expansion](#history-expansion)
        * [Event Designators](#event-designators)
        * [Word Designators](#word-designators)
    * [Shell Functions](#shell-functions)
      * [Scope](#scope)
    * [Prompt Strings](#prompt-strings)
    * [Arrays](#arrays)
      * [General Rules](#general-rules)
      * [Indexed Arrays](#indexed-arrays)
      * [Associative Arrays](#associative-arrays)
      * [Examples](#examples-1)
    * [Environment Variables](#environment-variables)
    * [The Home Directory](#the-home-directory)
    * [Special Path Characters](#special-path-characters)
    * [Initialization Files: `.bash_profile` and `.bashrc`](#initialization-files-bash_profile-and-bashrc)
    * [Shebang Line](#shebang-line)
    * [Interactive Shells & Login Shells](#interactive-shells--login-shells)
    * [Invoking a Script](#invoking-a-script)
      * [What File Extension Do I Use? (`.sh`, `.bash`)](#what-file-extension-do-i-use-sh-bash)
  * [Builtins](#builtins)
    * [`mkdir`](#mkdir)
    * [`cd`](#cd)
    * [`rmdir` & `rm`](#rmdir--rm)
    * [`touch`](#touch)
    * [The Directory Stack: `dir`, `pushd` & `popd`](#the-directory-stack-dir-pushd--popd)
    * [`cp`](#cp)
    * [`mv`](#mv)
    * [Page Through a File (`less`, `more`)](#page-through-a-file-less-more)
    * [`cat`](#cat)
    * [`grep`](#grep)
    * [`exit`](#exit)
    * [Finding Things: `find` & `locate`](#finding-things-find--locate)
      * [`locate`](#locate)
      * [`find`](#find)
    * [`clear`](#clear)
    * [`alias`](#alias)
  * [Other Topics](#other-topics)
    * [Users & Superusers (`sudo`, `su`, `sudoers`)](#users--superusers-sudo-su-sudoers)
    * [Getting Help](#getting-help)
    * [Keyboard Shortcuts](#keyboard-shortcuts)

<!---toc end-->

## Covered Here

- Overview of shells & terminals
- Bash shell and `bash` interpreter
- Shell built-ins

## Resources & References

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
- [Bash man page](https://linux.die.net/man/1/bash)

## Version

`bash` version referenced here:

```bash
$ bash --version
GNU bash, version 4.4.23(1)-release (x86_64-apple-darwin18.0.0)
```

It attempts to be OS agnostic but was made from Mac OSX.

## Terminology

- The **console** is the system as a whole. This is both the command line as well as the output from previous commands.
- A **shell** is a special **command-line tool (interface)** and _interpreter_ that is designed specifically to provide text-based **interactive control over other command-line tools.**  It uses alphanumeric characters typed on a keyboard to provide instructions and data to the operating system, interactively.  From the Bash docs:

> At its base, a shell is simply a macro processor that executes commands. The term macro processor means functionality where text and symbols are expanded to create larger expressions. ... A Unix shell is both a command interpreter and a programming language.

- On Mac OSX, you **run `Terminal.app` to get access to a shell prompt.**  The Terminal is an _emulator_ and a text input/output application (_Applications > Utilities > Terminal.app_) that lets you interact with a **command-line environment.**  You could also interact with an environment using a remote connection method such as **secure shell (SSH)**.  A terminal window provides access to the input and output of a **shell process.**
- The standard OSX shell is **Bash**.  Bash is a Unix shell and command language **interpreter** first released in 1989.  In addition to running in a text window, Bash can also read and execute commands from a file, called a script.
- You run **command-line tools** (or just _commands_; one example would be `cd`) by typing the name of the tool.
    - Most tools can also take a number of **flags** aka **switches**.  `-l` would be one such flag.  Flags **change behavior.**
    - Flags can be used together after one hyphen.  For example, `-l` and `-a` are both flags to `ls`.  You can use `ls -la` to (1) display detailed info for each entry and (2) list all directory contents, including hidden files/folders.
    - Separately, some tools take **arguments**.  For example, in `ls /tmp/`, the second chunk is an argument.
- The shell (no matter the command, really) also has a notion of a **current working directory**. When you specify a filename or path that does not start with a slash, that path is assumed to be relative to this directory.  Otherwise, it is an absolute path.
    - Given a current directory `pwd` --> `/Users/brad`:
    - `bin/` is a relative path that becomes `/Users/brad/bin/`
    - `/etc/shells` is an absolute path and doesn't care what the current directory is
- The **prompt** is the beginning of the command line. It usually provides some contextual information like who you are, where you are and other useful info. It typically ends in a `$` but can be customized.

```bash
$ locate Terminal.app | grep "Terminal.app$"
/Applications/Utilities/Terminal.app
```

## Bash Syntax

These sections concern the command-line interpreter `bash` itself, mostly paraphrased from `man bash`.

### Command Usage

Usage:

```bash
$ bash [options] [command_string | file]
```

- `file` is assumed to be the name of a file containing shell commands. Bash reads and executes commands from this file, then exits.
- `bash`'s exit status is the exit status of the last command executed in the script. If no commands are executed, the exit status is 0.
- An attempt is first made to open the file in the current directory, and, if no file is found, then the shell searches the directories in `PATH` for the script.
- A double-dash (`--`) signals the end of options and disables further option processing.   Any arguments after the `--` are treated as filenames and arguments.  An argument of `-` is equivalent to `--`.

### Control Operators

A control operator is a token that performs a control function.  It is one of the following symbols:

- `||`: Establish an OR list.
- `&`: If a command is terminated by the control operator `&`, the shell executes the command in the background in a subshell.  The  shell  does not  wait  for the command to finish, and the return status is 0.
- `&&`: Establish an AND list.
- `;`: Commands separated by a ; are executed sequentially; the shell waits for each command to terminate in turn.  The return status is the exit status of the last command executed.
- `;;`
- `;&`
- `;;&`
- `(`
- `)`
- `|`: Pipe operator.  In `command | command2 ... `, the  standard output of `command` is connected via a pipe to the standard input of `command2`.
- `|&`: `command |& command2 ... `, the standard error of `command`, in addition to its standard output, is connected to `command2`'s standard input through the pipe.
- `\n`: Newlime, which may have special meaning when separating or following tokens

### Reserved Words

Reserved words are words that have a special meaning to the shell.

- `!`
- `case`
- `coproc`
- `do`
- `done`
- `elif`
- `else`
- `esac`
- `fi`
- `for`
- `function`
- `if`
- `in`
- `select`
- `then`
- `until`
- `while`
- `{` and `}`
- `time`
- `[[` and `]]`

### Pipelines

A pipeline is a sequence of one or more commands separated by one of the control operators `|` or `|&`.

- The return status of a pipeline is the exit status of the last command.
- Each command in a pipeline is executed as a separate process (i.e., in a subshell).

Basic form:

```bash
$ command [ [|||&] command2 ... ]
```

Effects:

- With `|`: The  standard output of `command` is connected via a pipe to the standard input of `command2`.
- With `|&`: The standard error of `command`, in addition to its standard output, is connected to `command2`'s standard input through the pipe.

### Lists

A list is a sequence of one or more pipelines separated by one of the operators `;`, `&`, `&&`, or `||`.

- Fire-and-forget: `&`: If a command is terminated by the control operator `&`, the shell executes the command in the background in a subshell.  The  shell  does not  wait  for the command to finish, and the return status is 0.
- Sequential: `;`: Commands separated by a ; are executed sequentially; the shell waits for each command to terminate in turn.  The return status is the exit status of the last command executed.

Separately, there are `&&` and `||` to declare AND and OR lists:

| Name | Form | Effect |
| ---- | ---- | ------ |
| AND list | `command1 && command2` | `command2` is executed if and only if `command1` returns an exit status of 0
| OR list | `command1 || command2` | `command2` is executed if and only if `command1` returns a nonzero exit status

### Conditional Expressions

Conditional  expressions  are  used  by the `[[` compound command and the `test` and `[` builtin commands to test file attributes and perform string and arithmetic comparisons.

Preferred syntax:

```bash
[[ expression ]]
```

This syntax returns a status of 0 or 1 depending on the evaluation of the conditional expression `expression`.

Expressions may be combined using the following operators, listed in decreasing order of precedence:

| Operator | Usage |
| -------- | ----- |
| `( expression )` | Returns the value of `expression`.  This may be used to override the normal precedence of operators. |
| `! expression` | True if `expression` is false. |
| `expression1 && expression2` | True if both `expression1` and `expression2` are true. |
| `expression1 || expression2` | True if either `expression1` or `expression2` is true. |

Evaluation is greedy/short-circuiting: the `&&` and `||` operators do not evaluate `expression2` if the value of `expression1` is sufficient to determine the return  value of the entire conditional expression.

Unary or binary primaries (this list excludes a few less-commonly used ones):

For files:

| Primary | Usage |
| ------- | ----- |
`-a file` | True if `file` exists. |
`-b file` | True if `file` exists and is a block special file. |
`-c file` | True if `file` exists and is a character special file. |
`-d file` | True if `file` exists and is a directory. |
`-e file` | True if `file` exists. |
`-f file` | True if `file` exists and is a regular file. |
`-g file` | True if `file` exists and is set-group-id. |
`-h file` | True if `file` exists and is a symbolic link. |
`-k file` | True if `file` exists and its "sticky" bit is set. |
`-p file` | True if `file` exists and is a named pipe (FIFO). |
`-r file` | True if `file` exists and is readable. |
`-s file` | True if `file` exists and has a size greater than zero. |
`-t fd`   | True if file descriptor `fd` is open and refers to a terminal. |
`-u file` | True if `file` exists and its set-user-id bit is set. |
`-w file` | True if `file` exists and is writable. |
`-x file` | True if `file` exists and is executable. |
`-G file` | True if `file` exists and is owned by the effective group id. |
`-L file` | True if `file` exists and is a symbolic link. |
`-N file` | True if `file` exists and has been modified since it was last read. |
`-O file` | True if `file` exists and is owned by the effective user id. |
`-S file` | True if `file` exists and is a socket. |

For variables:

| Primary | Usage |
| ------- | ----- |
| `-v varname` | True if the shell variable `varname` is set (has been assigned a value). |
| `-R varname` | True if the shell variable `varname` is set and is a name reference. |

For strings:

| Primary | Usage |
| ------- | ----- |
| -z string | True if the length of string is zero.
| `string1 == string2` or `string1 = string2` | True  if  the  strings are equal (prefer to use `==`) |
| `string1 != string2` | True if the strings are not equal. |
| `string1 < string2` | True if string1 sorts before string2 lexicographically. |
| `string1 > string2` | True if string1 sorts after string2 lexicographically. |

Arithmetic binary operators:

| Primary | Usage |
| ------- | ----- |
| `-eq` | Equal to |
| `-ne` | Not equal to |
| `-lt` | Less than |
| `-le` | Less than or equal to |
| `-gt` | Greater than |
| `-ge` | Greater than or equal to |

These are used as `arg1 OP arg2` where `arg1` and `arg2` may be positive or negative integers.

### Quoting

Quoting  is  used  to  remove  the special meaning of certain characters or words to the shell.

There are three quoting mechanisms:

1. the escape character: a non-quoted backslash (`\`)
2. single quotes: preserves the literal value of each character within the quotes.
3. double quotes: preserves the literal value of all characters within the quotes, _except_ `$`, <code>\`</code>, `\`, and, when history expansion is enabled, `!`.  The special parameters `*` and `@` have special meaning when in double quotes

Short answer: Double quotes dereference variables, while single quotes _always_ go literal.

#### Examples

```bash
$ a='first' b="second"
$ echo $a
first
$ echo "$a"
first
$ echo '$b'
$b
```

### Special Parameters

The shell treats several parameters specially.  These parameters may only be referenced; assignment to them is not allowed.

You can get these by prefacing them with `$`; that is, you can access what is represented by `?` by using parameter expansion, `$?`.

| Parameter | Meaning |
| --------- | ------- |
| `*` | Expands to the positional parameters, starting from one.  That is, `$*` is equivalent to `"$1c$2c..."`, where c is the first character of the value of the `IFS` environment variable.  If IFS is unset, the parameters are separated byspaces.   If  IFS  is  null,  the parameters are joined without intervening separators. |
| `@` | Expands to the positional parameters, starting from one.  When the expansion occurs within double quotes, each parameter expands to a separate word.  That is, `$@` is equivalent to `"$1" "$2" ...` |
| `#` | Expands to the number of positional parameters in decimal. |
| `?` | Expands to the exit status of the most recently executed foreground pipeline. |
| `-` | Expands  to  the current option flags as specified upon invocation, by the set builtin command, or those set by the shell itself (such as the `-i` option). |
| `$` | Expands to the process ID of the shell.  In a `()` subshell, it expands to the process ID of the current shell, not the subshell. |
| `!` | Expands  to  the  process ID of the job most recently placed into the background. |
| `0` | Expands to the name of the shell or shell script. |

Example:

```bash
function paramdemo() {
	echo -n "*: " && echo $*
	echo -n "@: " && echo $@
	echo -n "1: " && echo $1
	echo -n "2: " && echo $2
	echo -n "3: " && echo $3
	echo -n "#: " && echo $#
	echo -n "?: " && echo $?
	echo -n "-: " && echo $-
	echo -n "$: " && echo $$
	echo -n "!: " && echo $!
	echo -n "0: " && echo $0
}
```

Use:

```bash
$ paramdemo
*:
@:
1:
2:
3:
#: 0
?: 0
-: himBHs
$: 783
0: -bash

$ paramdemo uno dos tres
*: uno dos tres
@: uno dos tres
1: uno
2: dos
3: tres
#: 3
?: 0
-: himBHs
$: 783
0: -bash
```

### Redirection

> More examples: [All about redirection](http://tldp.org/HOWTO/Bash-Prog-Intro-HOWTO-3.html)

Before a command is executed, its input and output may be redirected using a special notation interpreted by the shell.  I/O redirection allows us to change:

- where output goes
- where input comes from

Redirections are processed in the order they appear, from left to right.

Keeping with the Unix theme of "everything is a file," programs such as `ls` actually send their results to a special file called standard output (often expressed as stdout) and their status messages to another file called standard error (stderr).  (These are at `/dev/stdout` ...)

```bash
$ ls /dev | grep "std.*"
stderr
stdin
stdout
```

Basic examples of redirecting stdout to a filesystem file:

```bash
$ # Example 1
$ # Same as echo "some text here" 1> redirected.txt
$ echo "some text here" > redirected.txt
$ cat redirected.txt
some text here

$ # Example 2
$ ls -l /usr/bin > ls-output.txt
$ head -n 5 ls-output.txt
total 139056
-rwxr-xr-x   4 root   wheel       925 Jul 15  2017 2to3-
lrwxr-xr-x   1 root   wheel        74 Nov 18 14:05 2to3-2.7 -> ../../System/Library/Frameworks/Python.framework/Versions/2.7/bin/2to3-2.7
-rwxr-xr-x   1 root   wheel     55072 Mar 28 00:02 AssetCacheLocatorUtil
-rwxr-xr-x   1 root   wheel     53472 Mar 28 00:02 AssetCacheManagerUtil
```

Filter descriptor number refresher:

- fd 0: standard input
- fd 1: standard output
- fd 2: standard error

#### Redirecting Input

General form:

```bash
cmd [n]<[|]word
```

This causes the file whose name results from the expansion of `word` to be opened for reading on file descriptor `n`, or the standard input (file descriptor 0) if `n` is not specified.

**Default**: If the file descriptor number `n` is omitted, and the first character of the redirection operator is `<`, the redirection refers to the standard input (file descriptor 0).

Here's an example of redirecting stdin: `cat` with no arguments reads from stdin.  Using the `<` redirection operator, we change the source of standard input from the keyboard to a file. We see that the result is the same as passing a single filename argument.

```bash
$ cat < redirected.txt
some text here
```

#### Redirecting Output

General form:

```bash
cmd [n]>[|]word
```

This causes the file whose name results from the expansion of `word` to be opened for writing on file descriptor `n`, or the standard output (file descriptor 1) if `n` is not specified.

**Default**: If the first character of the redirection operator is `>`, the redirection refers to the standard output (file descriptor 1).

Notes:

- If the file does not exist it is created; if it does exist it is truncated to zero size.
- With just `>`: the redirection will fail if the file whose name results from the expansion of `word` exists and is a regular file.
    - This will only fail _if_ the `noclobber` option to the `set` builtin has been enabled.
- With `>|`: the redirection is attempted even if the file named by word exists.
- Using just `> word` truncates the file `word`.
- Appending redirected output: `[n]>>word`
    - Causes the file whose name results from the expansion of `word` to be opened for appending on file descriptor `n`, or the standard output (file descriptor 1) if `n` is not specified.
    - If the file does not already exist, it is created just as though the `>` operator had been used.

##### Redirect `stderr`

You do this by using `n=2` in the syntax `n>word`.

Example: if `ls` encounters an error, it by default sends this to stderr.  We can redirect that error to `ls-error.txt`

```bash
$ ls -l /path/does/not/exist/ 2> ls-error.txt  # n=2 here in n>word syntax
$ cat ls-error.txt
ls: /path/does/not/exist/: No such file or directory
```

Example 2: Suppress error messages by redirecting to `/dev/null`, which is a _bit bucket_ that accepts input and does nothing with it.

```bash
$ # Suppress error msgs
$ ls /path/dne/ 2> /dev/null
```

##### Redirect `stderr` to `stdout` (and Vice Versa)

This is a specialized case where, in the syntax `[n]>[|]word`, you need `word` to represent `stderr`.  `&` is only interpreted to mean "file descriptor" in the context of redirections.

```bash
$ # Redirect  stdout to stderr
$ echo test 1>&2 # or echo test >&2, 1 is default for n
```

##### Redirect `stderr` _and_ `stdout`

The preferred (newer) way to redirect both stdout and stderr to the same place is `&>`:

```bash
$ # &> is same as >&
$ ls -l /bin/usr &> ls-output.txt
```

Note that this is semantically equivalent to `>word 2>&1`, which is an older syntax.

### Flow Control

How-tos:

- Docs: [Compound Commands](https://www.gnu.org/software/bash/manual/bashref.html#Compound-Commands)
- http://tldp.org/LDP/abs/html/loops1.html
- http://tldp.org/HOWTO/Bash-Prog-Intro-HOWTO-6.html

Notes:

- Wherever a `;` appears in the description of a command’s syntax, it may be replaced with one or more newlines.
- The syntaxes below are incomplete; they may omit brackets (denoting optionality) to stick with the common-case.

| Construct | Syntax |
| --------- | ------ |
| `until` | `until list-1; do list-2; done` |
| `while` | `while list-1; list-2; done` |
| `for` | `for name in words ; do list ; done`<br>or<br>`for (( expr1 ; expr2 ; expr3 )) ; do list ; done` |
| `case` | `case word in [ [(] pattern [ | pattern ] ... ) list ;; ] ... esac` |
| `select` | `select name in words; do list; done` |
| `if` | `if list; then list; [ elif list; then list; ] ... [ else list; ] fi` |

#### `for`

```bash
$ var1=foo
$ var2=bar
$ for arg in $var1 $var2;
> do
>     echo $arg
> done
foo
bar

$ for planet in Mercury Venus Earth Mars Jupiter Saturn Uranus Neptune Pluto
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

$ filename="*txt"
$ for file in $filename
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

#### `if`

The _expression_ syntax itself is at https://www.gnu.org/software/bash/manual/bashref.html#Bash-Conditional-Expressions.

```bash
$ # The key here is the *return* value!
$ true
$ if [ `echo $?` ]; then
>     echo "true indeed"
> fi
true indeed
```

See also: `man test`.

Another example:

```bash
$ x=5
$ if [ $x -eq 5 ]; then
>     echo "x equals 5."
> fi
x equals 5.
```

Combining `if` and `for` with a logical AND (`&&`):

```bash
$ var1=5; var2=8
$ for var in $var1 $var2
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

#### `case`

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

$ filemode rwx
7
$ filemode bad
Invalid entry
```

### Expansion

Manual: [shell expansions](https://www.gnu.org/software/bash/manual/bashref.html#Shell-Expansions)

Expansion is performed on the command line after it has been split into tokens. There are seven kinds of expansion performed:

- brace expansion
- tilde expansion (`echo ~`)
- parameter and variable expansion
- command substitution
- arithmetic expansion
- word splitting
- filename expansion

#### Command Substitution

Command substitution **allows the output of a command to replace the command itself.**

Use either

```bash
$(command)  # newer
```

or

```bash
`command`  # old
```

```bash
$ my_wd=`pwd`
$ echo $my_wd
/Users/brad/Scripts/playground/shellscripts

$ ls -l $(which cp)
-rwxr-xr-x  1 root  wheel  29008 Oct 25  2017 /bin/cp

$ file $(ls /usr/bin/* | grep zip)
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

#### Variable/Parameter Substitution

The basic form of parameter & variable expansion is `${parameter}` or just `$parameter`.  Use the former if you need to protect the variable to be expanded from characters immediately following it which could be interpreted as part of the name.

```bash
$ foo=bar
$ qux=7
$ echo $foo
bar
$ echo $qux
7
$ echo ${qux}{foo}
7{foo}
$ echo ${qux}${foo}
7bar
$ echo 1${qux}10
1710
```

There is a whole host of special syntax that can be used within the braces.  For example, `${parameter:-word}` says, "If `parameter` is unset or null, the expansion of `word` is substituted. Otherwise, the value of `parameter` is substituted."

```bash
$ def=10  # is defined
$ echo ${def:-default}
10
$ echo ${undef:-default}
default
```

For the full list, see [Shell Parameter Expansion](https://www.gnu.org/software/bash/manual/bashref.html#Shell-Parameter-Expansion).

With parameter expansion, if you misspell the name of a variable, the expansion will still take place but will result in an empty string:

```bash
$ echo $SUER

```

#### Brace Expansion

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
$ ls pckg
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

#### Filename/Pathname Expansion

TODO

#### History Expansion

History expansion is the ability to denote and expand commands in your `~/.bash_history` (previous commands you've typed) or even specific words from those commands.

History expansions introduce words from the history list into the input stream, making it easy to repeat commands, insert the arguments to a previous command into the current input line, or fix errors in previous commands quickly.

Types of history expansion fall into two categories:

- Event designators: a reference to a command line entry in the history list
- Word designators: used to select desired words from an event

##### Event Designators

Event designators:

| Designator | Meaning |
| ---------- | ------- |
| `!-n` | Refer to _n_ commands ago |
| `!!` | Previous command |
| `!string` | Refer to the most recent command starting with `string` |
| `!?string[?]` | Refer to the most recent command containing `string`. The trailing `?` may be omitted if `string` is followed immediately by a newline |
| `^ string1 ^ string2 ^` | Quick substitution. Repeat the last command, replacing `string1` with `string2 |

Examples:

```bash
$ echo first
first
$ echo second
second
$ !!  # Refer to previous command
echo second  # Refer to previous command
second
$ echo first again
first again
$ echo second again
second again
$ !-2  # Refer to 2 commands ago
echo first again  # Refer to 2 commands ago
first again
```

##### Word Designators

Word designators:

| Designator | Meaning |
| ---------- | ------- |
| `!^` | Initial argument (`:` is optional in middle) |
| `!$` | Final argument (`:` is optional in middle) |
| `!:n` | The `n`th word |
| `!:x-y` | A range of words; `-y` abbreviates `0-y`z |

Word designators are **zero-indexed**: Words are numbered from the beginning of the line, with the first word being denoted by 0 (zero).

Examples:

```
$ echo one two three four
one two three four
$ echo !^  # First argument
echo one  # First argument
one

$ echo one two three four
one two three four
$ echo !$  # Last argument
echo four  # Last argument
four

$ echo one two three four
one two three four
$ echo !:2
echo two
two

$ echo one two three four
one two three four
$ echo !:2-3
echo two three
two three
```

### Shell Functions

A shell function is an object that is called like a simple command and executes a compound command with a new set of positional parameters.  Shell functions are declared as follows; the reserved word `function` is optional:

```bash
$ name () compound-command [redirection]
$ function name [()] compound-command [redirection]
```

When using the braces, the list inside brackets must be terminated by a semicolon, a "&", _or_ a newline:

$ func () { echo "defined"; }  # semicolon required

To delete a function: `unset -f name`

```
$ func () { echo "defined"; }
$ func
defined
$ unset -f func
$ func
-bash: func: command not found
```

When a function is executed, the arguments to the function become the positional parameters during its execution

`$*` expands to the positional parameters, starting from one.

```bash
$ function params { echo $*; }
$ params 1 2 3 4 5
1 2 3 4 5
```

To list functions: `declare -f`.

#### Scope

Variables local to the function may be declared with the `local` builtin. These variables are visible only to the function and the commands it invokes.

```bash
$ HELLO=Hello
$ function hello {
>         local HELLO=World
>         echo $HELLO
> }
$ echo $HELLO
Hello
$
$ hello
World
$ echo $HELLO
Hello
```

### Prompt Strings

- `PS1`: displayed when `bash` is ready to read a command.  Default: `\s-\v\$ `
- `PS2`: displayed by `bash` when it needs more input to complete a command.  Default: `> `
- `PS0`: displayed by `bash` after it reads a command but before executing it

Allowed escape characters:

| Character | Meaning |
| --------- | ------- |
| `\a`   | an ASCII bell character (07)
| `\d`   | the date in "Weekday Month Date" format (e.g., "Tue May 26") |
| `\D{format}` | the  format  is  passed  to  strftime(3)  and the result is inserted into the prompt string; an empty format results in a locale-specific time representation.  The braces are required |
| `\e`   | an ASCII escape character (033) |
| `\h`   | the hostname up to the first `.` |
| `\H`   | the hostname |
| `\j`   | the number of jobs currently managed by the shell |
| `\l`   | the basename of the shell's terminal device name |
| `\n`   | newline |
| `\r`   | carriage return |
| `\s`   | the name of the shell |
| `\t`   | the current time in 24-hour HH:MM:SS format |
| `\T`   | the current time in 12-hour HH:MM:SS format |
| `\@`   | the current time in 12-hour am/pm format |
| `\A`   | the current time in 24-hour HH:MM format |
| `\u`   | the username of the current user |
| `\v`   | the version of bash (e.g., 2.00) |
| `\V`   | the release of bash, version + patch level (e.g., 2.00.0) |
| `\w`   | the current working directory, with $HOME abbreviated with a tilde (uses the value of the PROMPT_DIRTRIM variable) |
| `\W`   | the basename of the current working directory, with $HOME abbreviated with a tilde |
| `\!`   | the history number of this command |
| `\#`   | the command number of this command |
| `\$`   | if the effective UID is 0, a #, otherwise a $ |
| `\nnn` | the character corresponding to the octal number nnn |
| `\\`   | a backslash |
| `\[`   | begin a sequence of non-printing characters, which could be used to embed a terminal control sequence into the prompt |
| `\]`   | end a sequence of non-printing characters |


Manual: https://www.gnu.org/software/bash/manual/bashref.html#Controlling-the-Prompt

In `~/.bash_profile`, add:

```bash
PS1='\W \$ '
```

to abbreviate your prompt to the working directory + a "$".

For more options: [Bash Shell PS1: 10 Examples to Make Your Linux Prompt like Angelina Jolie](https://www.thegeekstuff.com/2008/09/bash-shell-ps1-10-examples-to-make-your-linux-prompt-like-angelina-jolie/)

Another example:

```bash
STARTCOLOR="\[\e[0;32m\]"  # Escape color literals or prompt will overwrite itself
ENDCOLOR="\[\e[0m\]"
export PS1_VERBOSE="$STARTCOLOR\u@\H: \s\v [\D{%Y-%m-%d} \t] \w \$ $ENDCOLOR"
```

See also: [bash:tip_colors_and_formatting](https://misc.flogisoft.com/bash/tip_colors_and_formatting)

### Arrays

Docs: [Arrays](https://www.gnu.org/software/bash/manual/bashref.html#Arrays)

#### General Rules

- There is no maximum limit on the size of an array, nor any requirement that members be indexed or assigned contiguously.
- Any element of an array may be referenced using `${name[subscript]}`
- Expand to all members: `${name[@]}` or `${name[*]}`.  When there are no array members, `${name[@]}` expands to nothing.
- See the keys: `${!name[@]}` or `${!name[*]}`
- Referencing an array variable without a subscript is equivalent to referencing with a subscript of 0.
- To destroy, use `unset`:
    - `unset name[subscript]` destroys the array element at index `subscript`.
    - `unset name` destroys the array

#### Indexed Arrays

- Indexed arrays are referenced using integers and are zero-based.
- An indexed array is created automatically if any variable is assigned to using the syntax `name[subscript]=value`.
- To create: `declare -a name`
- To assign: `name=( [sub1]=string1 [sub2]=string2 ... )`, or just `name=( val1 val2 val3 ... )`

#### Associative Arrays

- Available in Bash 4+.  Check `echo $BASH_VERSION` and [upgrade to Bash 4](http://clubmate.fi/upgrade-to-bash-4-in-mac-os-x/) if needed.
- Associative arrays use arbitrary strings as indexes.
- To create: `declare -A name`
- To assign: `name=( [sub1]=string1 [sub2]=string2 ... )`

#### Examples

```bash
$ echo $BASH_VERSION
4.4.19(1)-release

$ declare -A modes
$ modes=( ["---"]=0 ["--x"]=1 ["-w-"]=2 ["-wx"]=3 ["r--"]=4 ["r-x"]=5 ["rw-"]=6 ["rwx"]=7 )
$ echo ${modes["r--"]}
4
$ echo ${modes[@]}
3 0 5 6 2 7 4 1

$ declare -a iarr
$ iarr=( 1 9 0 8 )
$ echo ${iarr[@]}
1 9 0 8
$ echo ${!iarr[@]}
0 1 2 3

# Referencing an array variable without a subscript is
# equivalent to referencing with a subscript of 0.
$ echo $iarr
1
```

### Environment Variables

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

### The Home Directory

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

$ tree -F -L 1 /
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

### Special Path Characters

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

### Initialization Files: `.bash_profile` and `.bashrc`

`/etc/profile`
`~/.bash_profile`
`~/.bash_login`
`~/.profile`
`~/.bashrc`

You can use `bash --rcfile <file>` to execute commands from `file` instead of the standard personal initialization file `~/.bashrc` if the shell is interactive.

### Shebang Line

`!/usr/bin/env bash` is the proper first line for a Bash script.  If Bash is your default shell, then the `#!` isn't technically necessary, but it's best to have it for portability.  (You'll often see just `/bin/bash`, where the executable is pretty much always located.)

This is the path to the program that interprets the commands in the script, whether it be a shell, a programming language, or a utility.  It tells your system that this file is a set of commands to be fed to the command interpreter indicated.

### Interactive Shells & Login Shells

Login shell: one whose first character of argument zero is a `-`, or one started with the `-l`/`--login` option.

- Commands are run with user-interaction from keyboard
- `Terminal.app` on Mac OSX runs a login shell by default (not true of Linux)

Interactive shell: one started _without non-option arguments_, or one started with the `-i` option.

- An example of running _non interactively_ is running a shell script, i.e. `./myscript.bash` or `./myscript.sh`, where the script has the `#! /bin/bash` shebang and is executable.

```bash
$ bash -i  # Interactive
$ bash -l  # Make bash act as if it had been invoked as a login shell
```

To tell if you are in a login shell:

```bash
$ echo $0
-bash # "-" is the first character. Therefore, this is a login shell

$ echo $0
bash # "-" is NOT the first character. This is NOT a login shell
```

### Invoking a Script

So, you've written a script, say `helloworld` (no extension):

```bash
$ echo "echo hello world" > helloworld
$ cat helloworld
echo hello world
```

How do you call the script from the command line?  There are two ways:

1. Invoke it by `bash helloworld` or `sh helloworld` (`sh` may turn off Bash-specific extensions)
2. make the script itself directly executable with `chmod +x <file>`.  This is the preferred method.

For an easy explanation of modes for `chmod`, see Schotts - _The Linux Command Line_, chapter 9.  A few common ones are:

```bash
chmod 555 helloworld  # read-execute permission for everyone
chmod 755 helloworld  # read-write-ex permission for owner, read-ex for others
chmod 700 helloworld  # only owner
```

Keep in mind that a script **needs read**, as well as execute permission for it to run, since the shell needs to be able to read it.

Here's a function that gets the corresponding code (requires Bash 4+):

```bash
$ filemode () {
>     declare -A modes
>     modes=( ["---"]=0 ["--x"]=1 ["-w-"]=2 ["-wx"]=3 ["r--"]=4 ["r-x"]=5 ["rw-"]=6 ["rwx"]=7 )
>     echo ${modes[$1]}
> }
$ filemode rwx
7
```

Now, call the script:

```bash
$ ./helloworld
hello world
```

Notice the leading dot, indicating the current directory.  Why is this needed?  If `helloworld` is _not_ in `$PATH`, the script will not be found.

As a final step, you can place the script somewhere in `$PATH`.  One common location for "user-only" scripts is `~/bin/`, or `/usr/local/bin/` for scripts to be shared.  Then `export PATH="~/bin/:$PATH"` in your `.bash_profile`.  The script could then be invoked by simply typing `scriptname [ENTER]` from the command line.

#### What File Extension Do I Use? (`.sh`, `.bash`)

The short answer is that you don't technically need either.  The naming of the script is for "aesthetic purposes" and has nothing to do with how it's run.

From [Advanced Bash-Scripting Guide](https://linux.die.net/abs-guide/why-shell.html):

> By convention, user-written shell scripts that are Bourne shell compliant generally take a name with a `.sh`extension.

The more important distinction is which is used in the shebang line.  `#!/bin/sh` is not be the same as `#!/bin/bash`.

## Builtins

### `mkdir`

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

### `cd`

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

### `rmdir` & `rm`

If you try to do `rmdir` on Mac OSX and it refuses to remove the directory even though you are positive it's empty, then there is likely a hidden file contained there such as _.DS_Store_. In that case, type `rm -rf <dir>` instead (where `<dir>` is directory name).

| Syntax | Use |
| ------ | --- |
| `rm <fileName> ..` | delete file(s) |
| `rm -i <fileName> ..` | ask for confirmation for each file |
| `rm -f <fileName>` | force deletion of file |
| `rm -r <foldername>/` | delete folder |

### `touch`

Use touch to create blank files.  Make sure to specify the extension.

```bash
$ touch testfile.txt
```

Note that if the specified file already exists, the file itself will not be modified, but its last-modified-timestamp will be updated to "now."

### The Directory Stack: `dir`, `pushd` & `popd`

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
$ dirs -p  # p: one entry per line
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
$ pushd Scripts/python/
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

### `cp`

The first argument is the file to copy.  The second is its destination, which may be **either a file (essentially copy + rename) or a directory**.

```bash
$ cp
usage: cp [-R [-H | -L | -P]] [-fi | -n] [-apvXc] source_file target_file
       cp [-R [-H | -L | -P]] [-fi | -n] [-apvXc] source_file ... target_directory
```

```bash
$ mkdir mult && cd mult
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

### `mv`

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


### Page Through a File (`less`, `more`)

`less` and `more` are similar commands, but do have [slight differences](https://unix.stackexchange.com/questions/81129/what-are-the-differences-between-most-more-and-less). `more` will display the file without hiding your command history; `less` will hide your command history until you press `q`.

- 'less' is a program similar to 'more', but which allows backward movement in the file as well as forward movement.
- less does not have to read the entire input file before starting, so with large input files it starts up faster than text editors like Vim.

```bash
$ less test.txt
```

To get out of `less` just type `q` (as in quit).

### `cat`

While `less` lets you page through a file, `cat` prints the entire file to STDOUT.

```bash
$ cat test.txt
This is the first line

And this is the third.
```

### `grep`

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

### `exit`

Using `exit` is the right and proper method of "exiting" from a script.

- `exit [n]` exits the shell with a status of `n`.
- If `n` is omitted, the exit status is that of the last command executed.
- 0 is the only "okay" return code; all others indicate errors of some type.
- When executed, the exit status of a function is the exit status of the last command executed in the body.
- `$?` is a special Bash variable that’s set to the exit code of each command after it runs.
- tldp.org: [Reserved Exit Codes](http://tldp.org/LDP/abs/html/exitcodes.html#EXITCODESREF)

### Finding Things: `find` & `locate`

- `locate`: "find filenames quickly."  Searches a database for all pathnames which match the specified pattern.
- `find`: recursively walks a file hierarchy.

#### `locate`

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
$ locate -S

Database: /var/db/locate.database
Compression: Front: 14.03%, Bigram: 59.84%, Total: 10.01%
Filenames: 1148539, Characters: 120204898, Database size: 12028142
Bigram characters: 4830994, Integers: 73081, 8-Bit characters: 164
```

To update the database, use `/usr/libexec/locate.updatedb`.  This is run regularly under the hood.

#### `find`

`find` is for "finding files the hard way," recursively searching a directory based on a variety of attributes.

Syntax: you provide `find` one or more paths and an optional expression.

```bash
find [-H | -L | -P] [-EXdsx] [-f path] path ... [expression]
```

The simplest case of `find` is to pass `.` as the path, which recursively lists the subcontents with your current directory as root:

```bash
$ find .
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
$ find . -type f
./file2.txt
./file.txt
./helloworld
./template.sh
./messages
./hello_world
./msg

# Find only 2-level nested .txt files
$ find . -type f -name "*.txt" -mindepth 2
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

### `clear`

In Sublime Text, there is a feature "Scroll Past End" that allows you to scroll the area of code you’re editing to the center of the window, even if it’s at the end of the file.

There is no direct equivalent functionality in terminal, but we can use `clear`, which clears the terminal screen and gets us a "blank page."

### `alias`

In your `~/.bash_profile`, you can create a custom shortcut called an `alias`.  Add a line like this to `~/.bash_profile`:

```bash
alias la='ls -A'
```

Now, whenever you type `la`, the Terminal will run `ls` with the `-a` modifier, which includes hidden files.

## Other Topics

TODO: these should be put elsewhere, maybe in something Linux or OSX specific.

### Users & Superusers (`sudo`, `su`, `sudoers`)

`sudo` stands for "superuser do."

If you have a lot of root-type work to do in a session, type `sudo -s` to create a new superuser shell, and work from there.

The default security policy is `sudoers`, which is configured via the file `/private/etc/sudoers`.  This defines specific commands that particular users are permitted to execute under an assumed identity.

The security policy determines what privileges, if any, a user has to run `sudo`.  The policy may require that users authenticate themselves with a password or another authentication mechanism.

TODO: more here (nobody, root, daemon users?)

Let's say you try to get a glimpse of the file `/private/etc/sudoers`:

```bash
$ head /private/etc/sudoers
head: /private/etc/sudoers: Permission denied
```

Why is permission denied?

```bash
$ ls -l /private/etc/sudoers
-r--r-----  1 root  wheel  1563 Dec 10  2016 /private/etc/sudoers
```

The file is owned by `root`, (and you are not `root`), while "world"/global permission are "---".

In this case, you will need `sudo` (where `!!` is the last command run, `head /private/etc/sudoers`):

```bash
$ head /private/etc/sudoers
head: /private/etc/sudoers: Permission denied
$ sudo !!
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
$ sudo -i
Password:
Bradleys-MacBook-Pro:~ root# whoami
root
Bradleys-MacBook-Pro:~ root# pwd
/var/root
```

The trailing `#` indicates the current user has superuser privleges.  When finished, use `exit` to return to the regular shell.

### Getting Help

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

### Keyboard Shortcuts

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

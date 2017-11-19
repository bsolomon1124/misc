# Contents

# Resources & references
- [Linux Bash Shell Cheat Sheet](https://learncodethehardway.org/unix/bash_cheat_sheet.pdf)
- GNU: [Bash Reference Manual](https://www.gnu.org/software/bash/manual/bashref.html); some useful sections:
    - [Built-in commands](https://www.gnu.org/software/bash/manual/bashref.html#Shell-Builtin-Commands)
    - [Shell Variables](https://www.gnu.org/software/bash/manual/bashref.html#Shell-Variables)
    - [Command-line editing](https://www.gnu.org/software/bash/manual/bashref.html#Command-Line-Editing)
- Jim Hoskins: [Introduction to the Mac OS X Command Line](http://blog.teamtreehouse.com/introduction-to-the-mac-os-x-command-line) [Sep 2012]
- _Learn Python the Hard Way_: [Command Line Crash Course](https://learnpythonthehardway.org/book/appendixa.html)
- techonthenet tutorials: [Unix](https://www.techonthenet.com/unix/index.php)

# Overview

# Terminology
- The **console** is the system as a whole. This is both the command line as well as the output from previous commands.
- A **shell** is a special **command-line tool (interface)** and _interpreter_ that is designed specifically to provide text-based **interactive control over other command-line tools.**  It uses alphanumeric characters typed on a keyboard to provide instructions and data to the operating system, interactively.  From the Bash docs:

> At its base, a shell is simply a macro processor that executes commands. The term macro processor means functionality where text and symbols are expanded to create larger expressions. ... A Unix shell is both a command interpreter and a programming language.

- You **run Terminal to get acces to a shell prompt.**  The Terminal is an _emulator_.
- The standard OS X shell is **bash**.  Bash is a Unix shell and command language **interpreter** first released in 1989.  In addition to running in a text window, Bash can also read and execute commands from a file, called a script.
- **Home** folder/directory: In Finder, choose Go > Home (shortcut: _Shift+Cmd+H_).  The Home folder is identified by an icon that looks like a house.
- The **Terminal** is a text input/output application (_Applications > Utilities > Terminal_) that lets you interact with a **command-line environment.**  You could also interact with an environment using a remote connection method such as **secure shell (SSH)**.  A terminal window provides access to the input and output of a **shell process.**
- You run **command-line tools** (or just _commands_; one example would be `cd`) that OS X provides by _typing the name of the tool_.
    - Most tools can also take a number of **flags** aka **switches**.  `-l` would be one such flag.  Flags **change behavior.**
    - Flags can be used together after one hyphen.  For example, `-l` and `-a` are both flags to `ls`.  You can use `ls -la` to (1) display detailed info for each entry and (2) list all directory contents, including hidden files/folders.
    - Separately, some tools take **arguments**.  For example, in `ls /Users/brad/temp`, the second chunk is an argument.
- The shell (no matter the command, really) also has a notion of a **current working directory**. _When you specify a filename or path that does not start with a slash, that path is assumed to be relative to this directory._
- The **prompt** is the beginning of the command line. It usually provides some contextual information like who you are, where you are and other useful info. It typically ends in a "$".

# Environment variables
**Environment variables** are variables inherited by all programs executed in the shell’s context. The shell itself uses environment variables to store information such as the name of the current user, the name of the host computer, and the paths to any executable programs.

`export` is used to create and view environment variables.  Use `export -p` to view a list of all names exported in the current shell:

```bash
Bradleys-MacBook-Pro:~ brad$ export -p
declare -x HOME="/Users/brad"
declare -x LANG="en_US.UTF-8"
declare -x LOGNAME="brad"
declare -x OLDPWD
declare -x PATH="/Applications/anaconda3/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin"
declare -x PWD="/Users/brad"
declare -x SHELL="/bin/bash"
# ...
```

One important environment variable is `PATH`.  Command line tools are located in specific directories, and the shell searches `PATH` for them when you run a command.  `PATH` contains a **colon-delimited list of paths** to search-- `/usr/bin:/bin:/usr/sbin:/sbin`, for example.

In the Anaconda installation, when you select "Add Anaconda to PATH," this allows you to run anything in the contents of _/Applications/anaconda3/bin_ from the command line.  (IPython, for example.)

# The home directory
Your home directory (`$HOME`) might not be the same as your _root_ directory.  To see your home directory, use

```bash
Bradleys-MacBook-Pro:Utilities brad$ cd $HOME
Bradleys-MacBook-Pro:~ brad$ pwd
/Users/brad
```

In the example above, `brad` is actually 2 levels below the _top-level_ (root) of your hard drive:

```bash
Bradleys-MacBook-Pro:~ brad$ cd ../..  # Move 2 levels up
Bradleys-MacBook-Pro:/ brad$ pwd
/
```

```
Macintosh HD
|-- Applications
    |-- Utilities
        |-- Terminal.app
|-- Library
|-- System
|-- Users
    |-- brad
```

# Special path characters
The shell supports a number of directory names that have a special meaning:

| Path string | Description |
| ----------- | ----------- |
| `.` | points to the current working directory | For example, if you type `./mytool` and press return, you are running the `mytool` command in the current directory.
| `..` | points to the parent directory (up 1 level) | The path `../Test` is a file or directory (named "Test") that is a **sibling of** the current directory. |
| `~` or `$HOME` | At the beginning of a path, the tilde character represents the home directory of the current user. | `$HOME` is the same thing (usually); technically, it is an environment variable that can be manipulated. |

An example of `cd`ing to a sibling directory:

```bash
Bradleys-MacBook-Pro:~ brad$ pwd
/Users/brad
Bradleys-MacBook-Pro:~ brad$ ls
Applications    Downloads   Movies      Public      temp
Desktop     Dropbox     Music       ds      testfile.txt
Documents   Library     Pictures    rodeo.log
Bradleys-MacBook-Pro:~ brad$ cd Documents
Bradleys-MacBook-Pro:Documents brad$ cd ../Pictures
Bradleys-MacBook-Pro:Pictures brad$ pwd
/Users/brad/Pictures
```

An example using a path with a tilde:

```bash
Bradleys-MacBook-Pro:~ brad$ pwd
/Users/brad
Bradleys-MacBook-Pro:~ brad$ cd Downloads
Bradleys-MacBook-Pro:Downloads brad$ cd ~/Documents  # ~ is alias for /Users/brad
Bradleys-MacBook-Pro:Documents brad$ pwd
/Users/brad/Documents
```

# Running an application
There are two ways to run an application (.app) from the command line.  (Example: current directory is `/Applications`.)
1. Use `open`: `Bradleys-MacBook-Pro:Applications brad$ open BitTorrent.app`
2. Specify the pathname of the executable file inside the package.  This may be confusing because of the hidden nature of the directory: in the GUI, you simply see `application.app`.  But underneath, there is a path to an executable file:

```bash
Bradleys-MacBook-Pro:Applications brad$ ls BitTorrent.app/Contents
Frameworks  Info.plist  Library     MacOS       PkgInfo     Resources   _CodeSignature
Bradleys-MacBook-Pro:Applications brad$ BitTorrent.app/Contents/MacOS/BitTorrent
```

# Commands

| Command | Usage |
| ------- | ----- |
| open | open a file | uses default application
| pwd | print working directory
| hostname | my computer's network name
| mkdir | create a new directory (folder)
| cd | change directory | `cd ~` is the same as `cd $HOME`.  You need a space following `cd`.
| ls | list directory
| rmdir | remove directory | only removes an _empty_ directory by default
| rm | remove file or files | You can use pattern matching characters (such as the asterisk) to match more than one file. You can also remove directories with this command, although use of `rmdir` is preferred.
| pushd | push directory
| popd | pop directory
| cp | copy a file or directory
| mv | move a file or directory (or rename them) | Moves files and directories from one place to another. You also use this command to rename files and directories.
| less | page through a file
| cat | print the whole file
| xargs | execute arguments
| find | find files
| grep | find things inside files
| man | read a manual page
| apropos | find what man page is appropriate
| env | look at your environment
| echo | print (output) some arguments to STDOUT
| export | export/set a new environment variable
| exit | exit the shell
| sudo | authenticate yourself as a superuser to gain extra privileges.  DANGER! be careful
| dirs | display the list of currently remembered directories
| touch | make a new file
| open | open file(s)
| defaults | interface to user's defaults
| chmod | changes the access mode of one file or multiple files
| chown | ?
| vi | launch the text editor vi

Now, for some more on specific commands

## `mkdir`
Say you first make a single directory and then want to make a directory one level down without `cd`ing.  You'll need to specify the "full relative path".  If you want to make subdirectories multiple levels down, you'll need `-p`:

```bash
Bradleys-MacBook-Pro:~ brad$ pwd
/Users/brad

Bradleys-MacBook-Pro:~ brad$ mkdir temp

Bradleys-MacBook-Pro:~ brad$ mkdir temp/stuff

Bradleys-MacBook-Pro:~ brad$ mkdir temp/stuff/things/files  # this will fail: +1 levels down

Bradleys-MacBook-Pro:~ brad$ mkdir -p temp/stuff/things/files  # need -p in this case
```

To make a directory with a space in its name, use quotes:

```bash
Bradleys-MacBook-Pro:~ brad$ mkdir 'new folder1'
Bradleys-MacBook-Pro:~ brad$ mkdir "new folder2"
```

Or, backslash escape the space literal:

```bash
Bradleys-MacBook-Pro:~ brad$ mkdir new\ folder1
```


If you `mkdir` a directory that already exists, you'll get an error:

```bash
Bradleys-MacBook-Pro:~ brad$ mkdir temp
Bradleys-MacBook-Pro:~ brad$ mkdir temp
mkdir: temp: File exists
```

You can't specify _files_ this way.  Using `mkdir file.txt` creates a folder called "file.txt" rather than a text file.  For this you'll need the [`touch`](#touch) command.

## `cd`

```bash
Bradleys-MacBook-Pro:~ brad$ mkdir -p dir1/dir2/dir3/dir4
Bradleys-MacBook-Pro:~ brad$ pwd
/Users/brad
Bradleys-MacBook-Pro:~ brad$ cd dir1/dir2/dir3
Bradleys-MacBook-Pro:dir3 brad$ pwd
/Users/brad/dir1/dir2/dir3
Bradleys-MacBook-Pro:dir3 brad$ cd ..
Bradleys-MacBook-Pro:dir2 brad$ pwd
/Users/brad/dir1/dir2
Bradleys-MacBook-Pro:dir2 brad$ cd ..; pwd  # one folder up
/Users/brad/dir1
Bradleys-MacBook-Pro:dir1 brad$ cd ../..; pwd  # two folders up
/Users
```

You can put quotes around any file/folder in any command:

```bash
cd "long folder name"
```

To get to your root:

```bash
Bradleys-MacBook-Pro:/ brad$ cd /; pwd
/
```

## `rmdir`
If you try to do rmdir on Mac OSX and it refuses to remove the directory even though you are positive it's empty, then there is actually a file in there called _.DS_Store_. In that case, type `rm -rf <dir>` instead (replace `<dir>` with the directory name).

## `touch`
```bash
Bradleys-MacBook-Pro:temp brad$ touch testfile.txt
```

## `pushd` and `popd`
TODO: not fulling understanding these 2...

Read these as "push directory" and "pop directory."  These commands let you **temporarily go to a different directory and then come back, easily switching between the two.**

- The `pushd` command takes your current directory and "pushes" it into a list for later, then it changes to another directory. It's like saying, "Save where I am, then go here."
    - `pushd`, if you run it by itself with no arguments, will switch between your current directory and the last one you pushed. It's an easy way to switch between two directories.
- The `popd` command takes the last directory you pushed and "pops" it off, taking you back there.
- You can think of the output of both as a stack.

```bash
Bradleys-MacBook-Pro:~ brad$ pwd
/Users/brad
Bradleys-MacBook-Pro:~ brad$ mkdir -p temp/dir1/dir2/dir3
Bradleys-MacBook-Pro:dir2 brad$ pwd
/Users/brad/temp/dir1/dir2
Bradleys-MacBook-Pro:dir2 brad$ pushd ~  # Store current directory, and go $HOME
~ ~/temp/dir1/dir2
Bradleys-MacBook-Pro:~ brad$ pwd
/Users/brad
Bradleys-MacBook-Pro:~ brad$ pushd  # pushed with no args - switch to last dir you pushd
~/temp/dir1/dir2 ~
Bradleys-MacBook-Pro:dir2 brad$ pushd ../..
~/temp ~/temp/dir1/dir2 ~/temp/dir1/dir2 ~  # TODO: not following here
Bradleys-MacBook-Pro:temp brad$ popd
~/temp/dir1/dir2 ~/temp/dir1/dir2 ~
Bradleys-MacBook-Pro:dir2 brad$ popd
~/temp/dir1/dir2 ~
Bradleys-MacBook-Pro:dir2 brad$ popd
~
```

## `cp`
The first argument is the file to copy.  The second is its destination, which may be either a file (essentially copy + rename) or a directory.

```bash
Bradleys-MacBook-Pro:~ brad$ cp
usage: cp [-R [-H | -L | -P]] [-fi | -n] [-apvXc] source_file target_file
       cp [-R [-H | -L | -P]] [-fi | -n] [-apvXc] source_file ... target_directory
```

```bash
Bradleys-MacBook-Pro:~ brad$ touch file.txt
Bradleys-MacBook-Pro:~ brad$ cp file.txt file2.txt  # As new file
Bradleys-MacBook-Pro:~ brad$ ls
file.txt     file2.txt
```

```bash
Bradleys-MacBook-Pro:~ brad$ cp file.txt temp  # To directory
```

Note that putting a `/` (slash) at the end of a directory checks that the file is really a directory, so if the directory doesn't exist, you'll get an error.

To copy directories rather than files, use the `-r` flag:

```bash
Bradleys-MacBook-Pro:~ brad$ cp -r temp temp2
```

**`cp` will overwrite files that already exist**, so be careful copying files around.

## `mv`
The syntax to move is similar to that of copy:

```bash
Bradleys-MacBook-Pro:~ brad$ mv
usage: mv [-f | -i | -n] [-v] source target
       mv [-f | -i | -n] [-v] source ... directory
```

```bash
Bradleys-MacBook-Pro:temp brad$ pwd; ls
/Users/brad/temp
file2.txt
Bradleys-MacBook-Pro:temp brad$ mkdir subtemp; mv file2.txt subtemp
Bradleys-MacBook-Pro:temp brad$ ls
subtemp
Bradleys-MacBook-Pro:temp brad$ ls subtemp
file2.txt
```

When you use two files, the operation becomes _renaming_:

```bash
Bradleys-MacBook-Pro:~ brad$ touch temp/file1.txt
Bradleys-MacBook-Pro:~ brad$ ls temp
file1.txt
Bradleys-MacBook-Pro:~ brad$ cd temp
Bradleys-MacBook-Pro:temp brad$ mv file1.txt file2.txt
Bradleys-MacBook-Pro:temp brad$ ls
file2.txt
```

## View (page through) a file (`less`, `more`)
`less` and `more` are similar commands, but do have [slight differences](https://unix.stackexchange.com/questions/81129/what-are-the-differences-between-most-more-and-less).  `more` will display the file without hiding your command history; `less` will hide your command history until you press `q`.

```bash
Bradleys-MacBook-Pro:~ brad$ less test.txt
```

To get out of `less` just type `q` (as in quit).

## `cat`
While `less` lets you page through a file, `cat` prints the entire file to STDOUT.

```bash
Bradleys-MacBook-Pro:~ brad$ cat test.txt
This is the first line.first

And this is the third.
```

# Other hacks

## Show hidden files
By default, the Finder in OS X hides some files away from view (mostly irrelevant ones) but if you want to see everything on your computer, then use:

```bash
defaults write com.apple.finder AppleShowAllFiles TRUE
```
## Change frequency with which App Store checks for updates
The integer is the day-frequency of update-checking.

```bash
defaults write com.apple.SoftwareUpdate ScheduleFrequency -int 1
```

## Forcing Mac not to sleep
Sometimes, you don’t want your computer to fall asleep automatically. You can "caffeinate" your Mac so that it doesn’t fall asleep until you say so:

```bash
Bradleys-MacBook-Pro:~ brad$ caffeinate
```

You can give your Mac a break once it is done by hitting `Control+C` in the Terminal or quitting Terminal altogether. Yes, this command only continues to work as long as Terminal stays open.

Perhaps you need your computer to stay awake for a few hours but want it to go to sleep after a set time when the task it needs to finish completes. It’s easy. All you have to do is enter the following command:

```bash
Bradleys-MacBook-Pro:~ brad$ caffeinate -i -t 3600
```

The number at the end represents the number of seconds. So, 3600 = 1 hour.

# Getting help
Simply typing `help` gets you a non-exhaustive list of commands and their options.

You can type `help name` to find out more about the function `name`.

```bash
Bradleys-MacBook-Pro:~ brad$ help pwd
pwd: pwd [-LP]
    Print the current working directory.  With the -P option, pwd prints
    the physical directory, without any symbolic links; the -L option
    makes pwd follow symbolic links.
```

Note that only the commands listed under `help` are available through `help name`.  Some, like `help ls`, will throw an error because they aren't present in the list.  `help` gets you acccess to **built-in** shell commands.

Another form of documentation is man pages (short for manual).  This directory is more extensive than `help`.  To access a man page, type the `man` command followed by the name of the thing you want to look up.  The link to the full OS X Man Pages is [here](https://developer.apple.com/legacy/library/documentation/Darwin/Reference/ManPages/).  To exit, press "q."

# Other
Bash scripts often begin with `#! /bin/bash` (assuming that Bash has been installed in /bin), since this ensures that Bash will be used to interpret the script, even if it is executed under another shell.

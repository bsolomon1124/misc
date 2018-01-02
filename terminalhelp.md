# Contents
- [Terminology](#terminology)
- [Environment variables](#environment-variables)
- [The home directory](#the-home-directory)
- [Special path characters](#special-path-characters)
- [Running an application](#running-an-application)
- [Commands](#commands)
    - [`mkdir`](#mkdir)
    - [`cd`](#cd)
    - [`rmdir` & `rm`](#rmdir--rm)
    - [`touch`](#touch)
    - [`pushd` & `popd`](#pushd-and-popd)
    - [`cp`](#cp)
    - [`mv`](#mv)
    - [`less` & `more`](#view-page-through-a-file-less-more)
    - [`cat`](#cat)
    - [`grep`](#grep)
    - [`find`](#find)
- [Chaining commands](#chaining-commands)
- [Other hacks](#other-hacks)
    - [`clear`](#clear)
    - [Show hidden files](#show-hidden-files)
    - [App update frequency](#change-frequency-with-which-app-store-checks-for-updates)
    - [Downloading files](#downloading-files)
    - [Zipping & unzipping](#zipping--unzipping)
    - [Dragging files to Terminal](#dragging-files-to-terminal)
    - [Brackets for batch operations](#brackets-for-batch-operations)
    - [Process information](#process-information)
    - [Making your own shorthand](#making-your-own-shorthand)
    - [Word count](#word-count)
- [Getting help](#getting-help)
- [Keyboard shortcuts](#keyboard-shortcuts)
- [Other](#other)

# Resources & references
- [Linux Bash Shell Cheat Sheet](https://learncodethehardway.org/unix/bash_cheat_sheet.pdf)
- GNU: official [Bash Reference Manual](https://www.gnu.org/software/bash/manual/bashref.html); some useful sections:
    - [Built-in commands](https://www.gnu.org/software/bash/manual/bashref.html#Shell-Builtin-Commands)
    - [Shell Variables](https://www.gnu.org/software/bash/manual/bashref.html#Shell-Variables)
    - [Command-line editing](https://www.gnu.org/software/bash/manual/bashref.html#Command-Line-Editing)
- Jim Hoskins: [Introduction to the Mac OS X Command Line](http://blog.teamtreehouse.com/introduction-to-the-mac-os-x-command-line) [Sep 2012]
- _Learn Python the Hard Way_: [Command Line Crash Course](https://learnpythonthehardway.org/book/appendixa.html)
- techonthenet tutorials: [Unix](https://www.techonthenet.com/unix/index.php)

# Terminology
- The **console** is the system as a whole. This is both the command line as well as the output from previous commands.
- A **shell** is a special **command-line tool (interface)** and _interpreter_ that is designed specifically to provide text-based **interactive control over other command-line tools.**  It uses alphanumeric characters typed on a keyboard to provide instructions and data to the operating system, interactively.  From the Bash docs:

> At its base, a shell is simply a macro processor that executes commands. The term macro processor means functionality where text and symbols are expanded to create larger expressions. ... A Unix shell is both a command interpreter and a programming language.

- You **run Terminal to get acces to a shell prompt.**  The Terminal is an _emulator_ and a text input/output application (_Applications > Utilities > Terminal_) that lets you interact with a **command-line environment.**  You could also interact with an environment using a remote connection method such as **secure shell (SSH)**.  A terminal window provides access to the input and output of a **shell process.**
- The standard OS X shell is **bash**.  Bash is a Unix shell and command language **interpreter** first released in 1989.  In addition to running in a text window, Bash can also read and execute commands from a file, called a script.
- You run **command-line tools** (or just _commands_; one example would be `cd`) that OS X provides by _typing the name of the tool_.
    - Most tools can also take a number of **flags** aka **switches**.  `-l` would be one such flag.  Flags **change behavior.**
    - Flags can be used together after one hyphen.  For example, `-l` and `-a` are both flags to `ls`.  You can use `ls -la` to (1) display detailed info for each entry and (2) list all directory contents, including hidden files/folders.
    - Separately, some tools take **arguments**.  For example, in `ls /Users/brad/temp`, the second chunk is an argument.
- The shell (no matter the command, really) also has a notion of a **current working directory**. _When you specify a filename or path that does not start with a slash, that path is assumed to be relative to this directory._
- The **prompt** is the beginning of the command line. It usually provides some contextual information like who you are, where you are and other useful info. It typically ends in a "$".

# Environment variables
**Environment variables** are variables inherited by all programs executed in the shell’s context. The shell itself uses environment variables to store information such as the name of the current user, the name of the host computer, and the paths to any executable programs.

`export` is used to create and view environment variables.  Use `export -p` or just `env`to view a list of all names exported in the current shell:

```bash
~ $ env
TERM_PROGRAM=Apple_Terminal
SHELL=/bin/bash
TERM=xterm-256color
TERM_PROGRAM_VERSION=400
USER=brad
PATH=/Applications/anaconda3/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:/usr/local/go/bin
PWD=/Users/brad
LANG=en_US.UTF-8
XPC_FLAGS=0x0
XPC_SERVICE_NAME=0
SHLVL=1
HOME=/Users/brad
LOGNAME=brad
GOPATH=/Users/brad/Scripts/go
_=/usr/bin/env
# ...
```

One important environment variable is `PATH`.  Command line tools are located in specific directories, and the shell searches `PATH` for them when you run a command.  `PATH` contains a **colon-delimited list of paths** to search-- `/usr/bin:/bin:/usr/sbin:/sbin`, for example.

In the Anaconda installation, when you select "Add Anaconda to PATH," this allows you to run anything in the contents of _/Applications/anaconda3/bin_ from the command line.  (IPython, for example.)  The installation adds this to your `~/.bash_profile`:

```bash
# added by Anaconda3 5.0.0 installer
export PATH="/Applications/anaconda3/bin:$PATH"
```

# The home directory

- **Home** folder/directory: In Finder, choose Go > Home (shortcut: _Shift+Cmd+H_).  The Home folder is identified by an icon that looks like a house.

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
```

```
Macintosh               # root
|-- Applications
    |-- Utilities
        |-- Terminal.app
|-- Library
|-- System
|-- Users
    |-- brad            # home
```

In Python, `os` doesn't accept the tilde (~) character.  Expand it with `os.path.expanduser`:

> On Unix, an initial ~ is replaced by the environment variable HOME if it is set; otherwise the current user’s home directory is looked up in the password directory through the built-in module pwd.

I.e.:

```python
>>> import os
>>> home = os.path.expanduser('~')
>>> print(home)
/Users/brad
```

# Special path characters
In addition to `~`, the shell supports a number of directory names that have a special meaning:

| Path string | Description |
| ----------- | ----------- |
| `.` | points to the current working directory | For example, if you type `./mytool` and press return, you are running the `mytool` command in the current directory.
| `..` | points to the parent directory (up 1 level) | The path `../Test` is a file or directory (named "Test") that is a **sibling of** the current directory. |
| `~` or `$HOME` | At the beginning of a path, the tilde character represents the home directory of the current user. | `$HOME` is the same thing (usually); technically, it is an environment variable that can be manipulated. |

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

# Running an application
There are two ways to run an application (.app) from the command line.  (Example: current directory is `/Applications`.)
1. Use `open`: `$ open BitTorrent.app`
2. Specify the pathname of the executable file inside the package.  This may be confusing because of the hidden nature of the directory: in the GUI, you simply see `application.app`.  But underneath, there is a path to an executable file:

```bash
$ ls BitTorrent.app/Contents
Frameworks  Info.plist  Library     MacOS       PkgInfo     Resources   _CodeSignature
$ BitTorrent.app/Contents/MacOS/BitTorrent
```

# Commands

| Command | Usage | Note
| ------- | ----- | ----
| open | open a file | uses default application
| pwd | print working directory
| hostname | my computer's network name
| mkdir | create a new directory (folder)
| cd | change directory |
| ls | list directory
| rmdir | remove directory | only removes an _empty_ directory by default
| rm | remove file or files | You can use pattern matching characters (such as the asterisk) to match more than one file. You can also remove directories with this command, although use of `rmdir` is preferred.  Note that this is a true delete, rather than sending to trash.
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
| sudo | authenticate yourself as a sudo (super) user to gain extra privileges.  *DANGER!* | may be necessary if you are modifying core pieces of the filesystem or installing packages
| dirs | display the list of currently remembered directories
| touch | make a new file
| open | open file(s)
| defaults | interface to user's defaults
| chmod | changes permissions of a file or folder
| chown | changes ownership of a file or folder
| vi | launch the text editor vi
| history | display the history list with line numbers
| head | display first lines of a file | `head -n <num_lines> <filename>` or `head <filename>`; default 10 |

Now, for some more on specific commands.

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

## `rmdir` & `rm`
If you try to do `rmdir` on Mac OSX and it refuses to remove the directory even though you are positive it's empty, then there is likely a hidden file contained there such as _.DS_Store_. In that case, type `rm -rf <dir>` instead (replace `<dir>` with the directory name).

| Syntax | Use |
| ------ | --- |
| `rm <fileName> ..` | delete file(s) |
| `rm -i <fileName> ..` | ask for confirmation for each file |
| `rm -f <fileName>` | force deletion of file |
| `rm -r <foldername>/` | delete folder |

## `touch`
```bash
Bradleys-MacBook-Pro:temp brad$ touch testfile.txt
```

Note that if the specified file already exists, the file itself will not be modified, but its last-modified-timestamp will be updated to "now."

## `pushd` and `popd`
TODO: not fulling understanding these 2...

Read these as "push directory" and "pop directory."  These commands let you **temporarily go to a different directory and then come back, easily switching between the two.**

- The `pushd` command takes your current directory and "pushes" it into a list for later, then it changes to another directory. It's like saying, "Save where I am, then go here."
    - `pushd`, if you run it by itself with no arguments, will switch between your current directory and the last one you pushed. It's an easy way to switch between two directories.
- The `popd` command takes the last directory you pushed and "pops" it off, taking you back there.
- You can think of the output of both as a stack.

```bash
$ pwd
/Users/brad
$ mkdir -p temp/dir1/dir2/dir3
Bradleys-MacBook-Pro:dir2 brad$ pwd
/Users/brad/temp/dir1/dir2
Bradleys-MacBook-Pro:dir2 brad$ pushd ~  # Store current directory, and go $HOME
~ ~/temp/dir1/dir2
$ pwd
/Users/brad
$ pushd  # pushed with no args - switch to last dir you pushd
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
The first argument is the file to copy.  The second is its destination, which may be **either a file (essentially copy + rename) or a directory**.

```bash
$ cp
usage: cp [-R [-H | -L | -P]] [-fi | -n] [-apvXc] source_file target_file
       cp [-R [-H | -L | -P]] [-fi | -n] [-apvXc] source_file ... target_directory
```

```bash
$ touch file.txt
$ cp file.txt file2.txt  # As new file
$ cp file.txt Downloads/file3.txt  # As new file within direc
$ ls
file.txt     file2.txt
```

```bash
$ cp file.txt temp  # To directory
```

Note that putting a `/` (slash) at the end of a directory checks that the file is really a directory, so if the directory doesn't exist, you'll get an error.

To copy directories rather than files, use the `-r` flag:

```bash
$ cp -r temp temp2
```

**`cp` will overwrite files that already exist**, so be careful copying files around.

To summarize:

| Syntax | Use |
| ------ | --- |
| `cp image.jpg newimage.jpg` | rename _image.jpg_ to _newimage.jpg_ |
| `cp image.jpg <folderName>/` | copy _image.jpg_ to _folderName/_ directory |
| `cp image.jpg folder/sameImageNewName.jpg`| copy _image.jpg_ to _folderName/_ directory and rename it |
| `cp -R stuff otherStuff` | rename a folder |
| `cp *.txt stuff/` | copy all of the specified file type to folder |

## `mv`
The syntax to move is similar to that of copy:

```bash
$ mv
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
$ touch temp/file1.txt
$ ls temp
file1.txt
$ cd temp
Bradleys-MacBook-Pro:temp brad$ mv file1.txt file2.txt
Bradleys-MacBook-Pro:temp brad$ ls
file2.txt
```

That is, `mv` with two file arguments is a means of renaming by moving.

To summarize:


| Syntax | Use |
| ------ | --- |
| `mv file.txt Documents/` | move file to a folder |
| `mv <folderName> <folderName2>` | move folder to (within) other folder |
| `mv filename.txt filename2.txt` | rename file |
| `mv <fileName> stuff/newfileName` | move file to folder and give it a new name |
| `mv <folderName>/ ..` | move folder up in hierarchy |


## View (page through) a file (`less`, `more`)
`less` and `more` are similar commands, but do have [slight differences](https://unix.stackexchange.com/questions/81129/what-are-the-differences-between-most-more-and-less). `more` will display the file without hiding your command history; `less` will hide your command history until you press `q`.

- 'less' is a program similar to 'more', but which allows backward movement in the file as well as forward movement.
- less does not have to read the entire input file before starting, so with large input files it starts up faster than text editors like vi.

```bash
$ less test.txt
```

To get out of `less` just type `q` (as in quit).

## `cat`
While `less` lets you page through a file, `cat` prints the entire file to STDOUT.

```bash
$ cat test.txt
This is the first line.first

And this is the third.
```

## `grep`
The following pipes to commands together.  `cat` prints the file and `grep` finds all lines with occurences of `ax`.

```bash
Bradleys-MacBook-Pro:adhoc brad$ cat braille.py | grep ax
fig, ax = plt.subplots()
ax.imshow(codes[5], cmap=cmap)
```

We can pipe any output to `grep`:

```bash
Bradleys-MacBook-Pro:adhoc brad$ history | grep conda
   21  /Applications/anaconda3/bin/jupyter-qtconsole ; exit;
   22  /Applications/anaconda3/bin/jupyter-qtconsole ; exit;
   23  /Applications/anaconda3/bin/jupyter-qtconsole ; exit;
   24  /Applications/anaconda3/bin/jupyter-qtconsole ; exit;
# ...
```

## `find`
The following looks for text files in our current directory and its child folders:

```bash
Bradleys-MacBook-Pro:python brad$ find . -name "*txt" -type f
./docs/tutorials/imgs/ex.txt
./_archive/pyfinance/pyfinance.egg-info/SOURCES.txt
./_archive/pyfinance/pyfinance.egg-info/requires.txt
./_archive/pyfinance/pyfinance.egg-info/top_level.txt
# ...
```

Continuing with the above, search those files for the word _neat_:

```bash
Bradleys-MacBook-Pro:python brad$ find . -name "*txt" -type f | xargs grep neat
```

# Chaining commands
Use the pipe operator ("|") at the end of a command to redirect its _output_ to the next command.  Note that this is different than a semicolon which is simply the equivalent of using the commands _separately_ on two different lines.

# Other hacks

## `clear`
In Sublime Text, there is a feature "Scroll Past End" that allows you to scroll the area of code you’re editing to the center of the window, even if it’s at the end of the file.

There is no direct equivalent functionality in terminal, but we can use `clear`, which clears the terminal screen and gets us a "blank page."

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
$ caffeinate
```

You can give your Mac a break once it is done by hitting `Control+C` in the Terminal or quitting Terminal altogether. Yes, this command only continues to work as long as Terminal stays open.

Perhaps you need your computer to stay awake for a few hours but want it to go to sleep after a set time when the task it needs to finish completes. It’s easy. All you have to do is enter the following command:

```bash
$ caffeinate -i -t 3600
```

The number at the end represents the number of seconds. So, 3600 = 1 hour.

## Downloading files
We can use `curl` for this in place of `wget`, which is not available by defualt on all systems.

```bash
# Save the downloaded .zip to Downloads/
$ curl http://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/F-F_Research_Data_Factors_CSV.zip --output Downloads/frenchdata.zip
```

## Zipping & unzipping
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

## Dragging files to terminal
You can drag a file directly to Terminal to add its file path to the command line.

https://www.youtube.com/watch?v=mgazHxDtiu8

## Brackets for batch operations
When you're working with variations of a file—like backups or different file types—it can get tedious typing out the same commands with small tweaks. Using the brace symbols ({}), you can easily perform batch operations on multiple versions of a file.

Say you want to rename just part of a filename. Instead of typing out `mv /path/to/file.txt /path/to/file.xml`, you could just run:

```bash
mv /path/to/file.{txt,xml}
```

The most common example of this is when you're backing up a file that you're making changes to. For example, if you are tweaking your _rc.conf_, you'll want to make a backup in case the new one doesn't work. So, to do so, you can just run:

```bash
sudo cp /etc/rc.conf{,-old}
```

## Process information
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

## Making your own shorthand
In your `~/.bash_profile`, you can create a custom shortcut called an `alias`.  Add a line like this to `~/.bash_profile`:

```bash
alias la='ls -A'
```

Now, whenever you type `la`, the Terminal will run `ls` with the `-a` modifier, which includes hidden files.

## Word count
Use `wc`.  Outputs: word, line, character, and byte count.

## Shorten the prompt

In `~/.bash_profile`, add:

```bash
PS1='\W \$ '
```

to abbreviate your prompt to the working directory + $.

# Getting help
Simply typing `help` gets you a non-exhaustive list of commands and their options.

You can type `help name` to find out more about the function `name`.

```bash
$ help pwd
pwd: pwd [-LP]
    Print the current working directory.  With the -P option, pwd prints
    the physical directory, without any symbolic links; the -L option
    makes pwd follow symbolic links.
```

Note that only the commands listed under `help` are available through `help name`.  Some, like `help ls`, will throw an error because they aren't present in the list.  `help` gets you acccess to **built-in** shell commands.

Another form of documentation is man pages (short for manual).  This directory is more extensive than `help`.  To access a man page, type the `man` command followed by the name of the thing you want to look up: `man <command>`.  The link to the full OS X Man Pages is [here](https://developer.apple.com/legacy/library/documentation/Darwin/Reference/ManPages/).  To exit, press "q."

# Keyboard shortcuts

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

# Other
Bash scripts often begin with `#! /bin/bash` (assuming that Bash has been installed in /bin), since this ensures that Bash will be used to interpret the script, even if it is executed under another shell.

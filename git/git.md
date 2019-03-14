# Contents

- [Contents][0]
- [How This Tutorial is Structured][1]
- [Resources & References][2]
    - [Beginner][3]
    - [Intermediate][4]
    - [Advanced][5]
    - [Interesting Stack Overflow Questions][6]
    - [Software][7]
- [About Git (No Git Commands Here!)][8]
    - [Version Control Systems (VCS)][9]
    - [File States in Git][10]
    - [The Git Object Model][11]
        - [Object Store][12]
    - [Git Index][13]
    - [TODO][14]
    - [Trees][15]
    - [A Golden Rule of Version Control][16]
- [Quick Reference: Commands][17]
- [Local Git][18]
    - [Creating a Repo: `git init`][19]
    - [Staging and Committing (`git status`, `git add`, and `git commit`)][20]
        - [Do I Need `git add`?  What about `git commit -a`?][21]
    - [Tracked versus Staged][22]
    - [Check Specific Differences: `git diff`][23]
    - [Ignore Files: `.gitignore`][24]
    - [Deleted and Moved Files: `git rm` & `git mv`][25]
    - [History: `git log`][26]
    - [Branching (`git branch`, `git checkout`)][27]
    - [Merging (`git merge`)][28]
- [Working with Remotes][29]
    - [Local Versus Remote Repos][30]
    - [URL Structure][31]
    - [SSH Setup][32]
    - [Cloning a Repo: `git clone`][33]
    - [Tracking and Manipulating Remotes: `git remote`][34]
    - [Update Remote Branches: `git fetch`][35]
    - [Interaction: `git push` & `git pull`][36]
        - [Pulling][37]
        - [Pushing][38]
        - [Aside: What is a ref?][39]
        - [Troubleshooting: "Your branch is ahead of 'origin/master'"][40]
- [Interaction with GitHub][41]
    - [Pull Requests][42]
        - [Keep Up with Upstream][43]
    - [Types of Accounts][44]
    - [RESTful API][45]
- [Glossary][46]
- [Other][47]
    - [Undoing Things][48]
        - [Revise a Commit][49]
        - [Unstage a Staged File][50]
        - [Unmodifying a Modified File][51]
    - [`git show`][52]
    - [Git Setup & Configuration][53]
    - [Signing Your Work][54]
    - [Plumbing Commands][55]
    - [Commit Guidelines][56]
    - [GUIs][57]

[0]: #contents
[1]: #how-this-tutorial-is-structured
[2]: #resources--references
[3]: #beginner
[4]: #intermediate
[5]: #advanced
[6]: #interesting-stack-overflow-questions
[7]: #software
[8]: #about-git-no-git-commands-here
[9]: #version-control-systems-vcs
[10]: #file-states-in-git
[11]: #the-git-object-model
[12]: #object-store
[13]: #git-index
[14]: #todo
[15]: #trees
[16]: #a-golden-rule-of-version-control
[17]: #quick-reference-commands
[18]: #local-git
[19]: #creating-a-repo-git-init
[20]: #staging-and-committing-git-status-git-add-and-git-commit
[21]: #do-i-need-git-add--what-about-git-commit--a
[22]: #tracked-versus-staged
[23]: #check-specific-differences-git-diff
[24]: #ignore-files-gitignore
[25]: #deleted-and-moved-files-git-rm--git-mv
[26]: #history-git-log
[27]: #branching-git-branch-git-checkout
[28]: #merging-git-merge
[29]: #working-with-remotes
[30]: #local-versus-remote-repos
[31]: #url-structure
[32]: #ssh-setup
[33]: #cloning-a-repo-git-clone
[34]: #tracking-and-manipulating-remotes-git-remote
[35]: #update-remote-branches-git-fetch
[36]: #interaction-git-push--git-pull
[37]: #pulling
[38]: #pushing
[39]: #aside-what-is-a-ref
[40]: #troubleshooting-your-branch-is-ahead-of-originmaster
[41]: #interaction-with-github
[42]: #pull-requests
[43]: #keep-up-with-upstream
[44]: #types-of-accounts
[45]: #restful-api
[46]: #glossary
[47]: #other
[48]: #undoing-things
[49]: #revise-a-commit
[50]: #unstage-a-staged-file
[51]: #unmodifying-a-modified-file
[52]: #git-show
[53]: #git-setup--configuration
[54]: #signing-your-work
[55]: #plumbing-commands
[56]: #commit-guidelines
[57]: #guis

# How This Tutorial is Structured

Git is an open-source distributed version control system (DVCS).

This tutorial is structured in the vein of [`giteveryday`](https://git-scm.com/docs/giteveryday): it works incrementally and builds up.

1. The first part is all conceptual, with no Git commands.  It talks about VCSs and how Git works.
2. The second part is about "local Git."  It is a subset of Git commands that let you work independently on a project on your local machine.
3. The third part is about working on group projects with Git, often where you are interacting with another server(s).
4. The last few parts are about GitHub specifically, and some odds-and-ends.

# Resources & References

_Ordered by ascending difficulty/assumed familiarity level._

## Beginner

- Metis DS:
    - [Using Git at the Command Line](https://github.com/thisismetis/dsp/blob/master/04-git.md)
    - [Getting Started with Git](https://vimeo.com/178481263?mc_cid=bbf0c1674e&mc_eid=9444b3c479) (video)
        - [List of commands](https://github.com/bsolomon1124/dsp/blob/master/resources/git_video_history.md) used in the above video
- [Git Cheat Sheet](https://services.github.com/on-demand/downloads/github-git-cheat-sheet.pdf)
- Roger Dudler: [git - the simple guide, no deep shit](https://rogerdudler.github.io/git-guide/)
- fournova tutorial: [Learn Version Control with Git](https://www.git-tower.com/learn/git/ebook/en/command-line/introduction)
    - fournova is the maker of Tower, a Git client for Mac & Windows
- CodeSchool: [Got 15 Minutes and Want to Learn Git?](https://try.github.io/levels/1/challenges/1)
- Real Python: [Introduction to Git and GitHub for Python Developers](https://realpython.com/python-git-github-intro/)

## Intermediate

- NumPy: [git resources](https://docs.scipy.org/doc/numpy-1.13.0/dev/gitwash/git_resources.html)
- Git Documentation: [Reference](https://git-scm.com/docs)
    - [`git/Documentation`](https://github.com/git/git/tree/master/Documentation) on GitHub mirror
- Nick Farina: [Git is Simpler Than You Think](http://nfarina.com/post/9868516270/git-is-simpler)
- Tom Preston-Werner: [The Git Parable](http://tom.preston-werner.com/2009/05/19/the-git-parable.html)
- Scott Chacon/Ben Straub - [Pro Git](https://book.git-scm.com/book/en/v2)
- Linux conference: [Git for Ages 4 and Up](https://www.youtube.com/watch?v=1ffBJ4sVUb4)
- [GitHub Help](https://help.github.com/)
- Mark Lodato:
    - [A Visual Git Reference](http://marklodato.github.io/visual-git-guide/index-en.html)
    - [Visualizing Git with D3](http://onlywei.github.io/explain-git-with-d3/#)
- Neo: [Git Immersion Training](http://gitimmersion.com/)
- ["Algorithm" is not a !@%#$@ 4-Letter Word](http://www.jamisbuck.org/presentations/rubyconf2011/index.html), RubyConf 2011 slides by Jamis Buck
- The GitHub [REST API v3](https://developer.github.com/v3/)
- [Learn Git Branching](https://learngitbranching.js.org/)
- [Understanding Git Conceptually](https://www.sbf5.com/~cduan/technical/git/)
- [The Git Parable](http://tom.preston-werner.com/2009/05/19/the-git-parable.html)

## Advanced

- Sam Livingston-Gray: [Think Like (a) Git](http://think-like-a-git.net/epic.html)
    - Video of Sam's [presentation](http://confreaks.tv/videos/cascadiaruby2011-think-like-a-git)
- The Git docs [reference manual](https://git-scm.com/docs)
- Ryan Tomayko: [The Thing About Git](https://tomayko.com/blog/2008/the-thing-about-git)
- Scott Chacon: [Git Internals](https://github.com/pluralsight/git-internals-pdf/releases)
- [Git Source Code Mirror](https://github.com/git/git)
- [Git for Computer Scientists](http://eagain.net/articles/git-for-computer-scientists/) (Git Internals / DAGs)

## Interesting Stack Overflow Questions

- [What does GIT PUSH do exactly?](https://stackoverflow.com/q/26005031/7954504)
- [Pull new updates from original GitHub repository into forked GitHub repository](https://stackoverflow.com/q/3903817/7954504)
- [How do I delete a Git branch both locally and remotely?](https://stackoverflow.com/q/2003505/7954504)
- [What does GIT PUSH do exactly?](https://stackoverflow.com/questions/26005031/what-does-git-push-do-exactly/26005964#26005964)

TODO: more

## Software

- [GitX](http://gitx.frim.nl/)
- [Tower](https://www.git-tower.com/mac/)

# About Git (No Git Commands Here!)

## Version Control Systems (VCS)

You can think of a version control system (short: "VCS") as a kind of "database". It lets you save a snapshot of your complete project at any time you want.  Version control is independent of the kind of project/language you're working with.

<img src="https://www.git-tower.com/learn/content/01-git/01-ebook/en/01-command-line/02-basics/01-what-is-version-control/what-is-vcs.png" alt="version_control.png" width="600" align="center"/>

Git is a _distributed_ VCS (DVCS), as opposed to a _centralized_ VCS.  In a DVCS, clients don’t just check out the latest snapshot of the files; rather, they **fully mirror** the repository, including its full history.  There is no central server with DVCS.  In Git, however, every developer is potentially both a node and a hub.

Git is _not_ delta-based VCS.  It is instead a set of miniature but complete snapshots.  To be efficient, if files have not changed, Git doesn’t store the file again, just a link to the previous identical file (technically, its contents) it has already stored.

## File States in Git

Each file in your working directory can be in one of two states: _tracked or untracked_.

Tracked files are files that were in the last snapshot; they can be unmodified, modified, or staged.

1. **Modified** means that there's been changes to the file but it's not committed yet.  This isn't a git command; when you manually edit any file in a git repo, you're modifying it.
2. **Staged** means that you have marked a file to go into your next commit snapshot.  Changes you make to files get marked in "chunks" or stages, and you decide how intermittently to take a snapshot of those changes.
3. **Committed** means that the changes you made have been stored/documented safely.

Untracked files are everything else: any files in your working directory that were not in your last snapshot and are not in your staging area.

![imgs/lifecycle.jpg](imgs/lifecycle.jpg)

## The Git Object Model

Let's start with a basic question: what is a repository?

> Think of a repository as a kind of **database** where your VCS stores all the versions and metadata that accumulate in the course of your project.  **In Git, the repository is just a simple hidden folder named `.git` in the root directory of your project.**

_Following excerpted from Loeliger & McCullough_:

Within a repository, Git maintains **two primary data structures, the object store and the Index**.

- The object store is designed to be efficiently copied during a clone operation as part of the mechanism that supports a fully distributed VCS.
- The Index is transitory information, is private to a repository, and can be created or modified on demand as needed.

Before we go any further, it can be illustrative to look at an "empty" Git repository after it has first been initialized, with no other action taken.  Note below that the contents of `hooks/` are excluded from display:

```bash
 repo2$ tree -F -I *.sample\* .git/
.git/
├── HEAD
├── config
├── description
├── hooks/
├── info/
│   └── exclude
├── objects/
│   ├── info/
│   └── pack/
└── refs/
    ├── heads/
    └── tags/
```

### Object Store

Git places only four types of objects in the object store: **blobs, trees, commits, and tags**.

Blobs:

> Each version of a file is represented as a blob. Blob, a contraction of "binary large object," is a term that's commonly used in computing to refer to some variable or file that can contain any data and whose internal structure is ignored by the program. A blob is treated as being opaque. A blob holds a file's data but does not contain any metadata about the file or even its name.

Trees:

> A tree object represents one level of directory information. It records blob identifiers, path names, and a bit of metadata for all the files in one directory. It can also recursively reference other (sub)tree objects and thus build a complete hierarchy of files and subdirectories.

Commits:

> A commit object holds metadata for each change introduced into the repository, including the author, committer, commit date, and log message. Each commit points to a tree object that captures, in one complete snapshot, the state of the repository at the time the commit was performed. The initial commit, or root commit, has no parent. Most commits have one commit parent, although later in the book (Chapter 9) we explain how a commit can reference more than one parent.

Tags:

> A tag object assigns an arbitrary yet presumably human readable name to a specific object, usually a commit. Although 9da581d910c9c4ac93557ca4859e767f5caf5169 refers to an exact and well-defined commit, a more familiar tag name like Ver-1.0-Alpha might make more sense!

## Git Index

The Index is a **temporary** and **dynamic** binary file that describes the directory structure of the entire repository. More specifically, the Index captures a version of the project’s overall structure at some moment in time.

## TODO

[from website...]

A Git repository contains, among other things, the following:

- A set of commit objects.
- A set of references to commit objects, called heads.  (_Not_ HEADs--two different things.)

So then, what is a commit object?  A commit object contains three things:

- A set of files, reflecting the state of a project at a given point in time.
- References to parent commit objects.  A project always has one commit object with no parents. This is the first commit made to the project repository.
- An SHA1 name, a 40-character (160-bit/20-byte) string that uniquely identifies the commit object.

The above is why Git is often visualized in terms of a directed acyclic graph (DAG).  You can visualize a repository as a directed acyclic graph of commit objects, with pointers to parent commits always pointing backwards in time, ultimately to the first commit.

A **head** is simply a reference to a commit object. Each head has a name. By default, there is a head in every repository called `master`. A repository can contain any number of heads. At any given time, one head is selected as the "current head. This head is aliased to `HEAD`, always in capitals.

Notice from above that the `.git/objects` directory (the directory for all of Git's objects) is initially empty, except for a few placeholders.

Let's now carefully create a simple object:

```bash
 repo2$ echo "hello world" > hello.txt
 repo2$ git add hello.txt
```

Now, how has `objects/` changed?  You now have one object for `hello.txt`.

```bash
 repo2$ tree -F .git/objects/
.git/objects/
├── 3b/
│   └── 18e512dba79e4c8300dd08aeb37f8e728b8dad
├── info/
└── pack/
```

An important concept is that **Git tracks content** instead of files.  (Literally, the content of files.)

When it creates an object for `hello.txt`, Git doesn't care that the filename is `hello.txt`. Git cares only about what's inside the file: the sequence of 12 bytes that represent "hello world" and the terminating newline (the same blob created earlier). Git performs a few operations on this **blob**, calculates its SHA1 hash, and enters it into the object store as a file named after the hexadecimal representation of the hash.

The subdirectory structure (`3b/`) is to improve filesystem efficiency.

## Trees

As mentioned previously a Git _blog_ object only hashes the contents of a file, not its name or any other metadata.

Git tracks the pathnames of files through another kind of object called a _tree_. When you use `git add`, Git creates a blob for the contents of each file you add, but it doesn’t create an object for your tree right away. Instead, it updates the Index.

You can think of Git as manipulating **three trees** in its normal operation:

1. The **working tree** - your sandbox.  Holds the actual files (i.e. `.py`) of your project.
2. The **Index** - staging area.  It stores information about what will go into your next commit.
    - `git ls-files -s` shows you what the Index looks like.
    - The Index is not technically a tree structure--it's actually implemented as a flattened manifest.
    - The Index is found in .git/index and keeps track of file pathnames and corresponding blobs.
    - Each time you run commands such as `git add`, `git rm`, or `git mv`, Git updates the Index with the new pathname and blob information.
3. The **HEAD** - snapshot of your last commit on current branch.
    - Pointer to the current branch reference, which is in turn a pointer to the last commit made on that branch.

You edit files themsleves in the working directory, and commit your changes to the repository itself.  The Index is effectively a **layer** between the working directory and the repository to stage, or collect, alterations.  When you manage your code with Git, you edit in your working directory, accumulate changes in your index, and commit whatever has amassed in the index as a single changeset.

[Reset Demystified](https://git-scm.com/book/en/v2/Git-Tools-Reset-Demystified) has a good visualization of these operations.

## A Golden Rule of Version Control

A single commit should only wrap related changes: fixing two different bugs should produce (at the very least) two separate commits.  When crafting a commit, it's very important to only include changes that belong together. You should never mix up changes from multiple, different topics in a single commit.

# Quick Reference: Commands

Structure: `git` is the program; the commands are technically _subcommands_: `git SUBCOMMAND [args]`.

Documentation for each git subcommand is available using:

- `git help subcommand`
- `git --help subcommand`
- `git subcommand --help`
- `man git-subcommand`

In addition, if you don’t need the full-blown manpage help, but just need a quick refresher on the
available options for a Git command, you can ask for the more concise "help" output with the `-h` or `--help` options, as in:

```bash
 ~$ git add -h
usage: git add [<options>] [--] <pathspec>...

    -n, --dry-run         dry run
    -v, --verbose         be verbose

    -i, --interactive     interactive picking
    -p, --patch           select hunks interactively
    -e, --edit            edit current diff and apply
    -f, --force           allow adding otherwise ignored files
    -u, --update          update tracked files
    -N, --intent-to-add   record only the fact that the path will be added later
    -A, --all             add changes from all tracked and untracked files
    --ignore-removal      ignore paths removed in the working tree (same as --no-all)
    --refresh             don't add, only refresh the index
    --ignore-errors       just skip files which cannot be added because of errors
    --ignore-missing      check if - even missing - files are ignored in dry run
    --chmod <(+/-)x>      override the executable bit of the listed files
```

Git commands understand both "short" and "long" options:

```bash
$ git commit -m "Fixed a typo."
$ git commit --message="Fixed a typo."  # equivalent
```

You can separate options from a list of arguments via the "bare double dash" convention. For instance, use the double dash to contrast the control portion of the command line from a list of operands, such as filenames.

```bash
$ git diff -w master origin -- tools/Makefile
```

Commands - quick reference:

**Note**: these are _not_ "full" syntaxes (they exclude some flags).  Rather, these should cover 98% of everyday cases.

- `git [--version] [--help] [--exec-path] [--html-path] [--man-path] [-p]`
- `git help [-a] [-g] [COMMAND|GUIDE]`
- `git add [-v] [-n] [-f] [<pathspec>...]`
- `git blame [-L <range>] [-t] <file>`
- `git branch`:
    - `git branch [-v] [-r | -a] [--list] [<pattern>...]`
    - `git branch -m [<oldbranch>] <newbranch>`
    - `git branch -u <upstream> [<branchname>]`
    - `git branch (-d | -D) [-r] <branchname>...`
    - `git branch --edit-description [<branchname>]`
- `git checkout`:
    - `git checkout <branch>`
    - `git checkout -b <new_branch>`
    - `git checkout [--] <paths>...`
- `git clone [-v] [-o <name>] <repository> [<directory>]`
- `git commit [-a] [-v] [--amend] [-m <msg>] [<file>...]`
- `git config`:
    - `git config [<file-option>] -l`
    - `git config [<file-option>] [type] [--show-origin] [-z|--null] name [value [value_regex]]`
    - `git config [<file-option>] [type] --add name value`
    - `git config -e [--global]`
- `git diff`: (TODO)
    - `git diff [options] [<commit>] [<path>...]`
    - `git diff [options] --cached [<commit>] [--] [<path>...]`
    - `git diff [options] <commit> <commit> [--] [<path>...]`
- `git init [directory]`
- `git log [--stat] [-p] [--oneline] [--graph] [--decorate] [--abbrev-commit | --no-abbrev-commit] [--reverse] [-n <number>] [--skip=<number>] [--before=<date>] [--after=<date>] [--author=<pattern>] [--branches[=<pattern>]] [<path>...]`
- `git merge [-n] [-v] [-s <strategy>] [--allow-unrelated-histories] [-m <msg>] [<commit>...]`
- `git pull [-v] [-r] [--stat] [-s <strategy>] [<repository>]`
- `git push [--all] [-v ] [-u] [<repository>]`
- `git remote`
    - `git remote [-v]`
    - `git remote add [-t <branch>] [-m <master>] [-f] <name> <url>`
    - `git remote rename <old> <new>`
    - `git remote remove <name>`
    - `git remote [-v] show <name>...`
- `git reset [--hard] [<commit>]`
- `git rm [-f] [-r] <file>...`
- `git status [-v] [-s] [-b] [--ignored]`

TODO:
- `git stash`
- `git mv`
- `git diff`
- `git fetch`
- `x`
- `git show [options] <object>...`
- `git request-pull`
- `git rebase`
- `git clean`

# Local Git

This section covers working with Git on a _local, individual basis_: no interaction with a team and minimal interaction with remotes (or GitHub, by extension).

## Creating a Repo: `git init`

There are two ways to create or copy a repo: `git init` and `git clone`.  We will save `git clone` for later and use `git init` here, which initializes a repository.

You can either:

- create your project (directory), `cd` into it, then use `git init`
- use `git init <directory>`, without first creating the directory itself, and then `cd` into it.

```bash
 ~$ mkdir myrepo/
 ~$ cd myrepo/
 myrepo$ git init
Initialized empty Git repository in /Users/brad/myrepo/.git/
```

As mentioned above, the `.git` folder is the actual repository.

```bash
 myrepo$ tree .git/
.git/
├── HEAD
├── config
├── description
├── hooks
│   ├── applypatch-msg.sample
│   ├── commit-msg.sample
│   ├── post-update.sample
│   ├── pre-applypatch.sample
│   ├── pre-commit.sample
│   ├── pre-push.sample
│   ├── pre-rebase.sample
│   ├── pre-receive.sample
│   ├── prepare-commit-msg.sample
│   └── update.sample
├── info
│   └── exclude
├── objects
│   ├── info
│   └── pack
└── refs
    ├── heads
    └── tags

8 directories, 14 files
```

Initially, some subdirectories as well as a HEAD file that references the HEAD of the master branch are created.

Note that this initial repository is truly _empty_.  Even if you have some files in the project already, Git did _not_ add the current content of your working copy as something like an "initial version". The repository contains not a single version of your project, yet.

When initialized, we are on the `master` branch by default, with no commits or anything in the staging area.

## Staging and Committing (`git status`, `git add`, and `git commit`)

Let's jump into things.  We will add a file, stage it, and commit it.  Create a 'hello Git' Python file in `myrepo/`.

```python
# hello.py
if __name__ == '__main__':
    print('hello Git')
```

Now let's check `git status` for the first time.

```bash
 myrepo$ git status -v
On branch master

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)

    hello.py

nothing added to commit but untracked files present (use "git add" to track)
```

The file is untracked; untracked files are not part of the repo or part of version control.

We tell Git to track it by adding it to the _staging area_ (Index) with `git add`.  We then commit that file and save a snapshot of the repository at that point.  **The Index holds a snapshot of the content of the working tree, and it is this snapshot that is taken as the contents of the next commit.**

Thus after making any changes to the working tree, and before running `git commit`, you must use `git add` command to add any new or modified files to the index.  One benefit of having a staging area is that a developer may only want to commit a subset of all modified files.

> See also: [Understanding the Git Index](https://alblue.bandlem.com/2011/10/git-tip-of-week-understanding-index.html)

```bash
 myrepo$ git add hello.py
 myrepo$ git status
On branch master

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)

    new file:   hello.py

 myrepo$ git commit -v -m 'init hello.py'
[master (root-commit) 68bdab5] init hello.py
 1 file changed, 3 insertions(+)
 create mode 100644 hello.py
```

More detail: what does `git commit` do?

- It records changes to the repository, storing the current contents of the index in a new commit along with a log message from the user describing the changes.  **Specifically, the changes are committed to HEAD.**
- `git add` can be used repeatedly in between commits and incrementally adds changes to the index before committing.

### Do I Need `git add`?  What about `git commit -a`?

The short answer is that `git add` is not technically always needed.

For the long answer, it is worth posting a snippet from `git help commit` [emphasis added].  At the end of the day, a commit _stores the current contents of the Index in a new commit._

> The content to be added can be specified in several ways:
>
> 1. by using `git add` to incrementally "add" changes to the index before using `git commit`
>
> 2. by using `git rm` to remove files from the working tree and the Index, again before using `git commit`
>
> 3. by listing files as arguments to the commit command, **in which case the commit will ignore changes staged in the Index, and instead record the current content of the listed files (which must already be known to Git)**
>
> 4. by using the `-a` switch with `git commit` to automatically "add" changes from all known files (i.e. all files that are already listed in the index) and to automatically "rm" files in the index that have been removed from the working tree, and then perform the actual commit;

In other words, the main effect of `-a` is that it affects deleted files.  It automatically stages files that have been modified and deleted, _but untracked files are not affected_.  (So, this would not have worked above.)  Adding the `-a` option **makes Git automatically stage every file that is already tracked** before doing the commit, letting you skip `git add`.

Here is a full-fledged example of when you would want to explicitly use `git add`.

```bash
 ~$ git init trial
Initialized empty Git repository in /Users/brad/trial/.git/

 ~$ cd trial
 trial$ touch data
 trial$ git status -s
?? data

 trial$ git hash-object data
e69de29bb2d1d6434b8b29ae775ad8c2e48c5391

 trial$ git add data  # we are intentionally not committing yet

 trial$ git ls-files --stage
100644 e69de29bb2d1d6434b8b29ae775ad8c2e48c5391 0   data

# Edit "data" to contain...
 trial$ cat data
New data
And some more data now

# The hash of data's contents is now different from what
# is in Index.
 trial$ git ls-files --stage
100644 e69de29bb2d1d6434b8b29ae775ad8c2e48c5391 0   data
 trial$ git hash-object data
e476983f39f6e4f453f0fe4a859410f63b58b500

 trial$ git status
On branch master

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)

    new file:   data

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

    modified:   data

# Now, what happens if we commit without a further `git add`?
# Only the file *creation* is commited
 trial$ git commit -m 'what happens here?'
[master (root-commit) c4f7484] what happens here?
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 data

 trial$ git status -s
 M data
```

Above, you _must_ run `git add` to update the Index with the absolute latest and greatest version of your file. If you don’t, you’ll have two different versions of the file: one captured in the object store and referenced from the index, and the other in your working directory.

Remember: **Git stages a file exactly as it is when you run `git add`**. If you commit now, the version of `data` as it was when you last ran `git add` is how it will go into the commit, not the version of the file as it looks in your working directory when you run `git commit`.

Think of `git add` not as "add this file," but more as "add this content."

Here is an example illustrating `git commit -a`:

```bash
 ~$ git init /tmp/commit-all-example
 ~$ cd /tmp/commit-all-example/

# >> is IO redirection like >, but appends if
# the file already exists.
 commit-all-example$ echo something >> ready
 commit-all-example$ echo somthing else >> notyet

 commit-all-example$ git status -s
?? notyet
?? ready

# Add both and commit them as normal.
 commit-all-example$ git add ready notyet
 commit-all-example$ git status -s
A  notyet
A  ready
 commit-all-example$ git commit -m "Setup"
[master (root-commit) c0155ea] Setup
 2 files changed, 2 insertions(+)
 create mode 100644 notyet
 create mode 100644 ready

# Modify `ready` and `git add` it.
 commit-all-example$ cat ready
something
something else
 commit-all-example$ git add ready

# Modify `notyet` but *don't* `git add` it.
# In other words, leave it *tracked but unstaged*.
 commit-all-example$ cat notyet
somthing else
this is unstaged!

# Add a new file in a subdirectory, but don't `git add` it either.
 commit-all-example$ mkdir subdir
 commit-all-example$ echo Nope >> subdir/new
 commit-all-example$ tree
.
├── notyet
├── ready
└── subdir
    └── new
```

At this point, we have:

- One file that is tracked and stage (`ready`)
- One file that is tracked but not staged (`notyet`)
- One file that is neither tracked nor staged (`subdir/new`)

Here are the consequences of using different commits:

- `git commit [-m <msg]` would commit just one file, `ready`--the only one that is staged.
- `git commit -m 'both staged & unstaged' ready notyet` would commit both files.
- `git commit --all` will do the same as the option above this.  It ignores `subdir/new`, though, because that file is untracked.

```bash
 commit-all-example$ git commit -m 'roll this back'
[master 9680a9d] roll this back
 1 file changed, 1 insertion(+)
 commit-all-example$ git status -s
 M notyet
?? subdir/

# Undo the commit.
# HEAD~1 == parent of HEAD.
 commit-all-example$ git reset --soft HEAD~1
 commit-all-example$ git status -s
 M notyet
M  ready
?? subdir/
```

## Tracked versus Staged

"Tracked" is a formal "stage" for Git file classification (tracked, ignored, untracked).

"Staging" _puts a file in the Index._  `git add` both stages a file and tracks it, if it is untracked.

## Check Specific Differences: `git diff`

`git diff` is like a more precise `git status`.  It shows exactly what has been modified.  `git diff HEAD` is a way to see what changes we're committing.

Technically, it shows the difference between `HEAD` and the current project state.

Below, we added three lines to `hello.py`, but did not yet stage it.

```bash
 myrepo$ git diff hello.py
diff --git a/hello.py b/hello.py
index 7df304e..8dc5777 100644
--- a/hello.py
+++ b/hello.py
@@ -5,3 +5,6 @@ def main():
 if __name__ == '__main__':
     # The main script.
     main()
+
+    # Let's do it again.
+    main()
```

We can view diffs for staged files with `git diff --cached`:

```bash
 myrepo$ git add hello.py
 myrepo$ git diff  # nothing here
 myrepo$ git diff --cached
diff --git a/hello.py b/hello.py
index 7df304e..8dc5777 100644
--- a/hello.py
+++ b/hello.py
@@ -5,3 +5,6 @@ def main():
 if __name__ == '__main__':
     # The main script.
     main()
+
+    # Let's do it again.
+    main()
```

Summary:

- `git diff` displays the changes that remain in your working directory and are **not staged**.  This only shows **unstaged** changes since your last commit.
- `git diff --cached` or `git diff --cached` shows changes that are staged and will therefore contribute to your next commit.  This will let you compare your staged changes to your last commit.

## Ignore Files: `.gitignore`

Typically, there are a couple of files that you don't want to be under version control: for instance, `.DS_Store` files on Mac OSX.  Another example is the `__pycache__` directory created when a local module is imported and compiled to bytecode.

To ignore these, create a file `.gitignore` in the root of your project.  This specifies intentionally untracked files to ignore.

To illustrate, add a second Python file:

```python
# myname.py
import hello

hello()
print('My name is Brad.')
```

Also modify `hello.py`:

```python
# hello.py
def main():
    print('hello Git')

if __name__ == '__main__':
    # The main script.
    main()
```

Now run it:

```bash
 myrepo$ python3 myname.py
hello Git
My name is Brad.
```

Now you have two untracked files:

```bash
 myrepo$ git status -s
 M hello.py
?? __pycache__/
?? myname.py
```

To get rid of (ignore) `__pycache__`, add the following `.gitignore`:

```bash
 myrepo$ touch .gitignore
```

```python
# .gitignore
__pycache__/
```

Finally, let's stage and two do separate commits: one for adding the `.gitignore`, and one for the files:

```bash
 myrepo$ git status -s
 M hello.py
?? .gitignore
?? myname.py

 myrepo$ git add *.py
 myrepo$ git commit -m 'add second .py file'
[master 5b412ff] add second .py file
 2 files changed, 9 insertions(+), 1 deletion(-)
 create mode 100644 myname.py

 myrepo$ git add .gitignore
 myrepo$ git commit -m 'add .gitignore'
[master d7f0a09] add .gitignore
 1 file changed, 2 insertions(+)
 create mode 100644 .gitignore

 myrepo$ git status
On branch master
nothing to commit, working tree clean
```

> **Note**: adding a `.gitignore` works retroactively, as in the above example.  However, this is only because we haven't made the commit.  (Files already tracked by Git are not affected.)  Try to add a `.gitignore` up front before any commits.

See `git help gitignore` > _Pattern Format_ for detailed description of how file patterns are treated.

A helpful compilation of ignore rules for different projects and platforms can be found here: [github.com/github/gitignore](github.com/github/gitignore).

## Deleted and Moved Files: `git rm` & `git mv`

Deleting a file constitutes an action that you want to track.  After deleting the file or subdirectory itself, use `git rm` to also remove it from the index (staging area) and working tree, then commit that change:

```bash
 myrepo$ rm myname.py
myname.py

 myrepo$ git status
On branch master
Changes not staged for commit:
  (use "git add/rm <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

    deleted:    myname.py

no changes added to commit (use "git add" and/or "git commit -a")

 myrepo$ git rm myname.py
rm 'myname.py'
 myrepo$ git commit -m 'delete myname.py'
[master 23a8fbb] delete myname.py
 1 file changed, 5 deletions(-)
 delete mode 100644 myname.py
```

To reiterate, `git rm` is not deleting the physical file itself; it is removing Git's reference to it.

> Note: If you modified the file and added it to the staging area already, you must force the removal with the `-f` option.

Similarly, `git mv` moves or renames a file or a directory within the repository.

## History: `git log`

Let's take a quick look at our commit log with `git log`.  With this command, there are a ton of (1) options and (2) ways to limit revision history that is displayed.  Here's a _condensed_ syntax:

```
git log
    [--stat]
    [-p]
    [--oneline] [--graph] [--decorate]
    [--no-abbrev-commit | --abbrev-commit]
    [--reverse] [-n <number>] [--skip=<number>] [--before=<date>] [--after=<date>] [--author=<pattern>] [--branches[=<pattern>]]
    [<path>...]`
```

Flags/options:

- `--stat` generates a _diffstat_, an abbreviated stat list for each commit.  (Include which files were altered and the relative number of lines that were added or deleted from each of them.)
- `-p` shows the diff (the patch output) introduced in each commit.
- The third line is concerned with output _formatting_.
- `--no-abbrev-commit` shows the full 40-byte hexadecimal commit object name instead of a prefix.
- The fourth line is conerend with _commit limiting_.
- `<path>...`: Commits modifying the given <paths> are selected.

Example:

```bash
 myrepo$ git log -n 2 --no-abbrev-commit
commit 23a8fbbc5d75e77e322b3357135e6e43788f7bf9 (HEAD -> master)
Author: Brad Solomon <brad.solomon.1124@gmail.com>
Date:   Sat May 12 16:22:17 2018 -0400

    delete myname.py

commit d7f0a096245dd695655e1b3b88a63db7c40f2ec4
Author: Brad Solomon <brad.solomon.1124@gmail.com>
Date:   Sat May 12 16:20:55 2018 -0400

    add .gitignore
```

## Branching (`git branch`, `git checkout`)

So far, as alluded to by `git status` we have been on the default _branch_, named `master`:

```bash
 myrepo$ git branch --list
* master
```

Branches are used to develop features isolated from each other. Branches provide a way for you to keep separate streams of development apart.  Create and use other branches for development, and merge them back to the master branch upon completion.  A branch represents a "sub-context" within a project.  In real-world projects, work always happens in multiple of these contexts in parallel.

**All the changes you make at any time will only apply to the _currently active_ branch; all other branches are left untouched.**  This gives you the freedom to both work on different things in parallel.

Branches are not "optional" in Git.  You are always working on a certain branch (the **currently active**, or "checked out", or "HEAD" branch).

So, which branch is HEAD at the moment? `git status` tells us in its first line of output,

```bash
 myrepo$ git status
On branch master
```

Let's create a new branch, `contact-form`.  There are two ways to do this:

```bash
# Option 1 - Creates a new branch head which points to the current HEAD
 myrepo$ git branch contact-form
 myrepo$ git branch -l
  contact-form
* master

# Option 2
# Specifying -b causes a new branch to be created as if
# git-branch(1) were called and then checked out.
# This will also switch to the branch in one step.
 myrepo$ git checkout -b contact-form-2
Switched to a new branch 'contact-form-2'
 myrepo$ git branch -l
  contact-form
* contact-form-2
  master

# Let's delete this branch.
# We need to checkout something different first.
 myrepo$ git checkout master
Switched to branch 'master'
 myrepo$ git branch -d contact-form-2
Deleted branch contact-form-2 (was 23a8fbb).
```

Recall from an earlier section that you can think of Git as manipulating **three trees** in its normal operation: HEAD, Index, Working Tree.  When you `git checkout` a branch, this:

- Changes HEAD to point to the new branch ref
- Populates your Index with the snapshot of that commit
- Copies the contents of the Index into your Working Tree

**Note**: The terms "branch" and "head" (not to be confused with `HEAD`) are nearly synonymous in Git. Every branch is represented by one head, and every head represents one branch.

Knowing the above, we can also **create a branch (head) that points to a previous commit**.  Below, `HEAD^` is an alias for the parent of the `HEAD` commit.

```bash
 myrepo$ git branch fix-headers HEAD^

# fix-headers points to previous commit;
# so does contact-form.
 myrepo$ git branch -v
  contact-form 23a8fbb delete myname.py
  fix-headers  23a8fbb delete myname.py
* master       8a81997 call twice

# Finally, checkout this branch.
 myrepo$ git checkout fix-headers
Switched to branch 'fix-headers'
```

What does this do?  `HEAD` now points to the commit object specified by `fix-headers`.

## Merging (`git merge`)

Eventually, you need to merge a branch with `master`.  You do that with `git merge`.  The basic syntax is `git merge [-v] [-m <msg>] [<commit>...]`.

Here's an example (with some output hidden):

```bash
 myrepo$ touch headers.txt
 myrepo$ git status
On branch fix-headers
Untracked files:
  (use "git add <file>..." to include in what will be committed)

    headers.txt

nothing added to commit but untracked files present (use "git add" to track)

 myrepo$ git add .
 myrepo$ git diff HEAD
diff --git a/headers.txt b/headers.txt
new file mode 100644
index 0000000..e69de29

 myrepo$ git commit -m 'init headers.txt'

# git-merge merges changes from <commit> into the current branch.
# So switch to master first.
 myrepo$ git checkout master

 myrepo$ git merge fix-headers
Merge made by the 'recursive' strategy.
 headers.txt | 0
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 headers.txt

 myrepo$ git log -n 1
commit 2196932549f6c46de150ccf4d69d053a7129ad92 (HEAD -> master)
Merge: 8a81997 9a7d989
Author: Brad Solomon <brad.solomon.1124@gmail.com>
Date:   Sat May 12 19:05:49 2018 -0400

    Merge branch 'fix-headers'
```

Here's a useful excerpt from `git help merge`:

```
       Assume the following history exists and the current branch is "master":

                     A---B---C topic
                    /
               D---E---F---G master

       Then "git merge topic" will replay the changes made on the topic branch since it diverged from master (i.e., E)
       until its current commit (C) on top of master, and record the result in a new commit along with the names of
       the two parent commits and a log message from the user describing the changes.

                     A---B---C topic
                    /         \
               D---E---F---G---H master
```


# Working with Remotes

## Local Versus Remote Repos

- A "local" repository resides on your local computer, as a ".git" folder inside your project's root folder. You are the only person that can work with this repository, by committing changes to it.
- A "remote" repository, in contrast, is typically located on a remote server on the internet or in your local network. No actual working files are associated with a remote repository: it has no working directory but it exclusively consists of the ".git" repository folder. Teams are using remote repositories to share & exchange data: they serve as a common base where everybody can publish their own changes and receive changes from their teammates.

> Note: Remote repositories can be on your local machine.  The word “remote” does not necessarily imply that the repository is somewhere else on the network or Internet, only that it is elsewhere and that you push/pull interact with it.

When you clone a repository from a remote server, Git automatically remembers this connection for you. It saves it as a **remote** called "origin" by default.  `origin` is the default name Git gives to the server you cloned from.

## URL Structure

Several commands (`git clone`, `git fetch`, `git pull`, or `git push`) have a URL as a parameter.  (Sometimes this is not a "technically correct" URL as defined by the relevant RFCs.)  Git supports **local, ssh, git, http, and https** protocols.

The simplest form of Git URL refers to a repository on a local filesystem, be it a true physical filesystem or a virtual filesystem mounted locally via the Network File System (NFS). There are two permutations:

> - /path/to/repo.git
> - file:///path/to/repo.git

The other forms of the Git URL refer to repositories on remote systems.

As mentioned above, Git has its own _Git native protocol_.  This is a special daemon that comes packaged with Git; it listens on a dedicated port (9418) that provides a service similar to the SSH protocol, but with absolutely **no authentication**.  The same is true for http.

> git://example.com/path/to/repo.git

When you `git clone`, `git fetch`, `git pull`, or `git push` to a remote repository using HTTPS URLs on the command line, you'll be asked for your GitHub username and password each time.

Lastly, there are two syntaxes for ssh:

> - ssh://[user@]host.xz[:port]/path/to/repo.git/
> - [user@]host.xz:path/to/repo.git/

Notice the very slightly different syntaxes.  These are two working examples:

```bash
 tmp$ git clone git@github.com:bsolomon1124/github-playground.git  # colon
 tmp$ git clone ssh://git@github.com/bsolomon1124/github-playground.git  # slash
```

See also: [Which remote URL should I use?](https://help.github.com/articles/which-remote-url-should-i-use/)

## SSH Setup

Secure Shell (SSH) is a network protocol for operating network services securely over an unsecured network.  It is a means by which to connect and log in to a specified host, and the **client must prove their identity to the remote machine**.

Authentication with SSH uses a two-part key: a public and a private one.

The public key should be installed on all servers to which you want access.  When a connection via SSH is trying to be established, the server will only grant access if it has a public key installed that matches the private key of the requesting computer.

Detailed instructions for connecting (to GitHub) with SSH are here:

> [Connecting to GitHub with SSH](https://help.github.com/articles/connecting-to-github-with-ssh/)

See also: [Switching remote URLs from HTTPS to SSH](https://help.github.com/articles/changing-a-remote-s-url/#switching-remote-urls-from-https-to-ssh)

To authenticate: `ssh -T git@github.com`.

## Cloning a Repo: `git clone`

This command makes a copy of a repository locally.  Note that the cloned repository is **complete**: it includes all of the commits and all of the branches ever made on the original, as of the time of cloning.

Remember, `git clone` can be used with any URL (local files or files on another server).  However, it's most frequently used for the latter.

First, fork the repo [Data4Democracy/github-playground](https://github.com/Data4Democracy/github-playground) to your account.  Just click "Fork" at the top-right of the page.

Now navigate to <https://github.com/[your_username]/github-playground>.  (In my case, https://github.com/bsolomon1124/github-playground.)

Click "Clone or Download" > "Use SSH" and click the clipboard icon.

```bash
 ~$ git clone -v git@github.com:bsolomon1124/github-playground.git
Cloning into 'github-playground'...
remote: Counting objects: 197, done.
remote: Compressing objects: 100% (2/2), done.
remote: Total 197 (delta 0), reused 2 (delta 0), pack-reused 194
Receiving objects: 100% (197/197), 295.41 KiB | 4.41 MiB/s, done.
Resolving deltas: 100% (72/72), done.
```

This uses the default remote name **origin** to keep track of the **upstream repository**.

Note that the cloned repo has a `.git` directory, even if that's not visible on GitHub:

```bash
 github-playground$ ls -d .[!.]?*  # hidden
.git        .gitignore
```

## Tracking and Manipulating Remotes: `git remote`

More broadly, _remotes_ is another term for a _set of repositories whose branches you're tracking._  You can have multiple remotes.

`git remote` manages these tracked repositories.

```bash
 github-playground$ git remote -v
origin  git@github.com:bsolomon1124/github-playground.git (fetch)
origin  git@github.com:bsolomon1124/github-playground.git (push)
```

A common layout is an interaction of three repositories: the "upstream" repo, your "origin" forked repo, and your local cloned repo:

```
          "upstream"                                         "origin"
Data4Democracy/github-playground    ---fork--->   _bsolomon1124/github-playground
                                \                 /\
                                 \               /
                                  \             /
                                  _\/          /
                                    local clone
```

```bash
 nyc18_ds14$ git remote -v
origin  git@github.com:bsolomon1124/nyc18_ds14.git (fetch)
origin  git@github.com:bsolomon1124/nyc18_ds14.git (push)
upstream    git@github.com:thisismetis/nyc18_ds14.git (fetch)
upstream    git@github.com:thisismetis/nyc18_ds14.git (push)
```

## Update Remote Branches: `git fetch`

From [Introduction to Git and GitHub for Python Developers](https://realpython.com/python-git-github-intro/):

> To explain the `fetch` command clearly, we need to take a step back and talk about how Git manages the relationship between your local repo and a remote repo. This next part is background, and while it's not something you'll use on a day-to-day basis, it will make the difference between `fetch` and `pull` make more sense.
>
> When you `clone` a new repo, Git doesn't just copy down a single version of the files in that project. It copies the entire repository and uses that to create a new repository on your local machine.
>
> Git does not make local branches for you except for master. However, it does keep track of the branches that were on the server. To do that, Git creates a set of branches that all start with `remotes/origin/<branch_name>`.
>
> Only rarely (almost never), will you check out these `remotes/origin` branches, but it's handy to know that they are there. Remember that every branch that existed on the remote when you cloned the repo will have a branch in `remotes/origin`.
>
> When you create a new branch and the name matches an existing branch on the server, Git will mark you local branch as a *tracking branch* that is associated with a remote branch. We'll see how that is useful when we get to `pull`.
>
> Now that you know about the `remotes/origin` branches, understanding `git fetch` will be pretty easy. All `fetch` does is update all of the `remotes/origin` branches. It will modify only the branches stored in `remotes/origin` and not any of your local branches.

To elaborate on the above: note that a repository that has remotes will have `.git/refs/remotes/`, while a "local-only" repo will not:

```bash
 ~$ tree ~/myrepo/.git/refs/
/Users/brad/myrepo/.git/refs/
├── heads
│   ├── contact-form
│   └── master
└── tags

2 directories, 2 files
 ~$ tree ~/github-playground/.git/refs/
/Users/brad/github-playground/.git/refs/
├── heads
│   └── master
├── remotes
│   └── origin
│       └── HEAD
└── tags
```

In the above example from `git remote`, using `git fetch upstream` would fetch all the information that `upstream` has but that you don't yet have in your repository.

```bash
 nyc18_ds14$ git fetch upstream
remote: Counting objects: 74, done.
remote: Total 74 (delta 34), reused 34 (delta 34), pack-reused 39
Unpacking objects: 100% (74/74), done.
From github.com:thisismetis/nyc18_ds14
 * [new branch]      notes       -> upstream/notes
 * [new branch]      submission0 -> upstream/submission0
```

While this is not the first time `fetch` is run for this repo, an earlier execution made `upstream`'s master branch accessible locally as `upstream/master`.  The above also makes `notes` and `submission0` accessible.

`git fetch` only downloads data to your local repository--it does no merging.

## Interaction: `git push` & `git pull`

### Pulling

In the section above on `git fetch`, it was mentioned that this only downloads data, but does no merging.

**If your current branch is set up to track a remote branch, use `git pull` to automatically fetch and then merge that remote branch into your current branch.**  `git clone` automatically sets up your local master branch to track the remote master branch on the server you cloned from.

What if we edit the files in GitHub?  Can we have this change our files locally?  Let's try making a small "direct" edit to [`myfile.txt`](https://github.com/bsolomon1124/github-playground/blob/master/myfile.txt) on GitHub, while adding a commit message and then clicking "commit changes" in the browser.

These changes _will not_ be immediately reflected in your local machine repo.  How do we get them to be reflected?  With `git pull`.

```bash
 github-playground$ git pull origin master
remote: Counting objects: 3, done.
remote: Compressing objects: 100% (2/2), done.
remote: Total 3 (delta 1), reused 0 (delta 0), pack-reused 0
Unpacking objects: 100% (3/3), done.
From github.com:bsolomon1124/github-playground
 * branch            master     -> FETCH_HEAD
   5e53d51..6034203  master     -> origin/master
Updating 5e53d51..6034203
Fast-forward
 myfile.txt | 1 +
 1 file changed, 1 insertion(+)
```

`git pull` is shorthand for `git fetch` + `git merge`.

If you open this file locally, you'll see that it now reflects the changes from GitHub.  Pulling _updates our local repository to reflect changes/commits made in the remote repo_.  This could be useful if we've invited other people to our GitHub project who have pulled your changes, made their own commits, and pushed them.

### Pushing

When in "Local Git" mode, we stopped with `git commit`.  `git push` is the logical next step when interacting with a remote.  `git push` pushes our local changes to our origin repo.  By default, `git push` expects us to provide it with two things:

1. To which remote repository we want to push. (i.e. `origin`)
2. To which branch on that remote repository we want to push (i.e. `master`).

The syntax is `git push <remote> <branch>`

The remote repository is destination of the push operation.

The name of our remote is `origin` and the default local branch name is `master`.

On the first push to a remote, use `-u`.  This adds an upstream (tracking) reference and enables us to just use argument-less `git push` in subsequent push commands.

Here's a quick example of creating a new file, staging & committing it, and pushing the changes:

```bash
 github-playground$ touch myfile.txt
 github-playground$ git status -sb
## master...origin/master
?? myfile.txt

# Stage & commit.
 github-playground$ git add myfile.txt
 github-playground$ git commit -m 'init myfile.txt'
[master 5e53d51] init myfile.txt
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 myfile.txt

# Push and remember as upstream.
 github-playground$ git push -u origin master
Counting objects: 2, done.
Delta compression using up to 4 threads.
Compressing objects: 100% (2/2), done.
Writing objects: 100% (2/2), 247 bytes | 247.00 KiB/s, done.
Total 2 (delta 1), reused 0 (delta 0)
remote: Resolving deltas: 100% (1/1), completed with 1 local object.
To github.com:bsolomon1124/github-playground.git
   9746397..5e53d51  master -> master
Branch 'master' set up to track remote branch 'master' from 'origin'.
```

Your work should now show up in your remote repository.

There is one part of the "commit output" that deserves more introspection (some lines hidden below):

```bash
 github-playground$ git push origin master
Counting objects: 2, done.
# ...
To github.com:bsolomon1124/github-playground.git
   6034203..48f860c  master -> master              # <-- what's this?
```

The format of the last line is `<oldref>..<newref> fromref -> toref`, where

- `oldref`: the old reference
- `newref`: the new reference
- `fromref`: is the name of the **local reference** being pushed
- `toref`: the name of the **remote reference** being updated

### Aside: What is a ref?

A Git reference (ref) is just a **file that contains a Git commit SHA-1 hash**. When referring to a Git commit, you can use the Git reference, which is an easy-to-remember name, rather than the hash.

- In other words, a ref points to an object name.
- `HEAD` is a "special-purpose" ref.
- The Git reference can be rewritten to point to a new commit.
- A branch is just a Git reference that stores the new Git commit hash.

```bash
 github-playground$ git show-ref
48f860cf047c9499723cd6ac536361cb716050c9 refs/heads/master
48f860cf047c9499723cd6ac536361cb716050c9 refs/remotes/origin/HEAD
b8ab9363854a1364a92440a6e0b24af672c9cdd7 refs/remotes/origin/add-discursive-notebook
48f860cf047c9499723cd6ac536361cb716050c9 refs/remotes/origin/master
```

As you can see above, these are all housed in `.git/refs`:

```bash
 github-playground$ tree .git/refs/
.git/refs/
├── heads
│   └── master
├── remotes
│   └── origin
│       ├── HEAD
│       └── master
└── tags
```

### Troubleshooting: "Your branch is ahead of 'origin/master'"

If you get the message

> `Your branch is ahead of 'origin/master' by [n] commits.`

You need to simply push to origin with `git push origin master`.

# Interaction with GitHub

GitHub is a Git hosting site, alonside BitBucket & GitLab.

GitHub is its own beast. (Not just an interface, it also behaves somewhat like a wrapper around core Git.)  There are a handful of concepts that are unique to or originated from GitHub: forking, pull requests, and issue tracking.

## Pull Requests

A _pull request_ is a GitHub-centric (rather than Git) concept, that is completely distinct from `git pull`.  Pull requests to signal project owners that another programmer has an interesting set of code to potentially merge in.  Pull requests allow any user with a commit that they feel makes a useful contribution to the project to announce that contribution to the core project owners.

Once a contributor has finished coding a feature, **committed that new code to a branch, and pushed that new branch to a fork**, it can be turned into a pull request. A pull request can be accurately but minimally described as a list of topically focused commits.

The default behavior of a pull request is to include all of the commits on the current topic branch.  You can technically include a specific range of commits, but the default workflow is to always create specific branches and then make pull requests out of them.

Once again, the typical flow here is:

1. On GitHub, fork a repo to your account.
2. `git clone` this repo locally.
3. **Check out a new branch for your modifications.**
4. Add, commit, and push back to master.  [TODO: master or origin?]
5. Make a pull request on GitHub.

See more: GitHub - [About pull requests](https://help.github.com/articles/about-pull-requests/)

### Keep Up with Upstream

If you want to merge in the target branch to make your Pull Request mergeable, you would add the original repository as a new remote, fetch from it, merge the main branch of that repository into your topic branch, fix any issues and finally push it back up to the same branch you opened the Pull Request on.

## Creating a Git Repository

When you click "New repository" in GitHub and add a README, .gitignore, or LICENSE, this will automatically create a commit in origin.

Say that you already have a local repo that you want to add.  If you do the below, note that it will ask you to merge since origin/master now techically has a merge conflict with your master.

From your local repo, run:

```bash
$ git remote add origin git@github.com:bsolomon1124/my-repo.git
$ git push -u origin master
```

## Types of Accounts

GitHub has four types of account and plan combinations:

1. Free personal
2. Paid personal
3. Free organization
4. Paid organization

GitHub Organizations provide ownership of repositories at a higher level than mere user accounts.

## RESTful API

See the [REST API v3 Guide](https://developer.github.com/v3/).

# Glossary

See also: `git help glossary`.

| Term | Definition |
| ---- | ---------- |
| Heads | |
| HEAD | The latest commit (version) in the current branch.  When you change branches, HEAD is updated to refer to the new branch’s latest commit.  "`master HEAD`" or "`HEAD` of `master`" are two terms you may see used. |
| Working tree | The directory where your alter your project's actual files. It is also the location where your repository has been checked out. |
| Index |
| Master |
| Origin |
| Upstream |
| Staging area | See _Index_.
| Working directory | See _working tree_.  Prefer to use _working tree_ over this term, which could be confused with _current directory_. |

# Other

## Undoing Things

### Revise a Commit

To redo a commit with additional cahnges you forgot, use `git commit --amend`. If you've made no changes since your last commit (for instance, you run this command immediately after your previous commit), then your snapshot will look exactly the same, and all you'll change is your commit message.

Example:

```bash
$ git commit -m 'initial commit'
$ git add forgotten_file
$ git commit --amend
```

### Unstage a Staged File

Let’s say you've changed two files and want to commit them as two separate changes, but you accidentally type `git add *` and stage them both. How can you unstage one of the two?

Use `git reset HEAD <file>...`.  Just be careful with `git reset`; it can be dangerous when used with `--hard`.

### Unmodifying a Modified File

Separately from the above, if you want to undo changes, use `git checkout -- <file>...`.

This reverts it back to what it looked like when you last committed (or initially cloned, or however you got it into your working directory).

## `git show`

`git show` shows info on one or more objects (blobs, trees, tags and commits).

If you run `git show` without an explicit commit number, it simply shows the details of the most recent commit.

Or, you can explicitly pass a commit or other object:

```bash
 myrepo$ git show 23a8fbbc5d75e77e322b3357135e6e43788f7bf9
commit 23a8fbbc5d75e77e322b3357135e6e43788f7bf9 (contact-form)
Author: Brad Solomon <brad.solomon.1124@gmail.com>
Date:   Sat May 12 16:22:17 2018 -0400

    delete myname.py

diff --git a/myname.py b/myname.py
deleted file mode 100644
index 8e3c88a..0000000
--- a/myname.py
+++ /dev/null
@@ -1,5 +0,0 @@
-# myname.py
-import hello
-
-hello.main()
-print('My name is Brad.')
```

## Git Setup & Configuration

`git config` is used to get and set **repository or global options**.

- A project's `.git/config` houses repo-specific configuration settings manipulated with the `--file` option or by default. These settings have the highest precedence.
- `~/.gitconfig` is home to global user-specific configuration settings manipulated with the `--global` option.

Below, some have already been set.  To list all:

```bash
 ~$ git config --global -l
user.email=brad.solomon.1124@gmail.com
user.name=Brad Solomon
core.editor='/Applications/Sublime Text.app/Contents/SharedSupport/bin/subl' --wait --new-window
credential.helper=osxkeychain
color.ui=true
```

To set a few:

```bash
$ git config --global user.name "[name]"  # name & email attached to commits
$ git config --global user.email "[email address]"
$ git config --global color.ui true  # enable colorization
$ git config --global credential.helper osxkeychain  # save pw/login
```

Because the configuration files are simple text files, you can view their contents with `cat` and edit them with your favorite text editor, too.

```bash
 myrepo$ cat .git/config
[core]
    repositoryformatversion = 0
    filemode = true
    bare = false
    logallrefupdates = true
    ignorecase = true
    precomposeunicode = true
```

## Signing Your Work

TODO - See https://git-scm.com/book/en/v2/Git-Tools-Signing-Your-Work

## Plumbing Commands

Here are two plumbing commands to see what `HEAD` looks like:

```bash
 myrepo$ git cat-file -p HEAD
tree 56acc7ebf613f0b37987ad8e2697abc7b7f65ce4
parent 75a73f71b40cb5e3ab23c99c938f873ae0075bf6
author Brad Solomon <brad.solomon.1124@gmail.com> 1526170497 -0400
committer Brad Solomon <brad.solomon.1124@gmail.com> 1526170497 -0400

let's try this again

 myrepo$ git ls-tree -r HEAD
100644 blob 2a03b7619a92d24aae954392bd6769e26c7a72e3    .gitignore
100644 blob 436a25cc9958a7339e7da0456e597cc337707012    file1.txt
100644 blob e69de29bb2d1d6434b8b29ae775ad8c2e48c5391    headers.txt
100644 blob 8dc5777a0edb746aecdd764e3bda91ea6059b2e2    hello.py
```

## Commit Guidelines

See the ["Submitting Patches"](https://github.com/git/git/blob/ccdcbd54c4475c2238b310f7113ab3075b5abc9c/Documentation/SubmittingPatches#L101) page from the documentation, or  [here](https://tbaggery.com/2008/04/19/a-note-about-git-commit-messages.html) is a "model Git commit messsage."

## GUIs

- **gitk** is a git GUI.  Note that you must be in a git repo directory to use.
- [**Tower**](https://www.git-tower.com/mac/) and [**GitX**](http://gitx.frim.nl/) are two alternate GUIs.
- **GitHub for Desktop**: https://desktop.github.com/.

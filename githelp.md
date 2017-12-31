# Contents
- [TODO](#xxx)

# Resources & references
Ordered by ascending difficulty/assumed familiarity level.

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

## Intermediate
- Nick Farina: [Git is Simpler Than You Think](http://nfarina.com/post/9868516270/git-is-simpler)
- Tom Preston-Werner: [The Git Parable](http://tom.preston-werner.com/2009/05/19/the-git-parable.html)
- Scott Chacon/Ben Straub - [Pro Git](https://book.git-scm.com/book/en/v2)
- Linux conference: [Git for Ages 4 and Up](https://www.youtube.com/watch?v=1ffBJ4sVUb4)
- [GitHub Help](https://help.github.com/)
- Mark Lodato:
    - [A Visual Git Reference](http://marklodato.github.io/visual-git-guide/index-en.html)
    - [Visualizing Git with D3](http://onlywei.github.io/explain-git-with-d3/#)
- Neo: [Git Immersion Training](http://gitimmersion.com/)

## Advanced
- Sam Livingston-Gray: [Think Like (a) Git](http://think-like-a-git.net/epic.html)
    - Video of Sam's [presentation](http://confreaks.tv/videos/cascadiaruby2011-think-like-a-git)
- The Git docs [reference manual](https://git-scm.com/docs)
- Ryan Tomayko: [The Thing About Git](https://tomayko.com/blog/2008/the-thing-about-git)
- Scott Chacon: [Git Internals](https://github.com/pluralsight/git-internals-pdf/releases)

## Software
- [GitX](http://gitx.frim.nl/)
- [Tower](https://www.git-tower.com/mac/)

## Graph theory
- ["Algorithm" is not a !@%#$@ 4-Letter Word](http://www.jamisbuck.org/presentations/rubyconf2011/index.html), RubyConf 2011 slides by Jamis Buck
- [Wikipedia](https://en.wikipedia.org/wiki/Graph_theory)

# Version control systems
You can think of a version control system (short: "VCS") as a kind of "database". It lets you save a snapshot of your complete project at any time you want.  Version control is independent of the kind of project/language you're working with.

<img src="https://www.git-tower.com/learn/content/01-git/01-ebook/en/01-command-line/02-basics/01-what-is-version-control/what-is-vcs.png" alt="version_control.png" width="750"/>

## File states in git
There are three main states that your files can reside in:

1. **Modified** means that there's been changes to the file but it's not committed yet.  This isn't a git command; when you manually edit any file in a git repo, you're modifying it.
2. **Staged** means that you have marked a file to go into your next commit snapshot.  Changes you make to files get marked in "chunks" or stages, and you decide how intermittently to take a snapshot of those changes.
3. **Committed** means that the changes you made have been stored/documented.

A fourth _step_ (not a stage) is to **push** the commit back up to GitHub.

## Git trees
Your local repository consists of three "trees" maintained by git.
1. Your **Working Directory**, which holds the actual files.
2. The **Index**, which acts as a staging area.
3. The **HEAD**, which points to the last commit you've made.

## A golden rule of version control
A single commit should only wrap related changes: fixing two different bugs should produce (at the very least) two separate commits.  When crafting a commit, it's very important to only include changes that belong together. You should never mix up changes from multiple, different topics in a single commit.

# The git workflow
`git status` shows the **current working tree status.**  Two useful flags:
- `-s` - Give the output in the short-format.
- `-b` - Show the branch and tracking info even in short-format.

Try checking our status before we have made any changes.

```bash
dsp $ git status
On branch master
Your branch is up-to-date with 'origin/master'.

nothing to commit, working tree clean
```

```bash
dsp $ git status -sb  # not telling us much at all
## master...origin/master
```

Now let's modify a file (or two) in our repo in whatever text editor and rerun the above:

```bash
dsp $ git status
On branch master
Your branch is up-to-date with 'origin/master'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

    modified:   05a-python.md
    modified:   statistics/5-1-blue_men.md

Untracked files:
  (use "git add <file>..." to include in what will be committed)

    .DS_Store

no changes added to commit (use "git add" and/or "git commit -a")
```
```bash
dsp $ git status -sb
## master...origin/master
 M 05a-python.md
 M statistics/5-1-blue_men.md
?? .DS_Store
```

This means that you have **modified** the files that appear there. This is what is called the **staging** area. Any files you modify will appear here.

One benefit of having a staging area is that a developer may only want to commit a subset of all modified files.

As indicated in the output for `git status`, the next step is to use `git add <file>...`.  This updates _what will actually be committed._  You can add all files by typing `$ git add .`, or you can add one by one by specifying the path after `$ git add`.

This also accepts wildcards: `$ git add new-page.html index.html css/*` would add all files in `css/`.

In other words, `git add` **snapshots the file in preparation for versioning.**

> The "index" holds a snapshot of the content of the working tree, and it is this snapshot that is taken as the contents of the next commit. Thus after making any changes to the working tree, and before running the commit command, you must use the `add` command to add any new or modified files to the index.

Let's add our modified files to the index:

```bash
dsp $ git add .
dsp $ git status
On branch master
Your branch is up-to-date with 'origin/master'.

Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

    new file:   .DS_Store
    modified:   05a-python.md
    modified:   statistics/5-1-blue_men.md
```

Changes are now ready to be `commit`ted.  What does `git commit` do?
- It records changes to the repository, storing the current contents of the index in a new commit along with a log message from the user describing the changes.
    - Specifically, the changes are committed to HEAD.
- `git add` can be used repeatedly in between commits and incrementally adds changes to the index before committing.

The message should be descriptive enough, but also short and sweet.

```bash
dsp $ git commit -m 'update 05a-python & 5-1-blue_men'
[master d43a48d] update 05a-python & 5-1-blue_men
 3 files changed, 46 insertions(+), 47 deletions(-)
 create mode 100644 .DS_Store
 ```

Once you're done with the challenge, it's time to show your work in your remote GitHub repository. Let's git push.  The `git push` command uploads all the new commits from our current HEAD branch to its remote counterpart branch.

```bash
dsp $ git push origin master
git: 'credential-osxkeychain' is not a git command. See 'git --help'.
Username for 'https://github.com': bsolomon1124
Password for 'https://bsolomon1124@github.com':
git: 'credential-osxkeychain' is not a git command. See 'git --help'.
Counting objects: 6, done.
Delta compression using up to 4 threads.
Compressing objects: 100% (6/6), done.
Writing objects: 100% (6/6), 966 bytes | 966.00 KiB/s, done.
Total 6 (delta 4), reused 0 (delta 0)
remote: Resolving deltas: 100% (4/4), completed with 4 local objects.
To https://github.com/bsolomon1124/dsp.git
   dcd4394..d43a48d  master -> master
```

The `push` command tells Git where to put our commits when we're ready, and now we're ready. `push` pushes our local changes to our origin repo (on GitHub).  By default, `git push` expects us to provide it with two things:
1. To which remote repository we want to push. (`origin`);
2. To which branch on that remote repository we want to push (`master`).

The name of our remote is `origin` and the default local branch name is `master`. The `-u` flag tells Git to remember the parameters, so that next time we can simply run `git push` and Git will know what to do.

Your work should now show up in your remote repository.

As a side note, we can use `git remote -v` (where v=verbose) to see what our _remotes_ our.  _Remotes_ is another term for a _set of repositories whose branches you're tracking._  Here _fetch_ is synonymous with _pull_:

```bash
dsp $ git remote -v
origin  https://github.com/bsolomon1124/dsp.git (fetch)
origin  https://github.com/bsolomon1124/dsp.git (push)
```

To restate the above:
> - A "local" repository resides on your local computer, as a ".git" folder inside your project's root folder. You are the only person that can work with this repository, by committing changes to it.
> - A "remote" repository, in contrast, is typically located on a remote server on the internet or in your local network. No actual working files are associated with a remote repository: it has no working directory but it exclusively consists of the ".git" repository folder. Teams are using remote repositories to share & exchange data: they serve as a common base where everybody can publish their own changes and receive changes from their teammates.

The `git remote` command has several different possible syntaxes.  One of them is:

> `git remote add [-t <branch>] [-m <master>] [-f] [--[no-]tags] [--mirror=<fetch|push>] <name> <url>`

`git remote add` allows us to _add a remote repository_ to our list set of remotes.  This command takes a **remote name** and a **repository URL**, which in the case of "15 Minutes to Git" is is https://github.com/try-git/try_git.git.

```bash
octobox $ git remote add origin https://github.com/try-git/try_git.git
octobox $ git remote -v
origin  https://github.com/try-git/try_git.git (fetch)
origin  https://github.com/try-git/try_git.git (push)
```

# The above in reverse
What if we edit the files in GitHub?  Can we have this change our files locally?  Let's try making a small "direct" edit to

`https://github.com/bsolomon1124/dsp/edit/master/00b-fork_repo.md`

while adding a commit message and then clicking "commit changes."

These changes _will not_ be immediately reflected in your local machine repo.  How do we get them to be reflected?

```bash
dsp $ git pull
remote: Counting objects: 3, done.
remote: Compressing objects: 100% (3/3), done.
remote: Total 3 (delta 2), reused 0 (delta 0), pack-reused 0
Unpacking objects: 100% (3/3), done.
From https://github.com/bsolomon1124/dsp
   d43a48d..a51a4c6  master     -> origin/master
Updating d43a48d..a51a4c6
Fast-forward
 00b-fork_repo.md | 2 +-
 1 file changed, 1 insertion(+), 1 deletion(-)
 ```

If you open this file locally, you'll see that it now reflects the changes from GitHub.

# Git init
`git init` creates an empty Git repository - basically a .git directory with subdirectories for objects, refs/heads, refs/tags, and template files. An initial HEAD file that references the HEAD of the master branch is also created.

Note that this initial repository is truly _empty_.  Git did _not_ add the current content of your working copy as something like an "initial version". The repository contains not a single version of your project, yet.

You have two options to get a local repository onto your machine: you can either create a new one through `git init` or clone from an existing remote repository.

Example:

```bash
python $ mkdir octobox
python $ cd octobox/
octobox $ ls  # empty
octobox $ git init
Initialized empty Git repository in /Users/brad/Scripts/python/octobox/.git/
octobox $ ls -a
.   ..  .git
```

Some related terminology is the term **working copy**.  The root folder of your project is often called the "working copy" (or "working directory"). It's the directory on your local computer that contains your project's files.

This leads us to a very basic question: what is a repository?

> Think of a repository as a kind of database where your VCS stores all the versions and metadata that accumulate in the course of your project. In Git, the repository is just a simple hidden folder named ".git" in the root directory of your project.

If we create an empty file, its status **untracked.**  (Slightly different than the `.md` files above.)

```bash
octobox $ touch octocat.txt
octobox $ ls
octocat.txt
octobox $ git status -sb
## No commits yet on master
?? octocat.txt
```

To tell Git to start tracking changes made to octocat.txt, we first need to add it to the staging area by using `git add`.

```bash
octobox $ git add octocat.txt
octobox $ git status -sb
## No commits yet on master
A  octocat.txt
```

# Pulling
Let's pretend some time has passed. We've invited other people to our GitHub project who have pulled your changes, made their own commits, and pushed them.

We can check for changes on our GitHub repository and pull down any new changes by running:

```bash
$ git pull origin master
```

In other words, pulling _updates our local repository to reflect changes/commits made in the remote repo_.

# History
Think of Git's `log` as a journal that remembers all the changes we've committed so far, in the order we committed them:

```bash
$ git log
```

With some fancy flags, to see an ASCII art tree of all the branches, decorated with the names of tags and branches:

```bash
dsp $ git log --graph --oneline --decorate --all
```

By default, with no arguments, `git log` lists the commits made in that repository in reverse chronological order — that is, the most recent commits show up first. As you can see, this command lists each commit with its SHA-1 checksum, the author’s name and email, the date written, and the commit message.

# Branching
Branches are used to develop features isolated from each other. The **master** branch is the "default" branch when you create a repository. Use other branches for development and merge them back to the master branch upon completion.

A branch represents a (sub-) **context** within a project.

In real-world projects, work always happens in multiple of these contexts in parallel:

- While you're preparing 2 new variations of your website's design (context 1 & 2)...
- you're also trying to fix an annoying bug (context 3).
- On the side, you also update some content on your FAQ pages (context 4).

All the changes you make at any time will only apply to the _currently active_ branch; all other branches are left untouched. This gives you the freedom to both work on different things in parallel.

Branches are not "optional" in Git.  You are always working on a certain branch (the **currently active**, or "checked out", or "HEAD" branch).

So, which branch is HEAD at the moment? `git status` tells us in its first line of output,

```bash
On branch master
```

Creating a new branch: Based on the project's current state, we create a new branch and name it "contact-form":

```bash
$ git branch contact-form
```

Using `git branch -v` (verbose) lists all of our branches:

```bash
octobox $ git branch -v
  contact-form 3b0ad2d add cute octocat story
* master       3b0ad2d add cute octocat story
```

You can see that our new branch "contact-form" was created and is based on the same version as "master". Additionally, the little asterisk character (\*) next to "master" indicates that this is our current HEAD branch. To emphasize this: the "git branch" command only created that new branch - but it didn't make it active.

To make another branch (say, "contact-form") active, use `git checkout`. This does two things for you:
1. It makes "contact-form" the current HEAD branch.
2. It replaces the files in your working directory to match exactly the revision that "contact-form" is at.

# Cloning a repo
This makes a copy of the repository in your laptop. Click on the clipboard image on the right sidebar to copy the HTTPS clone URL:

![git_clone](../imgs/git_clone.png)

Create the following folders: `~Scripts/python/metis/metisgh/prework`.

Using terminal:

```bash
$ pwd
/Users/brad/Scripts/python/
$ mkdir -p metis/metisgh/prework/
```

Navigate in your terminal to the folder you just created. Type `git clone` and then paste the clone URL.

```bash
$ git clone https://github.com/your_username/dsp.git
```

Cloning the directory will create the following:

`~/Scripts/python/metis/metisgh/prework/dsp`

And now `cd` into the `/dsp` folder.

This directory contains not only the downloaded material but also a `.git` subfolder.  **This is central to version control!**

When you clone a repository from a remote server, Git automatically remembers this connection for you. It saves it as a remote called "origin" by default.

# Other

## Git setup & configuration
`git config` is used to get and set repository or global options.

Here, some have already been set.  To list all:

```bash
octobox $ git config -l  # or -list
http.sslverify=true
http.sslcapath=/Applications/anaconda3/ssl/cacert.pem
http.sslcainfo=/Applications/anaconda3/ssl/cacert.pem
user.email=brad.solomon.1124@gmail.com
user.name=Brad Solomon
core.editor='/Applications/Sublime Text.app/Contents/SharedSupport/bin/subl' --wait --new-window
credential.helper=osxkeychain
core.repositoryformatversion=0
core.filemode=true
core.bare=false
core.logallrefupdates=true
core.ignorecase=true
core.precomposeunicode=true
```

To set a few:

```bash
$ git config --global user.name "[name]"  # name & email attached to commits
$ git config --global user.email "[email address]"
$ git config --global color.ui true  # enable colorization
```

## Access permission to cloned repos
When you `git clone` a url, Git will download a complete copy of this repository to your local disk - on condition that you're allowed to access this repository.

- For the "http" and "git" protocols, no access rights are necessary.
- For "https" URLs, you might need a username and a password.
- For "ssh" URLs (either with a leading "ssh://" or, with the shorter form, "user@server..."), you'll have to use "SSH Public Key" authentication. While being very safe, efficient, and widely used, it's also a little bit of work to set up.

### Authentication with SSH public keys
Secure Shell (SSH) is a network protocol for operating network services securely over an unsecured network.

Authentication with SSH uses a two-part key: a public and a private one.

The public key should be installed on all servers to which you want access.  When a connection via SSH is trying to be established, the server will only grant access if it has a public key installed that matches the private key of the requesting computer.

First, check that you do not already have a public key (in your home folder): `$ ls ~/.ssh`  If you don't have one, create one; you can press ENTER to default to the given paths:

```bash
~ $ ssh-keygen -t rsa -C "brad.solomon.1124@gmail.com"
Generating public/private rsa key pair.
Enter file in which to save the key (/Users/brad/.ssh/id_rsa):
Created directory '/Users/brad/.ssh'.
Enter passphrase (empty for no passphrase):
Enter same passphrase again:
Your identification has been saved in /Users/brad/.ssh/id_rsa.
Your public key has been saved in /Users/brad/.ssh/id_rsa.pub.
The key fingerprint is:
SHA256:sX+gTtYe4T60QmV1V7g0H+RniRwC5fpd97PYN86moBI brad.solomon.1124@gmail.com
The key's randomart image is:
+---[RSA 2048]----+
|         .oo ..oo|
|          . + O.o|
|        .  o = B+|
|         o+   ..o|
|        S+o    ..|
|       E.=oo. . o|
|       .=.=+.. ..|
|       =.o+o. +o+|
|        ooo. o+=o|
+----[SHA256]-----+
```

Now, two files will have been created for you: "id_rsa.pub" (your public key) and "id_rsa" (your private key), both located at _~./ssh/_  You'll need to upload the output of id_rsa.pub to your GitHub to interact with SSH (rather than https).  To copy the contents:

```bash
pbcopy < ~/.ssh/id_rsa.pub
```

## GitHub Gist
[TODO]

## `.gitignore`
Typically, in every project and on every platform, there are a couple of files that you don't want to be version controlled: on Mac OS, e.g., those pesky ".DS_Store" files aren't worth versioning.

A helpful compilation of ignore rules for different projects and platforms can be found here: github.com/github/gitignore.

The list of files to ignore is kept in a simple file called ".gitignore" in the root folder of your project. It's highly recommended to **define this list at the very beginning of your project - before making your first commit**. Because once files are committed, you'll have to jump through some hoops to get them out of version control, again.

## `git rm`
`rm` is _remove_.  Remove files from the index, or from the working tree and the index.  If you've deleted a file completely from your project, you'll want to use this and pass the file name to add its deletion to the staging area.

## GUIs
gitk is a builtin git GUI:

```bash
$ gitk
```

Note that you must be in a repo directory to use.

Tower is an alternate GUI: https://www.git-tower.com/mac/.

GitHub for desktop: https://desktop.github.com/.

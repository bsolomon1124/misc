# Contents
- [xxx](#xxx)

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

## Software (TODO)
- GitX
- Tower

## Graph theory
- ["Algorithm" is not a !@%#$@ 4-Letter Word](http://www.jamisbuck.org/presentations/rubyconf2011/index.html), RubyConf 2011 slides by Jamis Buck
- [Wikipedia](https://en.wikipedia.org/wiki/Graph_theory)

## Other:

# Version control systems

There are three main states that your files can reside in:

1. **Modified** means that there's been changes to the file but it's not committed yet.  This isn't a git command; when you manually edit any file in a `git` repo, you're modifying it.
2. **Staged** means that you have marked a file to go into your next commit snapshot.  Changes you make to files get marked in "chunks" or stages, and you decide how intermittently to take a snapshot of those changes.
3. **Committed** means that the changes you made have been stored locally. [?]

A fourth _step_ (not a stage) is to **push** the commit back up to GitHub.

`git status` shows the **current working tree status.**  Two flags:
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

# Background

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

# GitHub Gist


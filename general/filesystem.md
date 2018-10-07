# Mac OSX: File System

## Contents

- [Resources & References][2]
- [About This Guide][3]
- [The Filesystem Hierarchy Standard (FHS)][4]
    - [Rationale][5]
- [The MacOS File System][6]
- [Default `$PATH`][7]
- [High-Level Layout, Unannotated][8]
- [Detailed File System Layout][9]
- [More on `/usr/`][10]
- [Difference Between `/sbin/`, `/usr/sbin/`, and `/usr/local/sbin`][11]
- [A Note on Applications][12]

[2]: #resources--references
[3]: #about-this-guide
[4]: #the-filesystem-hierarchy-standard-fhs
[5]: #rationale
[6]: #the-macos-file-system
[7]: #default-path
[8]: #high-level-layout-unannotated
[9]: #detailed-file-system-layout
[10]: #more-on-usr
[11]: #difference-between-sbin-usrsbin-and-usrlocalsbin
[12]: #a-note-on-applications

## Resources & References

- Apple Developer: [File System Programming Guide](https://developer.apple.com/library/content/documentation/FileManagement/Conceptual/FileSystemProgrammingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010672)
- Linux Foundation: [Filesystem Hierarchy Standard, v 3.0](http://refspecs.linuxfoundation.org/fhs.shtml)
- `man` pages:
    - [`file-hierarchy`](http://man7.org/linux/man-pages/man7/file-hierarchy.7.html)
    - [`hier`](http://man7.org/linux/man-pages/man7/hier.7.html)

_Note_: these two man pages appear to be for version 2.0 of the FHS.

## About This Guide

The complete file system on a modern Mac has two major components: the **traditional filesystem hierarchy** as specified by the Filesystem Hierarchy Standard (FHS), and the **MacOS file system**.

This directory doesn't cover _everything_--just a curated list of relevant directories and what their purposes.

## The Filesystem Hierarchy Standard (FHS)

The Filesystem Hierarchy Standard (FHS) is a reference describing the conventions used for the layout of a UNIX system.  It defines directory structure and contents.

The latest version is 3.0, released on 3 June 2015.

The directories in this category (`bin/`, `/sbin`, etc) are inherited from traditional UNIX installations. They are an important part of the system’s BSD layer but are more useful to software developers than end users.

See also: `man 7 hier`.

### Rationale

The design of FHS is built around two independent distinctions among files:

- shareable vs. unshareable
- variable vs. static

**Single-user** mode is another important concept.  This the case where no other filesystems are mounted.

A **configuration file** is a local file used to control the operation of a program; it must be static and cannot be an executable binary.

## The MacOS File System

Typically, MacOS-specific directories under root (`/`) are capitalized, while FHS directories are lowercase.

One important directory is `/Users/<yourname>/`, which takes the place of the traditional Unix `/home/`.  The directories within are the "public user experience"--made for non-developers looking to store everyday files.

## Default `$PATH`

The default $PATH is set from `/etc/paths`:

```bash
$ cat /etc/paths
/usr/local/bin
/usr/bin
/bin
/usr/sbin
/sbin
```

It then checks `/etc/paths.d` and appends those also.  (In my case, `/usr/local/go/bin`.)

See `man path_helper`.

## High-Level Layout, Unannotated

Here's an "abridged" tree of my machine:

```
# FHS
/
/bin/                       bash, cat, chmod, echo, kill, launchctl, ls, mkdir, mv, pwd, rm, sh, test
/dev/
├── fd/
├── null
├── stderr@ -> fd/2
├── stdin@ -> fd/0
└── stdout@ -> fd/1
/etc/ -> private/etc
├── bashrc
/private/
├── etc/
├── tmp/
└── var/
/sbin/                      ifconfig, mount, reboot, shutdown
/tmp/ -> private/tmp
/usr/
├── bin/                    awk, cal, cd, clear, curl, grep, less, open, python, ssh, vim, zip
├── lib/
├── local/
│   ├── bin/
│   ├── Cellar/
│   ├── Homebrew/
│   └── sbin/
└── sbin/
/var/ -> private/var

# MacOS File System
/Applications/
└── Utilities/
/Users/
└── brad/
    ├── .local/
    │   ├── bin/
    ├── bin/
    ├── Applications/
    ├── Desktop/
    ├── Documents/
    ├── Downloads/
    ├── Library/
    ├── Movies/
    ├── Music/
    ├── Pictures/
    ├── Public/
    └── Sites/
/System/
```

## Detailed File System Layout

_Directories in **_bold_** are part of `$PATH` by default._

FHS:

| Directory | Notes |
| --------- | ----- |
| `/` | Root directory of the entire filesystem. |
| **_`/bin`_** | `bin` stands for **binaries**.  These are essential user utilities fundamental to single-user mode. These are needed to bring the system up or repair it. They may be used by both system administrators and the user. |
| `/dev/` | `dev` stands for **device** files, such as mount points for attached hardware. A device file is an interface to a device driver that appears in a file system as if it were an ordinary file. |
| `/dev/fd/` | File descriptor files; see `man fd`.
| `/dev/null` | The null device, which discards all data written to it but reports that the write operation succeeded.  It may be called the bit bucket or black hole; it is typically used for disposing of unwanted output streams of a process, or as a convenient empty file for input streams. This is usually done by redirection. |
| `/dev/stderr@ -> fd/2` | Standard error, a symlink to file descriptor 2. |
| `/dev/stdin@ -> fd/0` | Standard input, a symlink to file descriptor 0. |
| `/dev/stdout@ -> fd/1` | Standard output, a symlink to file descriptor 1. |
| **_`/sbin/`_** | `sbin` stands for **system binaries**.  These are programs and administration utilities fundamental to both single-user and multi-user environments, normally used to boot the system.  They are not normally meant for normal users. |
| `/usr/` | "Non-essential" command-line binaries, libraries, header files, and other data.  Contains the majority of user utilities.  This is a **secondary hierarchy**; `/usr/` and its subdirectories are designed to hold **read-only user data**. This directory is usually mounted from a separate partition. |
| **_`/usr/bin/`_** | This is **the directory where most user commands are located.**  Most programs executed by normal users which are not needed for booting or for repairing the system and which are not installed locally should be placed in this directory. |
| `/usr/lib/` | Libraries for the binaries in `/usr/bin` and `/usr/sbin`.  A **library** is a collection of non-volatile resources used by computer programs, often for software development. These may include configuration data, documentation, help data, message templates, pre-written code and subroutines, classes, values or type specifications. |
| `/usr/libexec` | Internal binaries that are not intended to be executed directly by users or shell scripts. |
| `/usr/local/` | Contains executables, libraries, etc. not included by the basic operating system.  A **tertiary hierarchy** for local data, specific to this host. Typically has further subdirectories, e.g., `bin/`, `lib/`, `share/`.  Many modern UNIX systems install third party packages into `/usr/local/` while keeping code considered part of the operating system in `/usr/`. **Locally installed software must be placed within `/usr/local/` rather than `/usr` unless it is being installed to replace or upgrade software in `/usr`**. |
| **_`/usr/local/bin/`_** | Composed entirely of symblinks associated with Homebrew; the hard links themselves are in `/usr/local/Cellar`.|
| `/usr/local/Homebrew/` | Directory for the Homebrew manager program itself. |
| **_`/usr/sbin/`_** | System dameons and utilities executed by users. |
| `/private/` | -- |
| `/private/tmp/` | Temporary files.  These can be **deleted without notice**, either as the result of a job or system reboot. |
| `/private/var/` | Multi-purpose log, temporary, transient, and spool files. |
| `/private/etc/` | Host-specific system configuration files and scripts. Contains: `bashrc`, system-wide file for interactive `bash` shells. |

MacOS file system:

| Directory | Notes |
| --------- | ----- |
| `/Applications/` | Part of the Local domain.  Contains resources such as apps that are local to the current computer and shared among all users of that computer. |
| `/Applications/Utilities/` |  A subset of apps that are intended for use in managing the local system, such as `Terminal.app`. |
| `/Users/` | The User domain.  Contains one or more user home directories.  This takes the place of traditional Unix `/home/`. |
| `/Users/brad/` | The owner is brad, with `drwxr-xr-x+` access. |
| `/Users/brad/.local/bin/` | TODO |
| `/Users/brad//bin/` | A good place for small shell scripts designed for local use. |
| `/Users/brad/Applications/` | User-specific apps. |
| `/Users/brad/Desktop/` | The items on the user’s desktop. |
| `/Users/brad/Documents/` | User documents and files. |
| `/Users/brad/Downloads/` | Files downloaded from the Internet. |
| `/Users/brad/Public/` | Content the user wants to share.  Accessible by other users on the system.  (Other directories in `/Users/brad/` are not.) |
| `/System/` | System software installed by Apple.  Do not modify. |

## More on `/usr/`

This directory is large and nested, so deserves its [own section](http://refspecs.linuxfoundation.org/FHS_3.0/fhs/ch04.html).

`/usr` is the second major section of the filesystem. It is for shareable, read-only data. Any information that is host-specific or varies with time should be stored elsewhere.

## Difference Between `/sbin/`, `/usr/sbin/`, and `/usr/local/sbin`

(This also applies to `/bin/`, `/usr/bin/`, and `/usr/local/bin`.)

System binaries are utilities used for system administration (and other root-only commands)
- `/sbin` contains binaries essential for booting, restoring, recovering, and/or repairing the system in addition to the binaries in `/bin`.
- Programs executed after `/usr` is known to be mounted are generally placed into `/usr/sbin`.
- Locally-installed system administration programs should be placed into `/usr/local/sbin`.

## A Note on Applications

`<AppName>.app` is an app’s _bundle_ ("bundle container"). This directory contains the app and all of its resources.

For example:

```bash
[10:00:00 brad   ~]$ tree -L 3 /Applications/FaceTime.app/
/Applications/FaceTime.app/
└── Contents
    ├── Info.plist
    ├── MacOS
    │   └── FaceTime
    # ...
    ├── Resources
    │   ├── AppIcon.icns
    │   ├── Assets.car
    │   ├── Base.lproj
    │   ├── DFRCallParticipantViewController.nib
    │   ├── Dutch.lproj
    │   ├── English.lproj
    # ...
    └── version.plist
```

Above, `/Applications/FaceTime.app/Contents/MacOS/FaceTime` is the app itself.  To run the app, you could do either of:

```bash
open /Applications/FaceTime.app  # Option 1
/Applications/FaceTime.app/Contents/MacOS/FaceTime  # Option 2
```

# Contents
This walkthrough coveres two distinct subjects:
1. SQL as a language, geared specifically towards SQL as understood by the SQLite RDBMS;
2. The SQLite command-line interface, sqlite3.

# Resources & references
- SQLite [Home page](https://www.sqlite.org/index.html); some useful sections:
    - [Command Line Shell For SQLite](https://www.sqlite.org/cli.html)
    - [Books About SQLite](https://www.sqlite.org/books.html)
    - [SQL As Understood By SQLite](https://www.sqlite.org/lang.html)
    - [Core Functions](https://www.sqlite.org/lang_corefunc.html)
    - [Aggregate Functions](https://www.sqlite.org/lang_aggfunc.html)
    - [Date & Time Functions](https://www.sqlite.org/lang_datefunc.html)
    - [Data Types](https://www.sqlite.org/datatype3.html)
    - [Distinctive Features](https://www.sqlite.org/different.html)
- CodeAcademy: [list of SQL commands](https://www.codecademy.com/articles/sql-commands?r=master)
- [SQLiteStudio](https://sqlitestudio.pl/index.rvt) is a SQLite database manager
- [sqlitetutorial.net/](http://www.sqlitetutorial.net/)
- [Download SQL Server 2017 for Mac]()

# SQL overview

- SQL, 'Structured Query Language', is a programming language designed to manage data stored in relational databases. SQL operates through simple, declarative statements. This keeps data accurate and secure, and helps maintain the integrity of databases, regardless of size.
- The SQL language is widely used today across web frameworks and database applications. Knowing SQL gives you the freedom to explore your data, and the power to make better decisions. By learning SQL, you will also learn concepts that apply to nearly every data storage system.
- The statements covered in this course, use SQLite Relational Database Management System (RDBMS).

# Relational databases and how they are organized

- A relational database is a database that organizes information into one or more tables. Here the relational database contains one table.  It is essentially a **container to store organized data**.
- A table is a collection of data organized into rows and columns. Tables are sometimes referred to as relations. Here the table is celebs.
- A column is a set of data values of a particular type. Here id, name, and age are each columns.
- A row is a single record in a table.

# What is SQLite & sqlite3?
The SQLite project provides a simple command-line program named **sqlite3**.

sqlite3 allows the user to manually enter and execute SQL statements **against an SQLite database.**

SQLite is a relational database management system (RDBMS).  Other such RDBMSs are MySQL, PostgreSQL, Oracle, Microsoft SQL Server.

## Why SQLite?

- SQLite uses dynamic typing.  It does not enforce data type constraints. Data of any type can (usually) be inserted into any column.
- It is open-source, and free.
- Zero configuration.
- Not a client-server database engine. Rather, it is embedded into the end program.

# File extensions

- `.sqlite`, `.sqlite3`, `.db` - *binary* database files (don't view them in a text editor).  You use `.open <file>` on these.  `.db` and `.sqlite` extensions are functionally equivalent; `.sqlite` denotes a SQLite databse, while `.db` is used by Oracle and others.  The content itself is determined by a sequence of bytes; the first 100 bytes of the database file comprise the database file header.
- `.sql` - written in ASCII; commonly contains _queries _but could also _create tables_ themselves.

# Useful dot-commands (alphabetized)
This list is _not_ exhaustive; full list [here](https://www.sqlite.org/cli.html#special_commands_to_sqlite3_dot_commands_).

| Commmand | Use | Example |
| :------- | :-- | :------ |
| `.cd DIRECTORY` | Change the working directory to `DIRECTORY` | |
| `.databases` | List names and files of attached databases | |
| `.exit` or `.quit` | Exit sqlite3 | |
| `.headers on|off` | Turn display of headers on or off | |
| `.help` | Show all dot-commands. | |
| `.import FILE TABLE` | Takes 2 arguments.  Import data from `FILE` into `TABLE`.  `FILE` is the name of the disk file from which data is to be read.  It could be CSV data. `TABLE` is the name of the _table_ (not database) into which the file will be read.  Note with CSV data you may need to specify `.separator ,` first.  | `sqlite> .import C:/work/somedata.csv tab1` |
| `.mode` | Change output mode: one of `ascii column csv html insert line list quote tabs tcl` | |
| `.once (-e|-x|FILE)` | Output for the next SQL command only to `FILE`. | |
| `.open ?OPTIONS? ?FILE?` | Close existing database and reopen `FILE`; The `--new` option starts with an empty file.  This _uses a persistent disk file as the database._ | `sqlite> .open ex1.db`; `sqlite> .open tysql.sqlite teach` |
| `.output ?FILE?` | Send output to `FILE` or stdout.  Use `.output` with no arguments to begin writing to standard output (again). | |
| `.read FILENAME` | Execute SQL in `FILENAME` | |
| `.separator COL ?ROW?` | Change the column separator and optionally the row.  This is separator for both the output mode and `.import`. | `separator ,` |
| `.tables` | List names of tables | |
| `.width NUM1 NUM2 ...` | Set column widths for "column" mode; Negative values right-justify | |

# `import` versus `read` versus `open`

- `.import FILE TABLE`: Import data from `FILE` into `TABLE`.  Use this with delimited data, not `.sqlite` or `.db` files.
- `.read FILENAME`:  Execute SQL in `FILENAME`.
- `.open ?OPTIONS? ?FILE?`: This _uses a persistent disk file as the database._

```sql
sqlite> .read euro2012.sql  # This .sql doc creates 3 tables
sqlite> .tables
eteam  game   goal
```

```sql
sqlite> .cd /Users/brad/Scripts/sql/
sqlite> .open flights.db
```

# File I/O

## File input
Use the `.import` command to import CSV (comma separated value) data into an SQLite table. The `.import` command takes two arguments which are the name of the disk file from which CSV data is to be read and the name of the SQLite table into which the CSV data is to be inserted.

Note that it is important to set the `mode` to "csv" before running the `.import` command. This is necessary to prevent the command-line shell from trying to interpret the input file text as some other format.

Note with CSV data you may need to specify `.separator ,` first.

Example:

```sql
`sqlite> .import work/somedata.csv tab1`
```

## File output
Let's work with an example table:

```sql
sqlite> create table tbl1(one varchar(10), two smallint);
sqlite> insert into tbl1 values('hello!',10);
sqlite> insert into tbl1 values('goodbye', 20);
```

**Steps to write to CSV:**

First, set the "mode" to "csv":

```sql
sqlite> .mode csv
```

Optionally, the `.header on` line causes column labels to be printed as the first row of output.

```sql
sqlite> .header on
```

The line ".once FILENAME" causes all query output to go into the named file instead of being printed on the console.

```sql
sqlite> .once /Users/brad/Scripts/sql/dataout.csv
```

Then run a query to extract the desired rows of the table.  The output goes to wherever you specified with `.once`.

```sql
sqlite> SELECT * FROM tbl1;
```

Optionally, to open the file:

```sql
sqlite> .system open /Users/brad/Scripts/sql/dataout.csv
```

### Difference between `.once` and `.output`
These commands both redirect the output of queries.

- With `.once`, output is only redirected for the single next command before reverting to the console.
- Conversely, `.output` sends all subsequent query results to that `FILE`.

# Primary keys: required conditions

- No two rows can have the same primary key value
- Every row must have a primary key value (cannot be NULL)
- Values in primary key columns should never be modified or updated
- Primary key values should never be re-used if one row is deleted

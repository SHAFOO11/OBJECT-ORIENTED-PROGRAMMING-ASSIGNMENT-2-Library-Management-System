# Library Management System

BIT1123 Object Oriented Programming — Assignment 2 (Group), 20%

A Java console application for managing a small library: registering members and
librarians, cataloging books and DVDs, borrowing and returning items with automatic
late-fee calculation, searching the catalog, and saving/loading data to a file.

## Group Members

| No. | Name                          | Student ID    | Program |
|-----|-------------------------------|---------------|---------|
| 1   | Ali Sharif Abdulkadir Sharif  | 202505010493  | BCSSE   |
| 2   | bawazir bandar khaled salem   | 202401010116  | BCSSE   |
| 3   | Ali Yousef Jalal Abdo         | 202401010131  | BIT     |
| 4   | Ahmed Mohammed Fadul Mohammed | 202401010432  | BCSSE   |
| 5   | Ali Ali Isak                  | 202401010128  | BIT     |

## Project Structure

```
src/
  Person.java       Abstract base class (name, id, contactNumber)
  Member.java        extends Person
  Librarian.java      extends Person
  LibraryItem.java  Abstract base class (itemId, title, available)
  Book.java           extends LibraryItem
  DVD.java            extends LibraryItem
  Loan.java         Association class linking a Member and a LibraryItem
  Library.java      Controller class (registration, borrowing, search, save/load)
  Main.java         Console entry point (menu-driven)
```

## OOP Concepts Demonstrated

- **Encapsulation** — all fields are private, accessed only through getters/setters
- **Inheritance** — `Member`/`Librarian` extend `Person`; `Book`/`DVD` extend `LibraryItem`
- **Polymorphism** — late fees and summaries are resolved at runtime through superclass references
- **Abstraction** — `Person` and `LibraryItem` are abstract classes with abstract methods

## How to Compile and Run

```bash
javac -d out src/*.java
java -cp out Main
```

## Contributors

<!-- GitHub usernames to be added here once provided by each group member -->

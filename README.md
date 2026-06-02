# Lab 14 – Anime Watchlist Tracker
## Student Name
Luka Kelly
---
## Project Description
This project is a simple Anime Watchlist Tracker created using Python.
The program stores anime information such as title, genre, and watching status. This project uses basic
Object-Oriented Programming concepts, including class, object, attributes, and methods.
---
## Technologies Used
- Python
- Git
- GitHub
- Visual Studio Code
---
## Features
The Anime Watchlist Tracker can:
- Store anime title
- Store anime genre
- Store watching status
- Display anime information
- Update anime watching status
- Store multiple anime objects in a list
- Display anime objects using a loop
---
## How to Run the Program
1. Open the project folder in VS Code.
2. Open the terminal.
3. Run the following command:
```bash
python anime_watchlist.py
```
If `python` does not work, try:
```bash
py anime_watchlist.py
```
---
## OOP Concepts Used
### Class
The class used in this project is:
```text
Anime
```
The class is used as a blueprint for creating anime objects.
### Object
Objects are created from the `Anime` class.
Example objects may include:
```text
anime1
anime2
anime3
```
### Attributes
The attributes used in this project are:
- title
- genre
- status
### Methods
The methods used in this project are:
- display_info()
- update_status()
---
## Git and GitHub Questions
### 1. What is Git?
A tool to track changes to code
### 2. What is GitHub?
A website to use Git
### 3. What is a commit?
A commit is saving changes to code
### 4. What is a branch?
A place to work on code without needing to change the main code
### 5. Why do programmers use Git and GitHub?
It makes it easy to track changes to code and see previous versions
---
## OOP Planning Questions
### 1. What class will you create?
Anime
### 2. What attributes will your class have?
- Title
- Genre
- Status
### 3. What methods will your class have?
- display_info()
- update_status()
### 4. How many anime objects will you create?
I will create three anime objects
### 5. Why is this project an example of Object-Oriented Programming?
It uses classes, methods and objects
---
## Sample Output
=== Watchlist ===
Title: Demon Slayer
Genre: Action
Status: Watching
Rating: 3/5
Update status?: no
No status updated
=== Watchlist ===
Title: Spy X Family
Genre: Comedy
Status: Completed
Rating: 3/5
Update status?: yes
Updating Status...
Enter 'Watched', 'Watching', or 'Waiting': Waiting
=== Watchlist ===
Title: Spy X Family
Genre: Comedy
Status: Waiting
Rating: 3/5
=== Watchlist ===
Title: Haikyuu
Genre: Sports
Status: Waiting
Rating: 3/5
Update status?: no
No status updated
---
## Reflection
### 1. What did you learn about Git?
I learned how to commit through the terminal
### 2. What did you learn about GitHub?
It is able to be connected to VS Code for easier commits
### 3. What did you learn about Python classes?
You can have a list connected to a class to display objects
### 4. What was the hardest part of this lab?
Using the correct git commands
### 5. What improvement did you add to your anime system?
I added ratings out of 5

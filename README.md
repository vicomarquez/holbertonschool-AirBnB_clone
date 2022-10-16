# AirBnB Clone - The Console Project for Holberton School

![AirBnB clone](https://camo.githubusercontent.com/a0c52a69dc410e983b8c63fa4aa57e83cb4157cd/68747470733a2f2f73332e616d617a6f6e6177732e636f6d2f696e7472616e65742d70726f6a656374732d66696c65732f686f6c626572746f6e7363686f6f6c2d6869676865722d6c6576656c5f70726f6772616d6d696e672b2f3236332f4842544e2d68626e622d46696e616c2e706e67)

## Project's Description

In this project we are going to start the first phase towards creating a web application of an AirBnB which is 'The console'. The console is a command interpreter to handle objects. This is a very important instance because we are using everything that we learnt about python to create a website. We also learnt how to serialize (converting python objects to json string representation) and deserialize (converting the json representation to objects), whic are two important processes to work with nowadays.

## Console Commands

| Command | Function |
| ------ | ------ |
| quit | exits the program |
| create | creates a new instance, saves it and prints the id|
| show | prints the string representation of an instance based on the classname and id |
| destroy | deletes an instance based on the class name and id  |
| all | prints all string representation of all instances based or not on the class name|
| update | updates an instance based on the class name and id by adding or updating attribute |

## How to use the console

First of all, you will need to clone this repository.
After that, you can start using the console this way:

#### Start the console

```sh
./console.py
```
#### Create a User object

```sh
(hbnb) create User
```
#### Display a specific object

```sh
(hbnb) show User [object id]
```

#### Display all objects or all objects of a specific class

```sh
(hbnb) all
```
or
```sh
(hbnb) all User
```

## Execution

This console works like this in interactive mode:
```sh
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```

And also in non-interactive mode:
```sh
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```

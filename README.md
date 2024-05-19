# AirBnB Clone - The Console

This project is a simple clone of the AirBnB console. The console is a command interpreter that allows you to create, update, destroy, and manage objects in a simple file-based storage system.

## Table of Contents
- [Description](#description)
- [Getting Started](#getting-started)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Examples](#examples)
- [Authors](#authors)

## Description

The AirBnB clone console is a command-line interpreter that provides several commands to manage AirBnB objects. The console supports creating new objects, retrieving objects from storage, updating existing objects, and deleting objects.

The following classes of objects are managed by the console:
- `BaseModel`
- `User`
- `State`
- `City`
- `Amenity`
- `Place`
- `Review`

## Getting Started

### Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/yourusername/AirBnB_clone.git
    ```

2. Change directory to the project folder:

    ```sh
    cd AirBnB_clone
    ```

3. Ensure the `console.py` file is executable:

    ```sh
    chmod +x console.py
    ```

### Usage

To start the console, run the following command:

```sh
./console.py
```

This will open an interactive shell where you can enter commands to manage AirBnB objects.

### Examples

Below are some examples of how to use the command interpreter:

#### Interactive Mode

```sh
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) create User
<new_user_id>
(hbnb) show User <new_user_id>
[User] (<new_user_id>) {'id': '<new_user_id>', 'created_at': '2023-05-15T00:00:00', 'updated_at': '2023-05-15T00:00:00'}
(hbnb) update User <new_user_id> first_name "John"
(hbnb) show User <new_user_id>
[User] (<new_user_id>) {'id': '<new_user_id>', 'created_at': '2023-05-15T00:00:00', 'updated_at': '2023-05-15T00:00:00', 'first_name': 'John'}
(hbnb) all User
[[User] (<new_user_id>) {'id': '<new_user_id>', 'created_at': '2023-05-15T00:00:00', 'updated_at': '2023-05-15T00:00:00', 'first_name': 'John'}]
(hbnb) count User
1
(hbnb) destroy User <new_user_id>
(hbnb) all User
[]
(hbnb) quit
$
```

#### Non-Interactive Mode

You can also use the console in non-interactive mode by piping commands into it:

```sh
$ echo "create User" | ./console.py
<new_user_id>
$ echo "User.show(<new_user_id>)" | ./console.py
[User] (<new_user_id>) {'id': '<new_user_id>', 'created_at': '2023-05-15T00:00:00', 'updated_at': '2023-05-15T00:00:00'}
$ echo "User.update(<new_user_id>, {'first_name': 'John'})" | ./console.py
$ echo "User.show(<new_user_id>)" | ./console.py
[User] (<new_user_id>) {'id': '<new_user_id>', 'created_at': '2023-05-15T00:00:00', 'updated_at': '2023-05-15T00:00:00', 'first_name': 'John'}
$ echo "User.destroy(<new_user_id>)" | ./console.py
$ echo "User.all()" | ./console.py
[]
```

## Authors

This project was developed by:

<alylolo223344@gmail.com>

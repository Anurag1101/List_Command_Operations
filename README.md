markdown
Copy code
# List Command Operations

Welcome to the **List Command Operations** repository! This project is a Python-based command-line application that allows users to interactively manipulate a list of integers by performing various operations like inserting, removing, appending, sorting, and reversing elements. The script is designed to handle commands dynamically based on user input, making it a versatile tool for learning and practicing Python list manipulations.

## Table of Contents
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Usage](#usage)
- [Commands Overview](#commands-overview)
  - [insert](#insert)
  - [print](#print)
  - [remove](#remove)
  - [append](#append)
  - [sort](#sort)
  - [pop](#pop)
  - [reverse](#reverse)
- [Example Usage](#example-usage)
- [Contributing](#contributing)
- [License](#license)

---

## Features

This script provides the ability to:
- **Insert values** into a list at specified positions.
- **Remove specific values** from the list.
- **Append values** to the end of the list.
- **Sort the list** in ascending order.
- **Reverse the list** to change the order of elements.
- **Pop the last element** from the list.
- **Print the current state of the list** at any time during operations.

With these operations, you can perform a wide range of manipulations on a list. This makes the script a great educational tool for understanding how list operations work in Python.

## Getting Started

### Prerequisites

To run this script, you'll need to have Python installed on your machine. You can check if Python is installed by running the following command in your terminal or command prompt:

```bash
python --version
If Python is not installed, you can download it from the official Python website.

Installation
Clone this repository to your local machine:

bash
Copy code
git clone https://github.com/yourusername/List_Command_Operations.git
Navigate to the cloned repository:

bash
Copy code
cd List_Command_Operations
(Optional) Create a virtual environment and activate it:

bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
You are now ready to run the script!

Usage
To execute the script, simply run:

bash
Copy code
python list_operations.py
Once the script is running, it will prompt you to:

Enter the number of commands you wish to perform.
Enter commands one at a time, with their respective arguments.
After entering each command, the script will process it and print the results if applicable.

Commands Overview
insert
bash
Copy code
insert <index> <value>
Inserts the value at the specified index in the list.
Example: insert 0 5 will insert the value 5 at index 0.
print
bash
Copy code
print
Prints the current state of the list.
Example: If the list is [1, 2, 3], it will output [1, 2, 3].
remove
bash
Copy code
remove <value>
Removes the first occurrence of the specified value from the list.
Example: remove 2 will remove the first occurrence of 2 in the list [1, 2, 2, 3], resulting in [1, 2, 3].
append
bash
Copy code
append <value>
Appends the value to the end of the list.
Example: append 4 will add 4 to the end of the list [1, 2, 3], resulting in [1, 2, 3, 4].
sort
bash
Copy code
sort
Sorts the list in ascending order.
Example: If the list is [3, 1, 2], it will be sorted to [1, 2, 3].
pop
bash
Copy code
pop
Removes the last element from the list.
Example: If the list is [1, 2, 3], pop will remove 3, resulting in [1, 2].
reverse
bash
Copy code
reverse
Reverses the order of elements in the list.
Example: If the list is [1, 2, 3], reverse will change the order to [3, 2, 1].
Example Usage
Here’s an example interaction that demonstrates the use of various commands:

bash
Copy code
Enter the number of commands: 8
insert 0 5      # List becomes [5]
insert 1 10     # List becomes [5, 10]
insert 0 6      # List becomes [6, 5, 10]
print           # Output: [6, 5, 10]
remove 10       # List becomes [6, 5]
append 9        # List becomes [6, 5, 9]
sort            # List becomes [5, 6, 9]
reverse         # List becomes [9, 6, 5]
print           # Output: [9, 6, 5]
Output:
csharp
Copy code
[6, 5, 10]
[6, 5]
[9, 6, 5]
Contributing
Contributions are welcome! If you would like to enhance the functionality of the script or improve the documentation, feel free to fork the repository and submit a pull request.

Fork the repository
Create a new branch (git checkout -b feature-branch)
Make your changes
Commit your changes (git commit -m 'Add some feature')
Push to the branch (git push origin feature-branch)
Open a pull request
License
This project is licensed under the MIT License - see the LICENSE file for details.

Author
Anurag Tiwari

# List Command Operations

This repository contains a Python script that allows you to perform various list operations interactively. The script supports several commands that can manipulate the list, such as inserting, printing, removing elements, and more.

## Features

The following operations are supported:
- **insert**: Insert a value at a specific index.
- **print**: Display the current list.
- **remove**: Remove the first occurrence of a value.
- **append**: Add a value to the end of the list.
- **sort**: Sort the list in ascending order.
- **pop**: Remove the last element from the list.
- **reverse**: Reverse the order of elements in the list.

## How to Use

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/List_Command_Operations.git
    ```
2. Navigate to the directory:
    ```bash
    cd List_Command_Operations
    ```

3. Run the script:
    ```bash
    python list_operations.py
    ```

4. Enter the number of commands you wish to perform:
    ```
    Enter the number of commands: 5
    ```

5. Enter the commands one by one:
    ```
    insert 0 5
    insert 1 10
    insert 0 6
    print
    remove 10
    ```

6. The output will be displayed for each command:
    ```
    [6, 5, 10]
    [6, 5]
    ```

## Example Commands

Here’s an example of a sequence of commands you can try:

```bash
insert 0 5      # Insert 5 at index 0
insert 1 10     # Insert 10 at index 1
insert 0 6      # Insert 6 at index 0
print           # Print the list: [6, 5, 10]
remove 10       # Remove the first occurrence of 10
print           # Print the list: [6, 5]
append 9        # Append 9 to the list
print           # Print the list: [6, 5, 9]
sort            # Sort the list in ascending order
print           # Print the sorted list: [5, 6, 9]
pop             # Remove the last element
print           # Print the list: [5, 6]
reverse         # Reverse the list
print           # Print the reversed list: [6, 5]

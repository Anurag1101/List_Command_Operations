# This line ensures the code inside this block runs only when the script is executed directly,
# not when it's imported as a module in another script.
if __name__ == '__main__':
    
    # Read the number of commands to process (how many operations the user will perform)
    n = int(input("Enter the number of commands: "))
    
    # Initialize an empty list where elements will be added, removed, or manipulated
    lst = []
    
    # Loop through the number of commands provided by the user
    for _ in range(n):
        # Read the user's command and split it into parts (command and arguments)
        command = input("Enter command: ").split()
        
        # The first part is the command type, e.g., insert, print, remove, etc.
        cmd_type = command[0]
        
        # Check the command type and execute the appropriate action
        
        if cmd_type == 'insert':
            # The 'insert' command requires two arguments: an index and a value
            # Convert these arguments from string to integer and insert the value at the given index
            index = int(command[1])
            value = int(command[2])
            lst.insert(index, value)  # Insert 'value' at the position 'index'
        
        elif cmd_type == 'print':
            # The 'print' command outputs the current state of the list
            print(lst)
        
        elif cmd_type == 'remove':
            # The 'remove' command needs one argument: the value to be removed
            # It removes the first occurrence of this value from the list
            value = int(command[1])
            lst.remove(value)
        
        elif cmd_type == 'append':
            # The 'append' command adds an element to the end of the list
            # It takes one argument: the value to be appended
            value = int(command[1])
            lst.append(value)
        
        elif cmd_type == 'sort':
            # The 'sort' command sorts the list in ascending order
            lst.sort()
        
        elif cmd_type == 'pop':
            # The 'pop' command removes the last element from the list
            lst.pop()
        
        elif cmd_type == 'reverse':
            # The 'reverse' command reverses the order of elements in the list
            lst.reverse()

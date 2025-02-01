import os

def list_directory_contents(directory):
    try:
        # Get the list of files and directories in the specified directory
        contents = os.listdir(directory)
        
        print(f"Contents of '{directory}':")
        for item in contents:
            print(item)
    except FileNotFoundError:
        print(f"The directory '{directory}' does not exist.")
    except PermissionError:
        print(f"Permission denied to access '{directory}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Specify the directory you want to list the contents of
directory_path = input("Enter the directory path: ")

# Call the function to list the contents
list_directory_contents(directory_path)

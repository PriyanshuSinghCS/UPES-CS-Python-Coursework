# Create multiple suitable exceptions for a file handling program. 

try:
    filename = input("Enter file to open: ")
    with open(filename, "r") as f:
        content = f.read().strip()
        num = int(content)
        print("Number from file:", num)
except FileNotFoundError:
    print("Error: The file does not exist!")
except PermissionError:
    print("Error: Permission denied.")
except ValueError:
    print("Error: The file contains text that isn't a number.")
except Exception as e:
    print("An unexpected error occurred:", e)
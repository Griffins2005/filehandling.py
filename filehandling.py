# File Creation
try:
    with open("my_file.txt", "w") as file:
        file.write("Hello, this is line 1\n")
        file.write("12345\n")
        file.write("This is line 3 with some numbers: 67890\n")
except IOError as e:
    print("Error creating file:", e)

# File Reading and Display
try:
    with open("my_file.txt", "r") as file:
        contents = file.read()
        print("Contents of my_file.txt:")
        print(contents)
except FileNotFoundError:
    print("File not found.")
except PermissionError:
    print("Permission denied.")

# File Appending
try:
    with open("my_file.txt", "a") as file:
        file.write("This is line 4\n")
        file.write("Another line added, line 5\n")
        file.write("Last line, line 6\n")
except IOError as e:
    print("Error appending to file:", e)
finally:
    print("Operations completed.")

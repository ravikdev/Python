with open("example.txt", "r") as f:
    contents = f.read()
    print(contents)
#This code reads the contents of "example.txt" into a string variable called contents, and then prints the contents to the console.

#To append to a file instead of overwriting its contents, you can use the mode argument "a" (append mode) when opening the file. Here's an example:


with open("example.txt", "a") as f:
    f.write("\nThis is a new line!")
#This code opens "example.txt" in append mode, and adds the string "\nThis is a new line!" to the end of the file on a new line.

#Overall, the open() function and the with statement are very useful for working with files in Python. Just remember to always close the file when you're done with it, or use the with statement to ensure that it gets closed automatically.






import pathlib

path = pathlib.Path("book.devops.txt")
path.write_text("LOG:DEBUG")
print(path.write_text("LOG:DEBUG"))
path = pathlib.Path("book.devops.txt")








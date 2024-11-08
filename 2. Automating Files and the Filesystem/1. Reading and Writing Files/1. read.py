file_path = 'book.devops.txt'
open_file = open(file_path, 'r')
text = open_file.read()
print(len(text))
print(text[16])
print(open_file)
open_file.close()



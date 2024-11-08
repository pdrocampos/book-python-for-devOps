file_path = 'book.devops.txt'
open_file = open(file_path, 'r')
text = open_file.readlines()
print(len(text))
print(text[0])
open_file.close()



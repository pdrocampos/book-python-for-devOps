file_path = '2.png'
with open(file_path, 'rb') as open_file:
    btext = open_file.read()

print(btext[0])
print(btext[:25])
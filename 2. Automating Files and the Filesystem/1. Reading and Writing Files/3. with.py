'''
Uma maneira prática de abrir arquivos é usar a instrução with. 
Nesse caso, você não precisa fechar o arquivo explicitamente. 
O Python o fecha e libera o recurso de arquivo no final do bloco indentado:
'''

file_path = 'book.devops.txt'
with open(file_path, 'r') as open_file:
    text = open_file.readlines()

print(text[3])
print(open_file.closed)

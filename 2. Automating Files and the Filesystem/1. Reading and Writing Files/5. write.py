text = '''export STAGE=PROD
export TABLE_ID=token-storage-1234
'''
with open('.envrc', 'w') as opened_file:
    opened_file.write(text)



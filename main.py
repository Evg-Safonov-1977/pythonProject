myFile = open('filename.txt', 'r', encoding="utf8")
file = myFile.read()
print(file)
myFile.close()

myFile = open('filename.txt', 'w')
myFile.write('tttt')
print('zzzz', file=myFile)
myFile.close()
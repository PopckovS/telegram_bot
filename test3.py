import os

path = '.git'
files = os.listdir(path)
result = ''
for i in files:
    result += str(i) + '\n'

print(result)
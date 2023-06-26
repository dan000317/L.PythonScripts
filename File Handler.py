# Use words.txt as the file name
fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()

inp = fhand.read()
inp = inp.rstrip("\n\n")
print (inp.upper())
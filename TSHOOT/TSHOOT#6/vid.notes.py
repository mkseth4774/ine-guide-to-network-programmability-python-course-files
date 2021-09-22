##
##
note = input('Enter your note: ')

with open("notes.txt", 'a') as f:
    f.write(note + "\n")

print()
print('Here are the notes you have: ')
with open('notes.txt') as f:
    for line in f:
        print(line.strip())
print()

##
## End of file...

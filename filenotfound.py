
try:
    with open('ajdskfjkaskdfjlsjl') as f:
        for line in f:
            print(line)
except (FileNotFoundError, TypeError):
#except:
    print('Hey, we have an issue, this file does not exist!!!')
    exit(99)

print('Yep, we are still running Python from this module!')

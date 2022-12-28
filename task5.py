word = input('Enter a word: ')

for letter in word:
    if letter.isdigit():
        if int(word) % 2 == 0:
            print(f'{word}-is even digit')
        else:
            print(f'{word}-is odd diggit')
    elif letter.istitle():
        print(f'{word}- capital letter')
    else:
        print(f'{word}-smoll letter')

        if letter.isalnum()==False:
            print(f'{word}-is symbol')

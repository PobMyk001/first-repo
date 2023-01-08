Phone_Book = {
    "Bob": "677545",
    "Marg": "345888",
    "Clif": "989000",
}
while True:

    command = input('enter the command:')

    if command == 'stats':
        print(f'{len(Phone_Book)} - number of subscribers')
    if command == 'add':
        print('enter the name:')
        name = input("> ")
        print('enter the phone number')
        number = input("> ")
        Phone_Book[name] = number
        print('subscriber is added')
    elif command == 'delete':
        print('enter the name:')
        name = input(">  ")

        del Phone_Book[name]
        print('phone number delete')
    elif command == 'list':
        print(Phone_Book.keys())
    elif command == 'show':
        print('enter the name')
        name = input('> ')
        if Phone_Book[name] == 'name':

        print(Phone_Book.get(name))
    else:
        print('subscriber not found')

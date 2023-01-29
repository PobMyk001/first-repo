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
        if name in Phone_Book:
            print('subscriber alreade exists')
        else:
            print('enter the phone number')
    number = input("> ")
    Phone_Book['name'] = number
    print('subscriber is added')
    if command == 'delete':
        print('enter the name:')
        name = input(">  ")
        if input(name) in Phone_Book:
            del Phone_Book[name]
            print('phone number delete')
    elif command == 'list':
        print(Phone_Book.keys())
    elif command == 'show':
        print('enter the name:')
        name = input('> ')
        if name in Phone_Book:
            print(Phone_Book.get(name))

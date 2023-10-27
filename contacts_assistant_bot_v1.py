def parse_validate_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    words = len(args)
    if cmd in ('add', 'change') and words != 2:
        return 'some not valid string'
    return cmd, *args


def add_contact(args, contacts):
    name, phone = args
    if name in contacts:
        what_to_do = input(f'Contact {name} already exists. Replace?: ')
        match what_to_do.lower():
            case 'y' | 'yes' | 1:
                contacts[name] = phone
                return 'Contact replaced.\n'
            case _:
                return 'Adding canceled.\n'
    contacts[name] = phone
    return 'Contact added.\n'


def change_contact(args, contacts):
    name, phone = args
    if name not in contacts:
        return f'No name {name} in contacts.\n'
    contacts[name] = phone
    return 'Contact changed.\n'


def show_all(contacts):
    result = ''
    for name, phone in contacts.items():
        result += f'{name}: {phone}\n'
    return result


def main():
    contacts = {}
    print('Welcome to the assistant bot!')
    while True:
        user_input = input('Enter a command: ')
        command, *args = parse_validate_input(user_input)
        match command:
            case 'close' | 'exit' | 'quit':
                print('Good bye!')
                break
            case 'hello':
                print('How can I help you?\n')
            case  'add':
                print(add_contact(args, contacts))
            case 'change':
                print(change_contact(args, contacts))
            case 'all':
                print(show_all(contacts))
            case _:
                print('Invalid command.\n')


if __name__ == '__main__':
    main()


clients = 'roberto, mariajose,'

def list_clients():
    print(clients)


def create_client(client_name):
    global clients
    if client_name not in clients:
        clients += client_name
        _add_comma()
    else:
        print('Client is already stored')


def _add_comma():
    global clients

    clients += ','


def _print_welcome():
    print('Welcome to PLATZIVENTAS')
    print('*' * 50)
    print('What would you like to do?')
    print('[C]reate client')
    print('[D]elete client')


if __name__ == '__main__':
    _print_welcome()
    command = input('Write a command: ')

    if command == 'C':
        client_name = input('Write client name: ')
        create_client(client_name)
        list_clients()
    elif command == 'D':
        pass
    else:
        print('Command does not exist')





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


def update_client(client_name, new_client_name):
    global clients
    if client_name in clients:
        clients = clients.replace(client_name + ',', new_client_name + ',')
    else:
        print('Client did not found')



def _add_comma():
    global clients

    clients += ','


def _print_welcome():
    print('Welcome to PLATZIVENTAS')
    print('*' * 50)
    print('What would you like to do?')
    print('[C]reate client')
    print('[D]elete client')
    print('[U]pdate client')


def _get_client_name():
    return input('What is the client name?: ')



if __name__ == '__main__':
    _print_welcome()
    command = input('Write a command: ')
    command = command.upper()

    if command == 'C':
        client_name = _get_client_name()
        create_client(client_name)
        list_clients()
    elif command == 'D':
        pass
    elif command == 'U':
        list_clients()
        client_name = _get_client_name()
        new_client_name = input('Write the new client name: ')
        update_client(client_name, new_client_name)
        list_clients()

    else:
        print('Command does not exist')




import sys

clients = 'roberto, mariajose,'

# Function for print all clients
def list_clients():
    print(clients)

# function for create a new client
def create_client(client_name):
    global clients
    #Verify if does not exist the same client
    if client_name not in clients:
        clients += client_name
        _add_comma()
    else:
        print('Client is already stored')

# Function for update a client name
def update_client(client_name, new_client_name):
    global clients
    # Verify if the client exists
    if client_name in clients:
        clients = clients.replace(client_name + ',', new_client_name + ',')
    else:
        _not_in_clients()

# Delete the client
def delete_client(client_name):
    global clients
    if client_name in clients:
        clients = clients.replace(client_name + ',', '')
    else:
        _not_in_clients()

def search_client(client_name):
    # Converts the clients variable into a list using the comma as a separator
    clients_list = clients.split(',')

    for client in clients_list:
        if client.lstrip() != client_name:
            continue
        else:
            return True


def _add_comma():
    global clients
    clients += ','

def _not_in_clients():
    print('Client is not in clients list')

def _print_welcome():
    print('Welcome to PLATZIVENTAS')
    print('*' * 50)
    print('What would you like to do?')
    print('[C]reate client')
    print('[D]elete client')
    print('[U]pdate client')
    print('[S]earch client')
    print('[L]ist clientS')


def _get_client_name():
    # Define an empty client name
    client_name = None

    while not client_name:
        client_name = input('What is the client name?: ')
        if client_name == 'exit':
            client_name = None
            break

    if not client_name:
        sys.exit()

    return client_name



if __name__ == '__main__':
    _print_welcome()
    command = input('Write a command: ')
    command = command.upper()

    if command == 'C':
        client_name = _get_client_name()
        create_client(client_name)
        list_clients()
    elif command == 'D':
        list_clients()
        client_name = _get_client_name()
        delete_client(client_name)
        list_clients()
    elif command == 'U':
        list_clients()
        client_name = _get_client_name()
        new_client_name = input('Write the new client name: ')
        update_client(client_name, new_client_name)
        list_clients()
    elif command == 'S':
        client_name = _get_client_name()
        found = search_client(client_name)

        if found:
            print('The client is in our clients list')
        else:
            print('The client is not in our clients list')
    elif command == 'L':
        list_clients()
    else:
        print('Command does not exist')




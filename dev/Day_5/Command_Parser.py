def execute_command(command):
    match command.split():
        case ['quit'] | ['exit']:
            print('Goodbye!')
        case ['hello', name]:
            print(f'Hello, {name}!')
        case ['add', a, b]:
            print(f'Result: {int(a) + int(b)}')
        case ['multiply', a, b]:
            print(f'Result: {int(a) * int(b)}')
        case ['help']:
            print('Commands: hello, add, multiply, quit')
        case _:
            print(f'Unknown command: {command}')
execute_command('hello Priya')
execute_command('add 15 27')
execute_command('multiply 6 8')
execute_command('quit')

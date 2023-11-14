gram = {
    "E": ["2E2", "3E3", "4"]
}
starting_terminal = "E"
inp = "2324232$"

stack = "$"
print(f'{"Stack": <15}' + f'{"Input Buffer": <15}' + f'Parsing Action')
print(f'{"-":-<50}')

while True:
    action = True

    for production in gram[starting_terminal]:
        if stack.endswith(production):
            stack = stack[:-len(production)] + starting_terminal
            print(f'{stack: <15}' + f'{inp: <15}' + f'Reduce S->{production}')
            action = False

    if len(inp) > 1:
        stack += inp[0]
        inp = inp[1:]
        print(f'{stack: <15}' + f'{inp: <15}' + f'Shift')
        action = False

    if inp == "$" and stack == ("$" + starting_terminal):
        print(f'{stack: <15}' + f'{inp: <15}' + f'Accepted')
        break

    if action:
        print(f'{stack: <15}' + f'{inp: <15}' + f'Rejected')
        break

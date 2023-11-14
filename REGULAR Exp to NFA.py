class State:
    def __init__(self, label):
        self.label = label
        self.transitions = {}

def regular_expression_to_nfa(regex):
    stack = []
    state_count = 0

    for symbol in regex:
        if symbol.isalpha() or symbol.isdigit():
            state = State(str(state_count))
            state_count += 1
            stack.append([state])
        elif symbol == '*':
            if stack:
                current_states = stack.pop()
                new_state = State(str(state_count))
                state_count += 1
                for state in current_states:
                    state.transitions[None] = new_state
                stack.append([new_state])
        elif symbol == '|':
            if stack:
                alternative_states = stack.pop()
                if stack:
                    current_states = stack.pop()

                    # Create new states for alternation
                    new_state1 = State(str(state_count))
                    state_count += 1
                    new_state2 = State(str(state_count))
                    state_count += 1

                    # Transition from new states to the branches
                    new_state1.transitions[None] = alternative_states[0]
                    new_state1.transitions[None] = current_states[0]
                    new_state2.transitions[None] = alternative_states[0]
                    new_state2.transitions[None] = current_states[0]

                    stack.append([new_state1, new_state2])
                else:
                    stack.append(alternative_states)

    if stack:
        final_states = stack.pop()
        if len(final_states) == 1:
            return final_states[0]
        else:
            raise ValueError("Invalid regular expression")

def print_nfa(state, visited=None):
    if visited is None:
        visited = set()
    if state not in visited:
        visited.add(state)
        for symbol, next_state in state.transitions.items():
            if symbol is None:
                print(f"{state.label} --ε--> {next_state.label}")
            else:
                print(f"{state.label} --{symbol}--> {next_state.label}")
        for next_state in state.transitions.values():
            print_nfa(next_state, visited)

# Example usage with a different regular expression
regex = "a*b"
nfa = regular_expression_to_nfa(regex)

# Print NFA
print_nfa(nfa)

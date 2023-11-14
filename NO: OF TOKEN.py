import re

expression = input("Enter an expression: ")

token_patterns = [
    (r'[0-9]+', 'NUMBER'),
    (r'[+\-*/]', 'OPERATOR'),
    (r'\(', 'LPAREN'),
    (r'\)', 'RPAREN'),
]

tokens = []

while expression:
    for pattern, token_type in token_patterns:
        match = re.match(pattern, expression)
        if match:
            tokens.append((match.group(), token_type))
            expression = expression[len(match.group()):].strip()
            break
    else:
        print("Invalid character in the expression")
        break

for token, token_type in tokens:
    print(f"Token: {token}, Type: {token_type}")

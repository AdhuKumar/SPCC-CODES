class Stack:
  def __init__(self):
    self.items = []

  def push(self, item):
    self.items.append(item)

  def pop(self):
    return self.items.pop()

  def is_empty(self):
    return len(self.items) == 0

  def peek(self):
    if not self.is_empty():
      return self.items[-1]
    else:
      return None

def precedence(operator):
  if operator == '+' or operator == '-':
    return 1
  elif operator == '*' or operator == '/':
    return 2
  else:
    return -1

def infix_to_postfix(infix_expression):
  postfix_expression = ""
  stack = Stack()

  for character in infix_expression:
    if character.isalpha() or character.isdigit():
      postfix_expression += character
    elif character == '(':
      stack.push(character)
    elif character == ')':
      while stack.peek() != '(':
        postfix_expression += stack.pop()
      stack.pop()
    else:
      while not stack.is_empty() and precedence(stack.peek()) >= precedence(character):
        postfix_expression += stack.pop()
      stack.push(character)

  while not stack.is_empty():
    postfix_expression += stack.pop()

  return postfix_expression

infix_expression = "a+b*c"
postfix_expression = infix_to_postfix(infix_expression)

print(f"Infix expression: {infix_expression}")
print(f"Postfix expression: {postfix_expression}")

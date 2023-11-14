def check_string_ending_with_ab(str1):
  if str1[-2:] == "ab":
    return True
  else:
    return False

str1 = input("Enter a string: ")

if check_string_ending_with_ab(str1):
  print("The string ends with 'ab'.")
else:
  print("The string does not end with 'ab'.")

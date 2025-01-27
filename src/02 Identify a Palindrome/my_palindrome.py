def is_palindrome(str=""):
  clean_list = [' ', ',', '.', '-', '\'', '!']
  temp_str = []
  for c in str:
    if c in clean_list:
      continue
    else:
      temp_str.append(c)
    clean_str = ''.join(temp_str)

  reverse_str = clean_str[::-1]
  if(clean_str.upper() == reverse_str.upper()):
    print("palindrome")
  else:
    print("not palindrome")

is_palindrome("radar")

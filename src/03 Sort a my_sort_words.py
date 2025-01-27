def sort_string(input="default"):
  return sorted(input.split(), key=str.casefold)

print(sort_string("APPLE banana orange Peach Strawberry BLUEBERRY"))

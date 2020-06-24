def rotate(letter, key):
  if letter.islower():
    new = ord(letter) + key
    if new > ord('z'):
      new = new - 26
    new = chr(new)
  else:
    new = letter
  return new

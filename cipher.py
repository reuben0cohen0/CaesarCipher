# Caesar Cipher
MAX_KEY_SIZE = 25


def getkey():
    key = 0
    while True:
        print('Enter the key number (1-%s)' % (MAX_KEY_SIZE))
        key = int(input())
        if (key >= 1 and key <= MAX_KEY_SIZE):
            return key
        else:
            print('Please enter a key between +1 and +25')


def gettranslatedmessage(mode, message, key):
    if mode[0] == 'd':
        key = -key
    translated = ''

    for symbol in message:
        if symbol.isalpha():
            num = ord(symbol)
            num += key
            # UPPERCASE Letters cipher
            if symbol.isupper():
                if num > ord('Z'):
                    num -= 26
                elif num < ord('A'):
                    num += 26
            # lowercase letters cipher
            elif symbol.islower():
                if num > ord('z'):
                    num -= 26
                elif num < ord('a'):
                    num += 26

            translated += chr(num)
        else:
            translated += symbol
    return translated

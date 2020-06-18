# Caesar Cipher
MAX_KEY_SIZE = 25


def getmode():
    while True:
        print('Do you wish to encrypt (e) or decrypt (d) or brute force (b) a message?')
        mode = input().lower()
        if mode in 'encrypt e decrypt d brute b'.split():
            return mode
        else:
            print('Enter either "encrypt" or "e" or "decrypt" or "d" or "brute" or "b"')


def getmessage():
    print('Enter your message:')
    return input()


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

            if symbol.isupper():
                if num > ord('Z'):
                    num -= 26
                elif num < ord('A'):
                    num += 26
            elif symbol.islower():
                if num > ord('z'):
                    num -= 26
                elif num < ord('a'):
                    num += 26

            translated += chr(num)
        else:
            translated += symbol
    return translated


mode = getmode()
message = getmessage()
if mode[0] != 'b':
    key = getkey()

print('Your translated text is:')
if mode[0] != 'b':
    print(gettranslatedmessage(mode, message, key))
else:
    for key in range(1, MAX_KEY_SIZE + 1):
        print(key, gettranslatedmessage('decrypt', message, key))
print('Would you like to do another message?')
answer = ["yes", "Yes", "y", "Y", "no", "NO", "n", "N"]
for x in answer:
    if x == "yes" "Yes" "y" "Y":
        continue

from crypto import encrypt

if __name__ == "__main__":
    word = input("Word: ")
    key = int(input("Key: "))
    print(encrypt(word, key))

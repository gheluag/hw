def get_password(word):
    hash_word = hex(hash(word))
    print(hash_word)
get_password(word = input("введите слово: "))
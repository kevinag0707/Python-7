

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'

word = input('Type a word: ')

for ind in word:
    answer = alphabet.index(ind)
    print(answer)
    
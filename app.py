import secrets
import sys

def gen_passphrase(word_count: int = 7, separator: str = '-'):
    f = open('bitcoin-bip39.txt', 'r')
    text = f.read()
    f.close()
    lines = [l.strip() for l in text.strip().split('\n')]
    def gen_word():
        i = secrets.randbelow(2048)
        return lines[i]
    words = [gen_word() for n in range(word_count)]
    print(separator.join(words))

try:
    gen_passphrase(int(sys.argv[1]), sys.argv[2])
except IndexError:
    try:
        gen_passphrase(int(sys.argv[1]))
    except IndexError:
        gen_passphrase()

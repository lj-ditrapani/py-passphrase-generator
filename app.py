import argparse
import secrets
import sys

def gen_passphrase(word_count: int, separator: str, file_prefix: str):
    with open(file_prefix + '.txt', 'r') as file:
        text = file.read()
    lines = [line.strip() for line in text.strip().splitlines()]
    count = len(lines)
    def gen_word():
        i = secrets.randbelow(count)
        return lines[i]
    words = [gen_word() for n in range(word_count)]
    print(separator.join(words))

parser = argparse.ArgumentParser()
parser.add_argument("count", type=int, help='number of random words to generate')
parser.add_argument("separator", type=str, help="string to insert between words. Use ' ' for empty space")
parser.add_argument("--wordlist", "-l", type=str, help="source word list from bitcoin or eff.org", default='bip39', choices=['bip39', 'eff-large', 'eff-short', 'eff-short-2'])
args = parser.parse_args()
gen_passphrase(args.count, args.separator, args.wordlist)

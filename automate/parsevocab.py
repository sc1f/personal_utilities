#!/usr/bin/env python3

import argparse
arg = argparse.ArgumentParser()
arg.add_argument("file", type=str, help="input text file")
arg.add_argument("dir", type=str, help="dir to save new file in")
input = arg.parse_args()

def parse_vocab(file, dir):
    vocab_file = open(file).read().split("\n")
    vocab_length = int(len(vocab_file))
    split_length = int(vocab_length / 2)
    if vocab_length % 2 != 0:
        return ValueError("input file cannot be evenly split")
    # begin processing
    vocab_fr = vocab_file[:vocab_length//2]
    vocab_en = vocab_file[vocab_length//2:]
    for word in vocab_fr:
        word.rstrip()
    for word in vocab_en:
        word.rstrip()
    vocab_final = []
    for i in range(0, split_length):
        vocab_final.append(str(vocab_fr[i]) + '|' + str(vocab_en[i]))
    # write to new file
    with open(dir + 'output_vocab.txt', 'w') as output:
        output.write("\n".join(vocab_final))
        print("output file written, with " + str(len(vocab_final)) + " lines")

if __name__ == '__main__':
    parse_vocab(input.file, input.dir)

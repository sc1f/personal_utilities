#!/user/bin/env python3

import pypdf2, csv, argparse
args = argparse.ArgumentParser()
args.add_argument("input", type="str", help="input file")
args.add_argument("output", type="str", help="output filename")
input = args.parse_args()

def parse_pdf(file):
    reader = pypdf2.PdfFileReader(input.input)
    print("Reading " + str(input.input) +", a PDF file with " + str(reader.getNumPages()) + " pages\n")

if __name__ == '__main__':
    parse_pdf(input.input)

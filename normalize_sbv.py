# Takes .sbv subtitle file and tries to make subtitles
# that are like Youtube's with lengths between 30 and 50
# chars per line by halving long lines


import sys
import argparse
import pathlib


parser = argparse.ArgumentParser(description="CLI tool for normalizing sbv caption length")
parser.add_argument("-m", "--max", dest="max_length", type=int, default=50, help="Maximum length in characters for line of caption")
parser.add_argument("-o", "--output", dest="outfile", type=pathlib.Path, help="Name of the output file. By default -norm is appended")
parser.add_argument("input_file", type=pathlib.Path, help="Input .sbv captions file") 

if __name__ == '__main__':

    args = parser.parse_args()
    with open(args.input_file, 'r') as f:
        lines = f.readlines()
    if lines[-1] != '\n':
        lines.append('\n')

    newlines = []

    i = 0
    while i < len(lines):
        # Append timestamp
        newlines.append(lines[i])
        i += 1

        # Keep adding words of caption until a "\n" separator is found
        tofix = []
        totallen = 0
        while lines[i] != '\n':
            tofix.extend(lines[i].strip().split())
            totallen += len(lines[i])
            i += 1

        # If over the max length split into two lines with a similar length
        if totallen <= args.max_length:
            newlines.append(" ".join(tofix)+'\n')
        else:
            j, halflen = 0, 0
            while halflen < totallen//2:
                halflen += len(tofix[j]) + 1
                j += 1
            newlines.append(" ".join(tofix[:j])+'\n')
            newlines.append(" ".join(tofix[j:])+'\n')

        i += 1
        newlines.append('\n')

    outfile = args.outfile
    if outfile is None:
        outfile = args.input_file.parent / (args.input_file.stem + '-norm.sbv')
    with open(outfile, 'w') as f:
        f.writelines(newlines)

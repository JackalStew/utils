"""
Splits the contents of input into several strings of specified maximum length.
A prefix and suffix can also be specified.
Pipe stuff in, stuff comes out.
"""
from argparse import ArgumentParser
from sys import stdin, stdout

parser = ArgumentParser()
parser.add_argument("-n", "--max-len", type=int, default=50)
parser.add_argument("-p", "--prefix", default="Str = Str + \"")
parser.add_argument("-s", "--suffix", default="\"")
args = parser.parse_args()

n = args.max_len
prefix = args.prefix
suffix = args.suffix

for line in stdin.readlines():
    line = line.rstrip()
    for i in range(0, len(line), n):
        stdout.write(prefix + line[i:i+n] + suffix + '\n')

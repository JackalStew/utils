"""
Quick script for modifying line endings.
Pipe stuff into it, new stuff comes out.
"""
from argparse import ArgumentParser
from sys import stdin, stdout

parser = ArgumentParser()
parser.add_argument("-w", "--windows", action="store_true")
args = parser.parse_args()

line_end = "\n"
if args.windows:
    line_end = "\r\n"

for line in stdin.readlines():
    stdout.write(line.rstrip("\r\n") + line_end)

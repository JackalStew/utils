"""
A script to produce several "echo" command lines to reconstruct a file.
Bad characters are delimted.
Pipe stuff in, stuff comes out.
"""
from argparse import ArgumentParser
from sys import stdin, stdout

parser = ArgumentParser()
parser.add_argument("fname")
parser.add_argument("-w", "--windows", action="store_true")
args = parser.parse_args()
fname = args.fname
is_win = args.windows

esc_char = '\\'
bad_chars = r'''"'&;<>~\#!$(){}[]'''
if is_win:
    esc_char = '^'
    bad_chars = r'''&^<>'''

for line in stdin.readlines():
    new_line = ""
    for c in line.rstrip():
        if c in bad_chars:
            c = esc_char + c
        new_line += c
    stdout.write("echo " + new_line  + " >> " + fname + '\n')

# python .\debflags.py -f .\rules.txt -k CONFARGS -v

import argparse
import re

parser = argparse.ArgumentParser(description='Python script for extracting Debian Sid compile flags.')
parser.add_argument('-f', '--file', type=str, help='Input file', required=True)
parser.add_argument('-k', '--keyword', type=str, help='Keyword used by the rules file to refer to flags.')
parser.add_argument('-v', '--verbose', action='store_true', help='Print entire line and every single occurrence. Note: A $ means that the line contains a reference of the flags.')
args = parser.parse_args()

# Keyword to search by
if args.keyword:
    FLAG_KEYWORD = args.keyword
else:
    FLAG_KEYWORD = "CONFARGS"

# Final flags
FINAL_FLAGS = ""

# Pattern to check for = or += which add to the complilation flags
pattern_equals = r'^{}\s*=.*$'.format(re.escape(FLAG_KEYWORD))
pattern_plus_equals = r'^{}\s*\+=.*$'.format(re.escape(FLAG_KEYWORD))

# Begin extracting flags.
with open(args.file, 'r') as file:
    lines = file.readlines()

    for line_number, line in enumerate(lines, start=1):
        if FLAG_KEYWORD in line:

            previous_line = lines[line_number-2]
            conditioned = "ifeq" in previous_line
            include_flags = False

            # We add anything for amd64
            if conditioned and "amd64" in previous_line:
                include_flags = True

            # This means the flag is good for anything, and we want it
            if not conditioned:
                include_flags = True

            doesReference = f"$({FLAG_KEYWORD})" in line

            if args.verbose:
                if doesReference:
                    print(f"Line {line_number}$: {line.strip()}")
                else:
                    print(f"Line {line_number}: {line.strip()}")

            # A reference to the flags does not add to the final output
            if doesReference:
                continue

            match_eq = re.match(pattern_equals, line.strip())
            match_pl_eq = re.match(pattern_plus_equals, line.strip())

            if match_eq or match_pl_eq:
                if not include_flags:
                    continue
                FINAL_FLAGS += line[line.index("=")+1:].strip() + " "

    print(f"\nFlags found: {FINAL_FLAGS}\n")

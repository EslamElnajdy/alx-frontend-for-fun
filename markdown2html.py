#!/usr/bin/python3

"""
script markdown2html.py that takes an argument 2 strings:
    - First argument is the name of the Markdown file
    - Second argument is the output file name
"""


import sys
import os
import re

def convert_heading(line):
    if line.startswith("#"):
        match = re.match(r'^(#+)\s*(.+)$', line)
        if match:
            count = len(match.group(1))
            return f"<h{count}>{match.group(2).strip()}</h{count}>"
    return line


def main():
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html",
              file=sys.stderr)
        sys.exit(1)

    markdown_file = sys.argv[1]
    html_file = sys.argv[2]

    if not os.path.exists(markdown_file):
        print(f"Missing {markdown_file}", file=sys.stderr)
        sys.exit(1)

    # open the file markdown
    lines = []
    converted_lines = []

    with open(markdown_file, "r") as f:
        lines = f.readlines()

    for line in lines:
        converted_line = convert_heading(line)
        converted_lines.append(converted_line)

    with open(html_file, "w") as html:
        html.write("\n".join(converted_lines))
        html.write("\n")


    sys.exit(0)


if __name__ == "__main__":
    main()

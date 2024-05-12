#!/usr/bin/python3

"""
module
"""
import sys
import os
import re


def convert_heading(line=''):
    """ fn """
    if (line.startswith("#")):
        match = re.match(r'^(#+)\s*(.+)$', line)
        if match:
            count = min(len(match.group(1)), 6)
            return f"<h{count}>{match.group(2).strip()}</h{count}>"
    return line


def convert_unordered_list(lines=''):
    """ fn """
    converted_list = []
    in_list = False

    for line in lines:
        if line.startswith("- "):
            if not in_list:
                converted_list.append("<ul>")
                in_list = True
            converted_list.append(f"<li>{line.strip('- ').strip()}</li>")
        else:
            if in_list:
                converted_list.append("</ul>")
                in_list = False
            converted_list.append(line)

    if in_list:
        converted_list.append("</ul>")

    return converted_list

def convert_ordered_list(lines):
    """ fn """
    converted_list = []
    in_list = False

    for line in lines:
        if line.startswith("* "):
            if not in_list:
                converted_list.append("<ol>")
                in_list = True
            converted_list.append(f"<li>{line.strip('* ').strip()}</li>")
        else:
            if in_list:
                converted_list.append("</ol>")
                in_list = False
            converted_list.append(line)

    if in_list:
        converted_list.append("</ol>")

    return converted_list


def convert_to_html(markdown_file, html_file):
    """ fn """
    with open(markdown_file, "r") as md:
        lines = md.readlines()
        converted_lines = [convert_heading(line) for line in lines]
        converted_lines = convert_unordered_list(converted_lines)
        converted_lines = convert_ordered_list(converted_lines)

    with open(html_file, "w") as html:
        for line in converted_lines:
            html.write(line + "\n")


def main():
    """
    fn
    """
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html",
              file=sys.stderr)
        sys.exit(1)

    markdown_file = sys.argv[1]
    html_file = sys.argv[2]

    if not os.path.exists(markdown_file):
        print(f"Missing {markdown_file}", file=sys.stderr)
        sys.exit(1)

    convert_to_html(markdown_file, html_file)
    sys.exit(0)


if __name__ == "__main__":
    main()

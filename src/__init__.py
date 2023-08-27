import argparse
import os
import re
import json
from .scripts.scan_web_passwords import ScanPageForPasswords
from .scripts.enhanced_passwords import enhanced_passwords


def main():
    parser = argparse.ArgumentParser(description="This tool is designed to generate enhanced password variations by "
                                                 "analyzing content from a given webpage. The generator can consider "
                                                 "different combinations of uppercase-lowercase, leetspeak "
                                                 "substitutions, and year appendages. By setting specific flags, users "
                                                 "can define the complexity and variation of the generated passwords to"
                                                 " ensure a broad range of possible combinations.\n Created by j0lt")

    parser.add_argument('--url', '-U', type=str, required=True, help="URL to fetch possible passwords from a "
                                                                     "specific webpage.")
    parser.add_argument('--cookies', '-c', type=str,
                        help="Provide cookies in format: '{\"cookie_name\": \"cookie value\", ...}' "
                             "if required to access the page.")
    parser.add_argument('--uplow', '-u', action='store_true', help="Consider both uppercase and lowercase "
                                                                   "variations of the passwords. eg: pAssWord and so on")
    parser.add_argument('--leet', '-l', action='store_true', help="Transform certain letters in passwords to "
                                                                  "similar-looking numbers or symbols, eg: p@ssw0rd")
    parser.add_argument('--year', '-y', action='store_true',
                        help="Append and prepend years (e.g., from 1970 to current "
                             "year) to the passwords.eg: password@2023 and "
                             "2023@password")
    parser.add_argument('--simple', '-s', action='store_true', help="If you only want simple  passwords without any "
                                                                    "transformations.")
    parser.add_argument('--output', '-o', required=True, type=str, help="Output file in text format. eg. "
                                                                        "/path/to/a/directory/output.txt")

    args = parser.parse_args()

    if not re.match(r'^https?://', args.url):
        args.url = 'http://' + args.url
        if not re.match(r'^https?://[^/]+/.*', args.url):
            print("Please enter the URL in the format http://url/path or https://url/path.")
            exit(1)

    cookies_dict = {}
    if args.cookies:
        try:
            cookies_dict = json.loads(args.cookies)
            if not isinstance(cookies_dict, dict):
                raise ValueError("Cookies should be provided in a dictionary format.")
        except json.JSONDecodeError:
            print("Error decoding cookies. Ensure they are in the format: '{\"cookie_name\": \"cookie value\", ...}'.")
            exit(1)

    output_directory = os.path.dirname(args.output)
    if output_directory and not os.path.exists(output_directory):
        print(f"Error: The specified directory '{output_directory}' does not exist.")
        exit(1)
    if not args.output.endswith('.txt'):
        print("Error: Please provide a filename with a .txt extension.")
        exit(1)

    options_list = []
    if args.uplow:
        options_list.append('uplow')
    if args.leet:
        options_list.append('leet')
    if args.year:
        options_list.append('year')

    simple_passwords = ScanPageForPasswords(args.url, cookies_dict)

    with open(args.output, 'w') as f:
        if args.simple or not options_list:
            for word in simple_passwords:
                f.write(word + "\n")
        if options_list:
            enhanced_passwords(simple_passwords, options_list).result(f)

    with open(args.output, 'r') as file:
        passwords = file.readlines()
    unique_passwords = list(dict.fromkeys(passwords))
    with open(args.output, 'w') as file:
        file.writelines(unique_passwords)

    print(f"Output saved at {args.output}")

# webpage-password-list-generator

This tool is designed to generate enhanced password variations by analyzing the content from a given webpage. Leveraging the information fetched, it can construct potential passwords considering combinations such as uppercase-lowercase variations, leetspeak substitutions, and appending/prepending of years. Depending on the specific flags set, users can precisely tailor the complexity and variations of the generated passwords to ensure a broad spectrum of combinations.

Created by j0lt.

## Features

- **Webpage Analysis**: Analyzes the given webpage for potential password seeds.
- **Uppercase-Lowercase Variations**: Creates combinations using various capitalization schemes.
- **Leetspeak Substitutions**: Converts specific characters in potential passwords to their leetspeak equivalents.
- **Year Appends**: Attaches years (from 1970 to the present year) to the start or end of potential passwords.
- **Simple Passwords**: Allows generation of basic passwords without any transformations.

## Usage

```
usage: main.py [-h] --url/-U URL [--cookies COOKIES] [--uplow/-u] [--leet-l] [--year/-y] [--simple/-s] --output/-o OUTPUT
```

### Options:

- `-h, --help`: Show this help message and exit.
- `--url URL, -U URL`: URL to fetch possible passwords from a specific webpage.
- `--cookies COOKIES, -c COOKIES`: Provide cookies in format: `{"cookie_name": "cookie value", ...}` if required to access the page.
- `--uplow, -u`: Consider both uppercase and lowercase variations of the passwords. 
- `--leet, -l`: Use leetspeak transformations for passwords.
- `--year, -y`: Append and prepend years to the passwords.
- `--simple, -s`: Only generate simple passwords without transformations.
- `--output OUTPUT, -o OUTPUT`: Specify the path for the output file.

### Examples:

1. **Basic Usage (generate simple password list without variations)**:
   ```bash
   python main.py -U https://example.com -o output.txt
   ```

2. **With Cookies (if needed)**:
   ```bash
   python main.py -U https://example.com -c '{"session": "abcd1234"}' -o output.txt
   ```

3. **Uppercase-Lowercase and Leetspeak Variations**:
   ```bash
   python main.py -U https://example.com -u -l -o output.txt
   ```

4. **Simple Passwords Only**:
   ```bash
   python main.py -U https://example.com -s -o output.txt
   ```

5. **All Transformations**:
   ```bash
   python main.py -U https://example.com -u -l -y -s -o output.txt
   ```


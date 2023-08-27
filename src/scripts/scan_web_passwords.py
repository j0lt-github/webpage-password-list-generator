from bs4 import BeautifulSoup
import requests

def ScanPageForPasswords(url, cookies=None):
    response = requests.get(url, cookies=cookies, headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/91.0.4472.124 Safari/537.36',
        'Accept-Language': 'en-US,en;q=0.5',
        'Referer': url
    })
    soup = BeautifulSoup(response.text, 'html.parser')
    possible_passwords = []
    words = [word.strip('.,-&') for string in soup.stripped_strings for word in string.split()]
    for string in words:
        if 5 <= len(string) <= 20:
            possible_passwords.append(string)
    possible_passwords = list(set(possible_passwords))
    return possible_passwords

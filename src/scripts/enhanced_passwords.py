from datetime import datetime
import itertools


class enhanced_passwords:

    def __init__(self, password_list, combination_list):
        self.default_password_list = password_list
        self.combination_list = tuple(combination_list)
        self.final = []

    def __upper_lower_password_combinations(self):
        upper_lower_combination_list = []
        for word in self.default_password_list:
            choices = [(char.lower(), char.upper()) for char in word]
            upper_lower_combination_list.extend([''.join(combination) for combination in itertools.product(*choices)])
        return upper_lower_combination_list

    def __leet_replacement(self, list_of_words=None):
        if list_of_words is None:
            list_of_words = []
        list_of_words.extend(self.default_password_list)
        substitutions = {
            'a': ['a', '@'],
            'A': ['A', '@'],
            'e': ['e', '3'],
            'E': ['E', '3'],
            'o': ['o', '0'],
            'O': ['O', '0'],
            'i': ['i', '1'],
            'I': ['I', '1'],
            's': ['s', '$'],
            'S': ['S', '$']
        }

        leet_combinations = []

        for word in list_of_words:
            charsToCombine = [substitutions[char] if char in substitutions else [char] for char in word]
            wordCombinations = [''.join(comb) for comb in itertools.product(*charsToCombine)]
            leet_combinations.extend(wordCombinations)

        return leet_combinations

    def __year_combination(self, list_of_words=None):
        if list_of_words is None:
            list_of_words = []
        list_of_words.extend(self.default_password_list)
        years = [str(year) for year in range(1970, datetime.now().year + 1)]
        year_passwords = []

        special_chars = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '?', '-', '+']

        for password in list_of_words:
            for year in years:
                year_passwords.append(password + year)
                year_passwords.append(year + password)
                for char in special_chars:
                    year_passwords.append(password + char + year)
                    year_passwords.append(year + char + password)

        return year_passwords

    def result(self, outfile):
        def run_all():
            for word in self.__upper_lower_password_combinations():
                outfile.write(word + "\n")
            for word in self.__leet_replacement():
                outfile.write(word + "\n")
            for word in self.__year_combination():
                outfile.write(word + "\n")

        def run_uplow_leet():
            for word in self.__upper_lower_password_combinations():
                outfile.write(word + "\n")
            for word in self.__leet_replacement():
                outfile.write(word + "\n")

        def run_uplow_year():
            for word in self.__upper_lower_password_combinations():
                outfile.write(word + "\n")
            for word in self.__year_combination():
                outfile.write(word + "\n")

        def run_leet_year():
            for word in self.__leet_replacement():
                outfile.write(word + "\n")
            for word in self.__year_combination():
                outfile.write(word + "\n")

        switch = {
            ('uplow', 'leet', 'year'): run_all,
            ('uplow', 'leet'): run_uplow_leet,
            ('uplow', 'year'): run_uplow_year,
            ('leet', 'year'): run_leet_year,
            ('uplow',): self.__upper_lower_password_combinations,
            ('leet',): self.__leet_replacement,
            ('year',): self.__year_combination,
        }
        switch.get(self.combination_list)()


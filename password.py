from ast import Str


import random
import string


class Password:
    def __init__(self) -> None:
        pass

    def create_password(self,  no_of_characters: int):
        password = ''
        remainders = no_of_characters % 4
        whole_digits = round(no_of_characters / 4)
        for i in range(whole_digits):
            newpw = self.__random_characters()
            password = newpw+password
        for i in range(remainders):
            newpw = self.__random_characters()
            password = newpw[random.randint(0, 3)]+password

        pw_list = list(password)
        random.shuffle(pw_list)
        if len(pw_list) == no_of_characters:
            password = ''.join(pw_list)
            
            return password
        else:
            difference = len(pw_list) - no_of_characters
            random.shuffle(pw_list)
            for i in range(difference):
                random.shuffle(pw_list)
                pw_list.pop()
            password = ''.join(pw_list)
            return password

    def __random_characters(self):
        lowercase = string.ascii_lowercase
        uppercase = string.ascii_uppercase
        digits = string.digits
        symbols = string.punctuation
        password = lowercase[random.randint(0, 25)] + uppercase[random.randint(
            0, 25)] + digits[random.randint(0, 9)] + symbols[random.randint(0, len(symbols) - 1)]

        return password

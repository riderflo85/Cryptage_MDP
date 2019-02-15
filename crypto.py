#! usr/bin/env python3
# coding: utf-8

import hashlib
from getpass import getpass

condition = True
result_done = ["o", "O", "oui"]
result_none = ["n", "N", "non"]


def encoding_key_low_level(key):

    key = key.encode()
    encoding_result = hashlib.sha1(key).hexdigest()
    print(encoding_result)


def encoding_key_medium_level(key):

    key = key.encode()
    encoding_low = hashlib.sha1(key).hexdigest()
    encoding_low = encoding_low.encode()
    encoding_result = hashlib.sha256(encoding_low).hexdigest()
    print(encoding_result)


def encoding_key_high_level(key):

    key = key.encode()
    encoding_low = hashlib.sha1(key).hexdigest()
    encoding_low = encoding_low.encode()
    encoding_medium = hashlib.sha256(encoding_low).hexdigest()
    encoding_medium = encoding_medium.encode()
    encoding_result = hashlib.sha512(encoding_medium).hexdigest()
    print(encoding_result)


def main():

    global condition

    cond = input("Voulez-vous chiffrer un mot de passe? (O/N)\n ")
    if cond in result_done:
        level = input("Quelle niveau de chiffrage voulez-vous? (1, 2 ou 3)\n ")
        user_choice = getpass()

        if level == "1":
            encoding_key_low_level(user_choice)

        elif level == "2":
            encoding_key_medium_level(user_choice)

        elif level == "3":
            encoding_key_high_level(user_choice)

    elif cond in result_none:
        condition = False

    else:
        print("Vous n'avez pas tapez de réponse correct...")
        end = input("Voulez vous quittez le programme? (O/N)\n ")

        if end in result_done:
            condition = False

        elif end in result_none:
            pass


while condition:
    main()

#!/bin/python3
# This script checks haveibeenpwned API to see if a password has been previously compromised
# See: https://haveibeenpwned.com/API/v2
# K-Anonymity: https://www.troyhunt.com/ive-just-launched-pwned-passwords-version-2/

import hashlib
import argparse
import requests

def check_pwd(pwd):
    base_url = "https://api.pwnedpasswords.com/range/"
    h_pwd = hashlib.sha1(str.encode(pwd)).hexdigest()
    url = "{}{}".format(base_url, h_pwd[:5])

    headers = {
        'User-Agent': 'PWND Password Checker 1.0',
    }

    response = requests.get(url, headers=headers)
    print(response.status_code)
    if response.status_code != 200:
        print("Oops, something went wrong with the request.")
        exit(1)

    list_of_hashes = response.content.decode().split('\r\n')

    for h in list_of_hashes:
        if h_pwd[5:].lower() in h.lower():
            freq = h.split(':', 1)[1]
            print("This password has been pwned {} times before!".format(freq))
            exit(1)

    print("This password might be safe enough to be used...")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Submits part of a password '
                                     'hash to haveibeenpwd API for compromise check.')
    parser.add_argument('password', metavar='PWD', nargs='+',
                        help='The password to submit for testing.')
    args = parser.parse_args()
    check_pwd(args.password[0])

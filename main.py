#!/usr/bin/env python

import os
import string
import random

def randompassword(size):
    '''
    This function generates a random password.
    Return string value.
    '''
    chars = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation
    chars = chars.replace('@', '')
    chars = chars.replace('l', 'L')
    chars = chars.replace('O', 'o')
    chars = chars.replace('I', 'i')
    # size = random.randint(24, 24)
    return ''.join(random.choice(chars) for x in range(int(size)))
    
def main():
    size = os.getenv("PASSWORD_LENGTH")
    print(randompassword(size))

if __name__ == "__main__":
    main()
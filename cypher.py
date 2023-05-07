print('Task 19')

import string  # Allows us to use different functions inside the string module.

'''American Standard Code for Information Interchange (ACII) is the numeric value
 that is given to different characters and symbols.
 '''
alphabet = string.ascii_lowercase  # "abcdefghijklmnopqrstuvwxyz"


def encrypt():  # Creating a function.
    print('TASK: Capstone Project - Cyphers.\n')
    message = input('Please type a message you would like to encrypt: ').lower()
    print()
    key = int(input('Please enter your key shift: '))  # key shift = How much you want your key to shift.

    encrypted_message = ""  # Final encrypted results after you have entered your key shift value.

    for c in message:  # for loop: For characters in message.

        if c in alphabet:
            position = alphabet.find(c)  # find position of characters in the alphabets.
            new_position = (position + key) % 26  # 26 is the count of alphabets
            new_character = alphabet[new_position]
            encrypted_message += new_character
        else:
            encrypted_message += c


    print("Your message after encription is :")
    print(encrypted_message)

encrypt()

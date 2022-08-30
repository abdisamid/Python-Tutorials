# Copyright © 2022 AlgoExpert LLC. All rights reserved.

def caesar_cipher(string, offset):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    encoded_string = ''

    for character in string:
        position = alphabet.index(character)
        offset_position = position - offset
        # No need to handle negative positions because of negative indexing
        encoded_character = alphabet[offset_position]
        encoded_string += encoded_character

    return encoded_string

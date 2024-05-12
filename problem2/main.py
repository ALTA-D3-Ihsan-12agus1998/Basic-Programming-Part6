def caesar(offset, input_str) :
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    result = ''

    for char in input_str :
        if char.isalpha() :
            is_upper = char.isupper()
            char = char.lower()
            shifted_index = (alphabet.index(char) + offset) % 26
            shifted_char = alphabet[shifted_index]
            result += shifted_char.upper() if is_upper else shifted_char
        else:
            result += char

    return result

if __name__ == '__main__':
    print(caesar(3, "abc")) # def
    print(caesar(2, "alta")) # cnvc
    print(caesar(10, "alterraacademy")) # kvdobbkkmknowi
    print(caesar(1, "abcdefghijklmnopqrstuvwxyz")) # bcdefghijklmnopqrstuvwxyza
    print(caesar(1000, "abcdefghijklmnopqrstuvwxyz")) # mnopqrstuvwxyzabcdefghijkl

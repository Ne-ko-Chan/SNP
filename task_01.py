import string

chars_to_strip = string.punctuation + string.whitespace


def is_palindrome(string) -> bool:
    string = str(string)
    string = string.lower()
    stripped = [c for c in string if c not in chars_to_strip]
    i = 0
    j = len(stripped) - 1
    while i != j:
        if stripped[i] != stripped[j]:
            return False
        i += 1
        j -= 1
    return True


# print(is_palindrome("A man, a plan, a canal -- Panama"))
# print(is_palindrome("Madam, I'm Adam!"))
# print(is_palindrome(333))
# print(is_palindrome(None))
# print(is_palindrome("Abracadabra"))

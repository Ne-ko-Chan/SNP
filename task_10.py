import string

chars_to_strip = string.punctuation + string.whitespace


def count_words(string: str) -> dict[str, int]:
    res: dict[str, int] = {}

    string = string.lower()

    # Substitute all unwanted characters with spaces
    # needed to correctly count words in "w1,w2"
    string = "".join([c if c not in chars_to_strip else " " for c in string])
    words = string.split(sep=" ")
    for w in words:
        res[w] = res.get(w, 0) + 1

    # Delete "" entry if it exists
    if res.get("", 0):
        del res[""]
    return res


# print(count_words("A man, a plan, a canal -- Panama!"))
# print(count_words("Doo bee doo bee doo"))

def find_anagram_or_create(map: dict[str, list[str]], word: str) -> None:
    for k, v in map.items():
        k_copy = k
        w_copy = word
        # All letters from k are in word
        for letter in k_copy:
            w_copy = w_copy.replace(letter, "")
        # All letters from word are in k
        for letter in word:
            k = k.replace(letter, "")

        if k == "" and w_copy == "":
            v.append(word)
            return
    map[word] = [word]


def combine_anagrams(words_array: list[str]) -> list[list[str]]:
    res_map = {}
    for word in words_array:
        find_anagram_or_create(res_map, word)
    return [v for _, v in res_map.items()]


print(
    combine_anagrams(
        ["cars", "for", "potatoes", "racs", "four", "scar", "creams", "scream"]
    )
)

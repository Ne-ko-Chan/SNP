import string


class BlockTranspositionCipher:
    def __init__(self, text: str, key: str, decrypt: bool = False) -> None:
        self.parse_key(key)
        self.is_decrypt = decrypt
        self.blocks = self.split_text(text, len(self.key))

    def __next__(self) -> str:
        self.i += 1
        if self.i >= len(self.blocks):
            raise StopIteration

        if not self.is_decrypt:
            res = self.encrypt_block()
            return res

        res = self.decrypt_block()
        if self.i == len(self.blocks) - 1:
            res = res.rstrip(" ")
        return res

    def __iter__(self):
        self.i = -1
        return self

    def parse_key(self, key: str) -> None:
        key = key.lower()
        if not self.validate_key(key):
            raise ValueError("invalid key")

        self.key = self.form_array_key(key)

    def encrypt_block(self) -> str:
        res = [" "] * len(self.key)
        block = self.blocks[self.i]
        for i, letter in enumerate(block):
            res[self.key.index(i)] = letter

        return "".join(res)

    def decrypt_block(self) -> str:
        res = [" "] * len(self.key)
        block = self.blocks[self.i]
        for i, letter in enumerate(block):
            res[self.key[i]] = letter

        return "".join(res)

    @staticmethod
    def split_text(text: str, n: int) -> list[list[str]]:
        res: list[list[str]] = []
        if len(text) % n != 0:
            text = text + " " * (n - len(text) % n)
        for i, v in enumerate(text):
            if i % n == 0:
                res.append([])
            res[-1].append(v)
        return res

    @staticmethod
    def validate_key(key: str) -> bool:
        tostrip = string.ascii_lowercase
        listkey = list(key)
        for c in tostrip:
            for i in range(len(listkey)):
                if listkey[i] == c:
                    del listkey[i]
                    break
        if len(listkey) != 0:
            return False
        return True

    @staticmethod
    def form_array_key(strkey: str) -> list[int]:
        letters = sorted(strkey)
        res = list(map(lambda x: letters.index(x), strkey))
        return res

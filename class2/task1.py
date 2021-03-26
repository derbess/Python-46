from string import ascii_uppercase, ascii_lowercase


class Alphabet:
    def __init__(self, lang, letters):
        self.lang = lang
        self.letters = letters

    def print(self):
        # list_letters = self.letters.split()
        for i in self.letters:
            print(i, end=" ")

    def letters_num(self):
        return len(self.letters)

# al1 = Alphabet("eng", "ABCDE")
# al1.print()
# print(al1.letters_num(), al1.lang)


class EngAlphabet(Alphabet):
    def __init__(self, lang, letters):
        super().__init__(lang, letters)
        self.cnt = len(letters)

    def is_en_letter(self, letter):
        for i in self.letters:
            if i == letter:
                return True
        return False

    def letters_num(self):
        return self.cnt

    @staticmethod
    def example():
        return "The quick brown fox jumps over the lazy dog"


eng = EngAlphabet("eng", ascii_uppercase + ascii_lowercase)
print(eng.letters)
print(eng.is_en_letter('$'))
print(eng.letters_num())
print(eng.example())
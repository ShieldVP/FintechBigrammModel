import random


class Bigramm:
    def __init__(self):
        pass

    def fit(self, path):
        self.model = self._get_continuers(
            ''.join(self._get_text(path)).split()
        )

    def generate(self, path, words_amount):
        word = random.choice(list(self.model.keys()))
        text = word
        for i in range(words_amount):
            next_word = self._choose(self.model[word])
            text += ' ' + next_word
            word = next_word
        with open(path, 'w') as stream:
            stream.write(text)
            
    def _get_text(self, path):
        with open(path) as stream:
            text = stream.read().lower()
            bad_symbols = {
                    ',', '.', '!', '?', '&',
                    '"', "'", ';', ':', '/',
                    '<', '>', '(', ')', '*',
                    '#', '[', ']', '{', '}',
                    '\\', '|', '-', '_', '+',
                    '=', '\n', '\t', '`', '~',
                    '’', '‘', '—', '–', '…',
            }
            return list(filter(lambda symb: symb not in bad_symbols, text))

    def _get_continuers(self, words_sequence):
        dictionary = dict()
        for i, word in enumerate(words_sequence[1:]):
            prev = words_sequence[i - 1]
            if prev in dictionary: 
                dictionary[prev].append(word)
            else:
                dictionary[prev] = [word] 
        return dictionary

    def _choose(self, words_set):
        size = len(words_set)
        chosen_word_number = random.randint(0, size - 1)
        return words_set[chosen_word_number]


if __name__ == "__main__":
    model = Bigramm()
    model.fit("book.txt")
    model.generate("result.txt", 200)
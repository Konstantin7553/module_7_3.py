import string


class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            try:
                with open(file_name, 'r', encoding='utf-8') as file:
                    text = file.read().lower()
                    for char in [',', '.', '=', '!', '?', ';', ':', '-']:
                        text = text.replace(char, '')
                    words = text.split()
                    all_words[file_name] = words
            except FileNotFoundError:
                print(f"File({file_name} not found.")
        return all_words

    def find(self, word):
        word = word.lower()
        result = {}
        all_words = self.get_all_words()
        for file_name, words in all_words.items():
            if word in words:
                result[file_name] = words.index(word)
        return result

    def count(self, word):
        word = word.lower()
        result = {}
        all_words = self.get_all_words()
        for file_name, words in all_words.items():
            result[file_name] = words.count(word)
        return result


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())
print(finder2.find('TEXT'))
print(finder2.count('teXT'))

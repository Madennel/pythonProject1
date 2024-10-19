import string


class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}

        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as file:
                content = file.read().lower()
                translator = str.maketrans('', '', string.punctuation + ' -')
                clean_content = content.translate(translator)
                words = clean_content.split()
                all_words[file_name] = words

        return all_words

    def find(self, word):
        word = word.lower()
        results = {}
        all_words = self.get_all_words()

        for file_name, words in all_words.items():
            if word in words:
                position = words.index(word) + 1
                results[file_name] = position

        return results

    def count(self, word):
        word = word.lower()
        results = {}
        all_words = self.get_all_words()

        for file_name, words in all_words.items():
            count = words.count(word)
            results[file_name] = count

        return results


finder = WordsFinder('test_file.txt')
print(finder.get_all_words())
print(finder.find('TEXT'))
print(finder.count('teXT'))

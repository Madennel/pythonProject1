class WordsFinder:
    def __init__(self, *args):
        self.file_names = args

    def get_all_words(self):
        all_words = {}

        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as f:
                all_words[file_name] = [word.lower().strip('.,=-!?;:') for word in f.read().split()]

        return all_words

    def find(self, word):
        found = {}

        for name, words in self.get_all_words().items():
            if word.lower() in words:
                found[name] = words.index(word.lower()) + 1

        return found

    def count(self, word):
        counted = {}

        for name, words in self.get_all_words().items():
            counted[name] = words.count(word.lower())

        return counted
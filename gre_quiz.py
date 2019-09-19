import csv
import random
import numpy as np


class GREQuiz:
    def __init__(self, words=None):
        self.load_game(words)
        self.incorrect = []

    def load_game(self, accepted_words):
        file_name = 'words.csv'
        words = {}
        with open(file_name, 'r', encoding='utf-8-sig') as csvfile:
            reader = csv.reader(csvfile)
            header = next(reader)
            for row in reader:
                if accepted_words is None:
                    words[row[0]] = row[1]
                if accepted_words is not None:
                    if row[0] in accepted_words:
                        words[row[0]] = row[1]
        self.words = words

    def question(self, word=None):
        if word is None:
            word = random.choice(list(self.words.keys()))
        correct = self.words[word]
        choices = [correct]
        while len(choices) < 5:
            cand = random.choice(list(self.words.values()))
            if cand not in choices:
                choices.append(cand)
        random.shuffle(choices)
        print(f'{word}\n')
        for i in range(len(choices)):
            print(f'{i+1}: {choices[i]}')
        answer = int(input())
        try:
            if choices[answer-1] == correct:
                print('Correct!\n')
                return 1
            else:
                print(f'Wrong, the correct choise is: \n{correct}')
        except:
            print('Invalid choice')
        self.incorrect.append(word)
        return 0

    def play_game(self, limit=np.inf):
        count = 0
        correct = 0
        result = 1
        while count < limit:
            result = self.question()
            if result == 1:
                correct += 1
            count += 1
        return correct/count

    def comprehensive_game(self):
        word_list = list(self.words.keys())
        random.shuffle(word_list)
        correct = 0
        for word in word_list:
            result = self.question(word)
            if result == 1:
                correct += 1



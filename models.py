import math


class NaiveBayesClassifier:
    def __init__(self, training_set, vocabulary, add_delta=0.01, space=10):
        self.training_set = training_set
        self.vocabulary = vocabulary
        self.add_delta = add_delta
        self.space = space

        self.factual_text_count = 0
        self.non_factual_text_count = 0
        self.factual_word_count = 0
        self.non_factual_word_count = 0
        self.factual_word_frequency = dict()
        self.non_factual_word_frequency = dict()

    def train(self):
        print("Determine Word Frequency per Q1 Value")
        for index, row in self.training_set.iterrows():
            text = row["text"]

            is_factual = False
            if row["q1_label"] == "yes":
                is_factual = True
                self.factual_text_count += 1
            elif row["q1_label"] == "no":
                is_factual = False
                self.non_factual_text_count += 1
            else:
                print("huh")

            words = text.split(" ")

            for word in words:
                formatted_word = word.lower()

                if formatted_word not in self.vocabulary:
                    continue

                if is_factual:
                    if formatted_word in self.factual_word_frequency:
                        self.factual_word_frequency[formatted_word] += + 1
                    else:
                        self.factual_word_frequency[formatted_word] = 1
                else:
                    if formatted_word in self.non_factual_word_frequency:
                        self.non_factual_word_frequency[formatted_word] += + 1
                    else:
                        self.non_factual_word_frequency[formatted_word] = 1

        print("Apply Smoothing to Word Frequency")
        print("Count Total Number of Words")
        for word in self.factual_word_frequency:
            self.factual_word_frequency[word] += self.add_delta
            self.factual_word_count += self.factual_word_frequency[word]
        for word in self.non_factual_word_frequency:
            self.non_factual_word_frequency[word] += self.add_delta
            self.non_factual_word_count += self.non_factual_word_frequency[word]

    def evaluate(self, test_set):
        scores = dict()

        for index, row in test_set.iterrows():
            text = row[1]
            factual_score = \
                math.log(self.factual_text_count / (self.factual_text_count + self.non_factual_text_count),
                         self.space)
            non_factual_score = \
                math.log(self.non_factual_text_count / (self.factual_text_count + self.non_factual_text_count),
                         self.space)

            words = text.split(" ")

            for word in words:
                formatted_word = word.lower()

                if formatted_word not in self.vocabulary:
                    continue  # Ignore it

                if formatted_word in self.factual_word_frequency:
                    factual_score += \
                        math.log(self.factual_word_frequency[formatted_word] / self.factual_word_count,
                                 self.space)
                else:
                    factual_score += \
                        math.log(self.add_delta / self.factual_word_count,
                                 self.space)

                if formatted_word in self.non_factual_word_frequency:
                    non_factual_score += \
                        math.log(self.non_factual_word_frequency[formatted_word] / self.non_factual_word_count,
                                 self.space)
                else:
                    non_factual_score += \
                        math.log(self.add_delta / self.non_factual_word_count,
                                 self.space)

            scores[row[0]] = (factual_score, non_factual_score)

        return scores

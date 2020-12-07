class NaiveBayesClassifier:
    def __init__(self, training_set, vocabulary, add_delta=0.01, space=10):
        self.training_set = training_set
        self.vocabulary = vocabulary
        self.add_delta = add_delta
        self.space = space

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
            elif row["q1_label"] == "no":
                is_factual = False
            else:
                print("huh")

            words = text.split(" ")

            for word in words:
                formatted_word = word.lower()

                if formatted_word not in self.vocabulary:
                    continue
                # TODO strip words of things like periods?

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
        return self.get_resulting_trace(), self.get_resulting_evaluation()

    def get_resulting_trace(self):
        pass

    def get_resulting_evaluation(self):
        pass

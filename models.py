class NaiveBayesClassifier:
    def __init__(self, training_set, vocabulary, add_delta, space):
        self.training_set = training_set
        self.vocabulary = vocabulary
        self.add_delta = add_delta
        self.space = space

    def train(self):
        factual_word_count = dict()
        non_factual_word_count = dict()

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
                    if formatted_word in factual_word_count:
                        factual_word_count[formatted_word] += + 1
                    else:
                        factual_word_count[formatted_word] = 1
                else:
                    if formatted_word in non_factual_word_count:
                        non_factual_word_count[formatted_word] += + 1
                    else:
                        non_factual_word_count[formatted_word] = 1

        print("Apply Smoothing to Word Frequency")
        for word in factual_word_count:
            factual_word_count[word] += self.add_delta
        for word in non_factual_word_count:
            non_factual_word_count[word] += self.add_delta

    def evaluate(self, test_set):
        return self.get_resulting_trace(), self.get_resulting_evaluation()

    def get_resulting_trace(self):
        pass

    def get_resulting_evaluation(self):
        pass

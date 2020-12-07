class NaiveBayesClassifier:
    def __init__(self, training_set, vocabulary, add_delta, space):
        self.training_set = training_set
        self.vocabulary = vocabulary
        self.add_delta = add_delta
        self.space = space

    def train(self):
        pass

    def evaluate(self, test_set):
        return self.get_resulting_trace(), self.get_resulting_evaluation()

    def get_resulting_trace(self):
        pass

    def get_resulting_evaluation(self):
        pass

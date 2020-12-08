from data_set_loader import load_dataset
from metrics import output_trace, output_overall_evaluation
from models import NaiveBayesClassifier
from vocabulary import extract_vocabulary_original, extract_vocabulary_filtered

print("Main File Start")

print("1 - THE DATASET")

print("Loading Datasets")
training_set_data = load_dataset("Input/covid_training.tsv")
test_set_data = load_dataset("Input/covid_test_public.tsv", False)

print("2 - THE Naive Bayes Classifier (NB-BOW)")

print("2.1 PARAMETERS")

print("Obtaining Vocabularies")
print("- Original Vocabulary, with all words, for model NB-BOW-OV")
original_vocabulary = extract_vocabulary_original(training_set_data)
print("- Filtered Vocabulary, with only words appearing at least twice, for model NB-BOW-FV")
filtered_vocabulary = extract_vocabulary_filtered(training_set_data)

print("Set additive smoothing add-delta=0.01")
add_delta = 0.01
print("Set space to log base 10 to avoid arithmetic underflow")
space = 10

print("Construct our models")
nb_bow_ov = NaiveBayesClassifier(training_set=training_set_data,
                                 vocabulary=original_vocabulary,
                                 add_delta=add_delta,
                                 space=space)
nb_bow_fv = NaiveBayesClassifier(training_set=training_set_data,
                                 vocabulary=filtered_vocabulary,
                                 add_delta=add_delta,
                                 space=space)

print("Train our models")
nb_bow_ov.train()
nb_bow_fv.train()

print("2.2 OUTPUT")

output_path = "Output/"

print("Output for NB-BOW-OV")
nb_bow_ov_scores = nb_bow_ov.evaluate(test_set=test_set_data)
print("- Trace")
output_trace(test_set_data, nb_bow_ov_scores, output_path + "trace_NB-BOW-OV.txt")
print("- Overall Evaluation File")
output_overall_evaluation(test_set_data, nb_bow_ov_scores, output_path + "eval_NB-BOW-OV.txt")

print("Output for NB-BOW-FV")
nb_bow_fv_scores = nb_bow_fv.evaluate(test_set=test_set_data)
print("- Trace")
output_trace(test_set_data, nb_bow_ov_scores, output_path + "trace_NB-BOW-FV.txt")
print("- Overall Evaluation File")
output_overall_evaluation(test_set_data, nb_bow_fv_scores, output_path + "eval_NB-BOW-FV.txt")

print("3 - THE LSTM CLASSIFIER (LSTM-W2V)")

print("Run the LSTM classifier provided by our wonderful TAs to compare performance")
print("- Code downloaded from https://gitlab.com/Feasinde/lstm-for-covid-disinformation")

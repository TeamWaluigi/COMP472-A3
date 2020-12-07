from data_set_loader import load_dataset
from vocabulary import extract_vocabulary_original, extract_vocabulary_filtered

print("Main File Start")

print("1 - THE DATASET")

print("Loading Datasets")
training_set_data = load_dataset("Input/covid_training.tsv")
test_set_data = load_dataset("Input/covid_test_public.tsv")


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

print("2.2 OUTPUT")

print("Output for NB-BOW-OV")
print("- Trace")
print("- Overall Evaluation File")

print("Output for NB-BOW-FV")
print("- Trace")
print("- Overall Evaluation File")


print("3 - THE LSTM CLASSIFIER (LSTM-W2V)")

print("Run the LSTM classifier provided by our wonderful TAs to compare performance")
print("- Code downloaded from https://gitlab.com/Feasinde/lstm-for-covid-disinformation")





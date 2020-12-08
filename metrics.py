def output_trace(test_dataset, scores, file_path):
    for tweetID in scores:
        factual_score, non_factual_score = scores[tweetID]

        most_likely_class = "yes" if factual_score > non_factual_score else "no"
        top_score_value = factual_score if factual_score > non_factual_score else non_factual_score
        formatted_top_score_value = '{:.2E}'.format(top_score_value)\
            .replace("E+0", "E+")\
            .replace("E-0", "E-")

        correct_class_row = test_dataset.loc[test_dataset[0] == tweetID]
        correct_class = correct_class_row.iloc[0][2]

        grade = "correct" if correct_class == most_likely_class else "wrong"

        # TODO print the following to file
        print(f'{tweetID}  {most_likely_class}  {formatted_top_score_value}  {correct_class}  {grade}')


def output_overall_evaluation(test_dataset, scores, file_path):
    accuracy = 0.99
    yes_p = 0.79
    no_p = 0.356
    yes_r = 0.435
    no_r = 0.32
    yes_f = 0.25
    no_f = 0.9259

    # TODO actual evaluation goes here

    # for some reason, the requirements in the handout demand this format...
    formatted_accuracy = '{:.4f}'.format(accuracy).lstrip('0')
    formatted_yes_p = '{:.4f}'.format(yes_p).lstrip('0')
    formatted_no_p = '{:.4f}'.format(no_p)  # ... and it's different for the no columns
    formatted_yes_r = '{:.4f}'.format(yes_r).lstrip('0')
    formatted_no_r = '{:.4f}'.format(no_r)
    formatted_yes_f = '{:.4f}'.format(yes_f).lstrip('0')
    formatted_no_f = '{:.4f}'.format(no_f)

    # TODO print the following to file
    print(f'{formatted_accuracy}')
    print(f'{formatted_yes_p}  {formatted_no_p}')
    print(f'{formatted_yes_r}  {formatted_no_r}')
    print(f'{formatted_yes_f}  {formatted_no_f}')

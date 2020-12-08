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

        # TODO print to file
        print(f'{tweetID}  {most_likely_class}  {formatted_top_score_value}  {correct_class}  {grade}')


def output_overall_evaluation(test_dataset, scores, file_path):
    pass

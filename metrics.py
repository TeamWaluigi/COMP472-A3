def output_trace(test_dataset, scores, file_path):
    trace_lines = []

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

        trace_lines.append(f'{tweetID}  {most_likely_class}  {formatted_top_score_value}  {correct_class}  {grade}\n')

    file = open(file_path, "w")
    file.writelines(trace_lines)
    file.close()

def output_overall_evaluation(test_dataset, scores, file_path):
    evaluation_lines = []

    correct_classifications = 0
    incorrect_classifications = 0
    yes_tp = 0
    yes_fp = 0
    yes_fn = 0
    yes_tn = 0
    no_tp = 0
    no_fp = 0
    no_fn = 0
    no_tn = 0

    for tweetID in scores:
        factual_score, non_factual_score = scores[tweetID]
        most_likely_class = "yes" if factual_score > non_factual_score else "no"

        correct_class_row = test_dataset.loc[test_dataset[0] == tweetID]
        correct_class = correct_class_row.iloc[0][2]

        if correct_class == most_likely_class:
            correct_classifications += 1
        else:
            incorrect_classifications += 1

        if correct_class == "yes":
            if most_likely_class == "yes":  # on the diagonal
                yes_tp += 1
                no_tn += 1
            else:   # off the diagonal
                yes_fn += 1
                no_fp += 1
        elif correct_class == "no":
            if most_likely_class == "no":  # on the diagonal
                no_tp += 1
                yes_tn += 1
            else:   # off the diagonal
                no_fn += 1
                yes_fp += 1

    accuracy = correct_classifications / (correct_classifications + incorrect_classifications)
    yes_p = yes_tp / (yes_tp + yes_fp)
    no_p = no_tp / (no_tp + no_fp)
    yes_r = yes_tp / (yes_tp + yes_fn)
    no_r = no_tp / (no_tp + no_fn)
    yes_f = (2 * yes_p * yes_r) / (yes_p + yes_r)
    no_f = (2 * no_p * no_r) / (no_p + no_r)

    # for some reason, the requirements in the handout demand this format...
    formatted_accuracy = '{:.4f}'.format(accuracy).lstrip('0')
    formatted_yes_p = '{:.4f}'.format(yes_p).lstrip('0')
    formatted_no_p = '{:.4f}'.format(no_p)  # ... and it's different for the no columns
    formatted_yes_r = '{:.4f}'.format(yes_r).lstrip('0')
    formatted_no_r = '{:.4f}'.format(no_r)
    formatted_yes_f = '{:.4f}'.format(yes_f).lstrip('0')
    formatted_no_f = '{:.4f}'.format(no_f)

    evaluation_lines.append(f'{formatted_accuracy}\n')
    evaluation_lines.append(f'{formatted_yes_p}  {formatted_no_p}\n')
    evaluation_lines.append(f'{formatted_yes_r}  {formatted_no_r}\n')
    evaluation_lines.append(f'{formatted_yes_f}  {formatted_no_f}\n')

    for line in evaluation_lines:
        print(line)

    file = open(file_path, "w")
    file.writelines(evaluation_lines)
    file.close()


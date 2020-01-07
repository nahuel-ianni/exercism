def latest(scores):
    return scores[-1]


def personal_best(scores):
    return max(scores)


def personal_top_three(scores):
    temp_scores = scores.copy()
    temp_scores.sort(reverse=True)

    return temp_scores[0:3]

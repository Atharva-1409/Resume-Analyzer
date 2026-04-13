def score_candidate(candidate, job):
    score = 0

    candidate_skills = set(candidate["skills"].split(","))
    job_skills = set(job["required_skills"].split(","))

    # Skill match
    match = candidate_skills.intersection(job_skills)
    score += len(match) * 15

    # Experience weight
    if candidate["experience"] >= job["min_experience"]:
        score += 25
    else:
        score -= 10

    return score


def rank_candidates(candidates, job):
    ranked = []

    for c in candidates:
        score = score_candidate(c, job)
        ranked.append((c["name"], score))

    return sorted(ranked, key=lambda x: x[1], reverse=True)

def percentile(student, roster):
    """Return the percentile rank (0 to 100) of a student in a roster.

    Args:
        student: the score/value of the student to rank.
        roster: list of all students' scores.

    Returns:
        A float between 0 and 100. A roster with one student returns 100.0.

    Raises:
        ValueError: if the roster is empty or the student is not in it.
    """
    if not roster:
        raise ValueError("roster is empty")
    sorted_roster = sorted(roster)
    if student not in sorted_roster:
        raise ValueError("student not in roster")
    rank_index = sorted_roster.index(student)
    total_students = len(sorted_roster)
    if total_students == 1:
        return 100.0
    return rank_index / (total_students - 1) * 100